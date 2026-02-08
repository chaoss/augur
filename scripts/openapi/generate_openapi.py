#!/usr/bin/env python3
#SPDX-License-Identifier: MIT
"""
Auto-generate an OpenAPI 3.1.0 specification from Augur's Flask routes.

This script introspects metric modules (via import + inspect) and static route
files (via AST parsing) to produce a complete, accurate OpenAPI spec without
requiring a running database.

Usage:
    python scripts/openapi/generate_openapi.py [--output PATH] [--verbose]
"""

import argparse
import ast
import importlib
import inspect
import os
import re
import sys
from collections import OrderedDict
from pathlib import Path

# ---------------------------------------------------------------------------
# Ensure project root is on sys.path and bypass DB-dependent config loading
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Must be set BEFORE any augur imports so get_development_flag() short-circuits
os.environ["AUGUR_DEV"] = "1"

AUGUR_API_VERSION = "api/unstable"
API_PREFIX = f"/{AUGUR_API_VERSION}"

# Mapping from metric module name -> OpenAPI tag
MODEL_TO_TAG = {
    "commit": "metrics-commits",
    "issue": "metrics-issues",
    "pull_request": "metrics-prs",
    "contributor": "metrics-contributors",
    "release": "metrics-releases",
    "deps": "metrics-deps",
    "repo_meta": "metrics-repo-meta",
    "message": "metrics-messages",
    "insight": "metrics-insights",
    "toss": "metrics-toss",
    "experimental": "metrics-experimental",
    "platform": "metrics-platform",
}

# Mapping from route source file -> OpenAPI tag
FILE_TO_TAG = {
    "util": "utility",
    "application": "application",
    "user": "user",
    "batch": "batch",
    "collection_status": "collection-status",
    "config": "config",
    "complexity": "complexity",
    "metadata": "metadata",
    "dei": "dei",
    "nonstandard_metrics": "nonstandard-metrics",
    "auggie": "auggie",
    "manager": "manager",
}

VERBOSE = False


def log(msg):
    if VERBOSE:
        print(f"  [info] {msg}")


# ============================================================================
# 1. METRIC DISCOVERY (AST-based, no imports needed)
# ============================================================================

def discover_metric_functions():
    """Parse metric modules via AST to extract @register_metric-decorated functions."""
    metrics_dir = PROJECT_ROOT / "augur" / "api" / "metrics"
    metric_files = sorted(
        f for f in metrics_dir.glob("*.py")
        if not f.stem.startswith("__")
    )

    discovered = []
    for filepath in metric_files:
        source = filepath.read_text(encoding="utf-8")
        try:
            tree = ast.parse(source, filename=str(filepath))
        except SyntaxError as e:
            log(f"Warning: syntax error in {filepath}: {e}")
            continue

        model_name = filepath.stem  # e.g. "commit", "issue", "toss"

        for node in ast.walk(tree):
            if not isinstance(node, ast.FunctionDef):
                continue

            reg_info = _find_register_metric_decorator(node)
            if reg_info is None:
                continue

            # Extract function signature from AST
            params = _extract_ast_function_params(node)

            # Extract docstring
            docstring = ast.get_docstring(node) or ""
            parsed_doc = _parse_docstring(docstring)

            # Derive endpoint from function name (same logic as register_metric)
            func_name = node.name
            endpoint = re.sub("_", "-", func_name).lower()
            display_name = re.sub("_", " ", func_name).title()
            metric_type = reg_info.get("type", "standard")
            tag = MODEL_TO_TAG.get(model_name, "metrics")

            info = {
                "function_name": func_name,
                "endpoint": endpoint,
                "name": display_name,
                "type": metric_type,
                "model": model_name,
                "tag": tag,
                "params": params,
                "description": parsed_doc["description"],
                "param_docs": parsed_doc["params"],
                "return_doc": parsed_doc["return_desc"],
                "columns": parsed_doc.get("columns", []),
            }
            discovered.append(info)
            log(f"Metric: {endpoint} (type={metric_type}, model={model_name})")

    log(f"Discovered {len(discovered)} metric functions")
    return discovered


def _find_register_metric_decorator(func_node):
    """Check if a function has @register_metric() and extract its kwargs."""
    for dec in func_node.decorator_list:
        # @register_metric() or @register_metric(type="toss")
        if isinstance(dec, ast.Call):
            func = dec.func
            if isinstance(func, ast.Name) and func.id == "register_metric":
                kwargs = {}
                for kw in dec.keywords:
                    val = _ast_literal(kw.value)
                    if val is not None:
                        kwargs[kw.arg] = val
                return kwargs
        # @register_metric (without parens - unlikely but handle it)
        if isinstance(dec, ast.Name) and dec.id == "register_metric":
            return {}
    return None


def _extract_ast_function_params(func_node):
    """Extract function parameters and defaults from an AST FunctionDef."""
    args = func_node.args
    params = []
    num_defaults = len(args.defaults)
    total_args = len(args.args)
    defaults_offset = total_args - num_defaults

    for i, arg in enumerate(args.args):
        name = arg.arg
        if name == "self":
            continue
        has_default = i >= defaults_offset
        default_val = None
        if has_default:
            default_node = args.defaults[i - defaults_offset]
            default_val = _ast_literal(default_node)
        params.append({
            "name": name,
            "default": default_val,
            "has_default": has_default,
        })

    return params


def _parse_docstring(docstring):
    """Parse multiple docstring formats into structured data.

    Handles:
    - Sphinx-style: :param name: desc, :return: desc
    - NumPy-style: Arguments/Parameters/Returns sections with dashed underlines
    - Legacy @api doc format: @apiDescription, @apiName, etc.
    """
    if not docstring:
        return {"description": "", "params": {}, "return_desc": "", "columns": []}

    lines = docstring.strip().split("\n")
    description_lines = []
    params = {}  # name -> {"desc": str, "type": str|None, "default": str|None}
    return_desc = ""
    columns = []  # DataFrame column names extracted from docstrings

    # Detect format — Sphinx takes priority (some docstrings have stray '-----' lines
    # mixed with :param, which doesn't make them NumPy-style)
    has_sphinx = any(re.match(r"\s*:param\s+", l) for l in lines)
    has_numpy = (any(re.match(r"\s*-{3,}$", l.strip()) for l in lines)
                 and any(re.match(r"\s*(Arguments|Parameters|Returns)\s*$", l.strip()) for l in lines))
    has_apidoc = any(re.match(r"\s*@api\w+", l) for l in lines)

    if has_numpy and not has_sphinx:
        description_lines, params, return_desc, columns = _parse_numpy_docstring(lines)
    elif has_apidoc:
        description_lines, params, return_desc = _parse_apidoc_docstring(lines)
        columns = []
    else:
        # Sphinx-style or plain text
        in_columns = False
        for line in lines:
            stripped = line.strip()
            # Detect DataFrame column listings in any format
            if stripped.lower().startswith("dataframe has these columns"):
                in_columns = True
                continue
            if in_columns:
                if stripped and not stripped.startswith(":") and not stripped.startswith("-"):
                    columns.append(stripped)
                elif stripped.startswith(":") or (not stripped and columns):
                    in_columns = False
                continue
            param_match = re.match(r":param\s+(\w+):\s*(.*)", stripped)
            return_match = re.match(r":return[s]?:\s*(.*)", stripped)
            if param_match:
                params[param_match.group(1)] = {
                    "desc": param_match.group(2),
                    "type": None,
                    "default": None,
                }
            elif return_match:
                return_desc = return_match.group(1)
            elif not stripped.startswith(":"):
                description_lines.append(stripped)

    desc = " ".join(l for l in description_lines if l).strip()

    return {
        "description": desc,
        "params": params,
        "return_desc": return_desc,
        "columns": columns,
    }


def _parse_numpy_docstring(lines):
    """Parse NumPy-style docstring sections."""
    description_lines = []
    params = {}
    return_desc = ""
    columns = []

    section = "description"
    current_param = None
    pending_section = None

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Detect section headers (word followed by dashed underline)
        if re.match(r"^-{3,}$", stripped):
            if pending_section:
                section = pending_section.lower()
                pending_section = None
                current_param = None
            continue

        # Check if this line is a section header (next line is dashes)
        if (i + 1 < len(lines)
                and re.match(r"^\s*-{3,}$", lines[i + 1].strip())
                and stripped and not stripped.startswith("-")):
            pending_section = stripped
            continue

        # Look for DataFrame column listings
        if section == "description" and stripped.lower().startswith("dataframe has these columns"):
            section = "columns"
            continue

        if section == "columns":
            if stripped and not stripped.startswith("-"):
                columns.append(stripped)
            continue

        if section == "description":
            # Skip @api-style lines
            if stripped.startswith("@"):
                continue
            description_lines.append(stripped)

        elif section in ("arguments", "parameters", "params"):
            # Lines like "group_name : str" or "page : int = 0 -> [>= 0]"
            param_match = re.match(
                r"^(\w+)\s*:\s*(\w+)(?:\s*=\s*(\S+))?(?:\s*->.*)?$", stripped
            )
            if param_match:
                pname = param_match.group(1)
                ptype = param_match.group(2)
                pdefault = param_match.group(3)
                params[pname] = {"desc": "", "type": ptype, "default": pdefault}
                current_param = pname
            elif current_param and stripped:
                # Continuation line (indented description)
                existing = params[current_param]["desc"]
                params[current_param]["desc"] = (
                    f"{existing} {stripped}" if existing else stripped
                )

        elif section in ("returns", "return"):
            if stripped:
                return_desc = f"{return_desc} {stripped}".strip() if return_desc else stripped

    return description_lines, params, return_desc, columns


def _parse_apidoc_docstring(lines):
    """Parse legacy @api doc format."""
    description_lines = []
    params = {}
    return_desc = ""

    for line in lines:
        stripped = line.strip()
        desc_match = re.match(r"@apiDescription\s+(.*)", stripped)
        param_match = re.match(r"@apiParam\s+(?:\{(\w+)\}\s+)?(\w+)\s*(.*)", stripped)
        if desc_match:
            description_lines.append(desc_match.group(1))
        elif param_match:
            ptype = param_match.group(1)
            pname = param_match.group(2)
            pdesc = param_match.group(3)
            params[pname] = {"desc": pdesc, "type": ptype, "default": None}
        elif not stripped.startswith("@"):
            description_lines.append(stripped)

    return description_lines, params, return_desc


# ============================================================================
# 2. AST-BASED STATIC ROUTE PARSING
# ============================================================================

def parse_static_routes():
    """Parse route files using AST to extract @app.route definitions."""
    routes_dir = PROJECT_ROOT / "augur" / "api" / "routes"
    route_files = sorted(
        f for f in routes_dir.glob("*.py")
        if not f.stem.startswith("__")
    )

    # Do NOT parse server.py - health routes are built separately via build_health_paths(),
    # and server.py cannot be AST-parsed for routes cleanly due to its GraphQL/metric setup.
    all_files = list(route_files)

    all_routes = []
    for filepath in all_files:
        source = filepath.read_text(encoding="utf-8")
        try:
            tree = ast.parse(source, filename=str(filepath))
        except SyntaxError as e:
            log(f"Warning: syntax error in {filepath}: {e}")
            continue

        file_tag = FILE_TO_TAG.get(filepath.stem, "other")
        if filepath.stem == "server":
            file_tag = "health"

        routes = _extract_routes_from_ast(tree, source, file_tag)
        all_routes.extend(routes)
        if routes:
            log(f"AST-parsed {filepath.name}: {len(routes)} route(s)")

    log(f"Parsed {len(all_routes)} static routes total")
    return all_routes


def _extract_routes_from_ast(tree, source, file_tag):
    """Walk AST to find function definitions with @app.route() decorators."""
    routes = []

    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue

        route_decorators = []
        auth_decorators = []

        for dec in node.decorator_list:
            route_info = _parse_route_decorator(dec)
            if route_info:
                route_decorators.append(route_info)
            auth_name = _parse_auth_decorator(dec)
            if auth_name:
                auth_decorators.append(auth_name)

        if not route_decorators:
            continue

        # Extract docstring
        docstring = ast.get_docstring(node) or ""
        parsed_doc = _parse_docstring(docstring)

        # Extract query params from request.args.get() calls in function body
        query_params = _extract_query_params(node)

        # Detect if function actually uses POST body data
        uses_post_body = _function_uses_post_body(node)

        # Extract path params from function arguments
        func_args = [arg.arg for arg in node.args.args]
        # Get defaults
        num_defaults = len(node.args.defaults)
        defaults_offset = len(node.args.args) - num_defaults
        func_defaults = {}
        for i, default in enumerate(node.args.defaults):
            arg_name = node.args.args[defaults_offset + i].arg
            func_defaults[arg_name] = _ast_literal(default)

        for rd in route_decorators:
            path = rd["path"]
            methods = rd["methods"]

            # Deduplicate GET+POST mirrors: if route declares both but
            # function never reads POST body, emit GET only.
            if not uses_post_body and set(methods) == {"GET", "POST"}:
                methods = ["GET"]
                log(f"Dedup: {path} GET+POST -> GET only (no POST body usage)")

            # Extract Flask path params like <repo_id>
            path_params = re.findall(r"<(\w+(?::\w+)?)>", path)
            # Normalize Flask path to OpenAPI: <repo_id> -> {repo_id}
            openapi_path = re.sub(r"<(?:\w+:)?(\w+)>", r"{\1}", path)

            routes.append({
                "path": openapi_path,
                "methods": methods,
                "function_name": node.name,
                "tag": file_tag,
                "description": parsed_doc["description"],
                "param_docs": parsed_doc["params"],
                "path_params": [p.split(":")[-1] for p in path_params],
                "query_params": query_params,
                "func_args": func_args,
                "func_defaults": func_defaults,
                "auth": auth_decorators,
            })

    return routes


def _function_uses_post_body(func_node):
    """Detect if a function reads POST body data (request.data, request.get_json, request.json, request.form)."""
    for node in ast.walk(func_node):
        # request.get_json()
        if (isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "get_json"
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "request"):
            return True
        # request.data or request.json
        if (isinstance(node, ast.Attribute)
                and node.attr in ("data", "json")
                and isinstance(node.value, ast.Name)
                and node.value.id == "request"):
            return True
        # request.form.get(...)
        if (isinstance(node, ast.Attribute)
                and node.attr == "form"
                and isinstance(node.value, ast.Name)
                and node.value.id == "request"):
            return True
    return False


def _parse_route_decorator(dec):
    """Try to extract route path and methods from an @app.route(...) decorator."""
    # Pattern: @app.route(path_expr, methods=[...])
    if not isinstance(dec, ast.Call):
        return None

    func = dec.func
    # Check for app.route(...)
    if isinstance(func, ast.Attribute) and func.attr == "route":
        if isinstance(func.value, ast.Name) and func.value.id == "app":
            pass  # good
        else:
            return None
    else:
        return None

    if not dec.args:
        return None

    path = _resolve_route_string(dec.args[0])
    if not path:
        return None

    methods = ["GET"]
    for kw in dec.keywords:
        if kw.arg == "methods":
            if isinstance(kw.value, ast.List):
                methods = [_ast_literal(elt) for elt in kw.value.elts if _ast_literal(elt)]

    return {"path": path, "methods": methods}


def _resolve_route_string(node):
    """Resolve a route path from various AST representations."""
    # Simple string constant
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value

    # f-string: f"/{AUGUR_API_VERSION}/user/validate"
    if isinstance(node, ast.JoinedStr):
        parts = []
        for val in node.values:
            if isinstance(val, ast.Constant):
                parts.append(str(val.value))
            elif isinstance(val, ast.FormattedValue):
                # Assume it's AUGUR_API_VERSION
                inner = val.value
                if isinstance(inner, ast.Name) and inner.id == "AUGUR_API_VERSION":
                    parts.append(AUGUR_API_VERSION)
                else:
                    parts.append(AUGUR_API_VERSION)
            else:
                parts.append("")
        return "".join(parts)

    # str.format() call: '/{}/batch'.format(AUGUR_API_VERSION)
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Attribute) and node.func.attr == "format":
            if isinstance(node.func.value, ast.Constant) and isinstance(node.func.value.value, str):
                template = node.func.value.value
                return template.replace("{}", AUGUR_API_VERSION, 1)

    return None


def _parse_auth_decorator(dec):
    """Check if a decorator is an auth-related one."""
    if isinstance(dec, ast.Name):
        if dec.id in ("ssl_required", "api_key_required", "login_required"):
            return dec.id
    if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Name):
        if dec.func.id in ("ssl_required", "api_key_required", "login_required"):
            return dec.func.id
    return None


def _extract_query_params(func_node):
    """Walk a function body to find request.args.get("param") calls."""
    params = {}
    for node in ast.walk(func_node):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        # request.args.get("param_name")
        if (isinstance(func, ast.Attribute) and func.attr == "get"
                and isinstance(func.value, ast.Attribute) and func.value.attr == "args"
                and isinstance(func.value.value, ast.Name) and func.value.value.id == "request"):
            if node.args and isinstance(node.args[0], ast.Constant):
                param_name = node.args[0].value
                default_val = None
                if len(node.args) > 1:
                    default_val = _ast_literal(node.args[1])
                params[param_name] = default_val
        # request.args.get("param") with form: request.form.get(...)
        if (isinstance(func, ast.Attribute) and func.attr == "get"
                and isinstance(func.value, ast.Attribute) and func.value.attr == "form"
                and isinstance(func.value.value, ast.Name) and func.value.value.id == "request"):
            if node.args and isinstance(node.args[0], ast.Constant):
                param_name = node.args[0].value
                if param_name not in params:
                    params[param_name] = None
    return params


def _ast_literal(node):
    """Try to extract a literal value from an AST node."""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.NameConstant):  # Python 3.7 compat
        return node.value
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.Str):
        return node.s
    if isinstance(node, ast.Name):
        if node.id == "None":
            return None
        if node.id == "True":
            return True
        if node.id == "False":
            return False
    return None


# ============================================================================
# 3. BUILD OPENAPI PATHS
# ============================================================================

def build_metric_paths(metrics, skip_deprecated=False):
    """Convert discovered metric functions into OpenAPI path items."""
    paths = OrderedDict()
    for m in metrics:
        mtype = m["type"]
        endpoint = m["endpoint"]

        if mtype == "standard":
            _add_standard_metric_paths(paths, m, endpoint, skip_deprecated=skip_deprecated)
        elif mtype == "toss":
            _add_toss_metric_paths(paths, m, endpoint)
        # repo_group_only, license, etc. are handled via nonstandard_metrics.py AST parsing

    return paths


def _add_standard_metric_paths(paths, m, endpoint, skip_deprecated=False):
    """Add 3 route variants for a standard metric (or 2 if skipping deprecated)."""
    query_params = _metric_query_params(m)

    # 1. Repo-level
    repo_path = f"{API_PREFIX}/repos/{{repo_id}}/{endpoint}"
    paths[repo_path] = {
        "get": _metric_operation(m, "repo", query_params, [_ref_param("repoIdPath")])
    }

    # 2. Repo-group level
    rg_path = f"{API_PREFIX}/repo-groups/{{repo_group_id}}/{endpoint}"
    paths[rg_path] = {
        "get": _metric_operation(m, "repo_group", query_params, [_ref_param("repoGroupIdPath")])
    }

    # 3. Deprecated combined (skip if --skip-deprecated)
    if not skip_deprecated:
        dep_path = f"{API_PREFIX}/repo-groups/{{repo_group_id}}/repos/{{repo_id}}/{endpoint}"
        op = _metric_operation(m, "deprecated_repo", query_params,
                               [_ref_param("repoGroupIdPath"), _ref_param("repoIdPath")])
        op["deprecated"] = True
        op["description"] = (
            f"{op.get('description', '')} "
            f"**Deprecated:** Use `{repo_path}` or `{rg_path}` instead."
        ).strip()
        paths[dep_path] = {"get": op}


def _add_toss_metric_paths(paths, m, endpoint):
    """Add 1 route for a toss metric."""
    query_params = _metric_query_params(m)
    repo_path = f"{API_PREFIX}/repos/{{repo_id}}/{endpoint}"
    paths[repo_path] = {
        "get": _metric_operation(m, "repo", query_params, [_ref_param("repoIdPath")])
    }


def _metric_query_params(m):
    """Build query parameter list from a metric's function signature."""
    # Known shared params that get $ref
    SHARED_PARAMS = {
        "period": "periodQuery",
        "begin_date": "beginDateQuery",
        "end_date": "endDateQuery",
        "group_by": "groupByQuery",
        "year": "yearQuery",
        "threshold": "thresholdQuery",
    }

    params = []
    for p in m["params"]:
        name = p["name"]
        # Skip path params
        if name in ("repo_group_id", "repo_id", "self"):
            continue
        if name in SHARED_PARAMS:
            params.append({"$ref": f"#/components/parameters/{SHARED_PARAMS[name]}"})
        else:
            doc_info = m["param_docs"].get(name, {})
            doc_desc = doc_info.get("desc", "") if isinstance(doc_info, dict) else doc_info
            doc_type = doc_info.get("type") if isinstance(doc_info, dict) else None
            param_def = {
                "name": name,
                "in": "query",
                "required": not p["has_default"],
                "description": doc_desc,
                "schema": _infer_schema(p["default"], param_name=name, docstring_type=doc_type),
            }
            params.append(param_def)
    return params


def _metric_operation(m, prefix, query_params, path_params):
    """Build an OpenAPI operation object for a metric endpoint."""
    suffix_map = {
        "repo": "",
        "repo_group": " (by Repo Group)",
        "deprecated_repo": " (deprecated)",
    }
    op = OrderedDict()
    op["summary"] = m["name"] + suffix_map.get(prefix, "")
    if m["description"]:
        op["description"] = m["description"]
    op["operationId"] = f"{prefix}_{m['function_name']}"
    op["tags"] = [m["tag"]]
    op["parameters"] = path_params + query_params

    # Build response schema from DataFrame columns if available
    response_schema = _metric_response_schema(m)
    op["responses"] = {
        "200": {
            "description": "Successful response",
            "content": {
                "application/json": {
                    "schema": response_schema
                }
            }
        }
    }
    return op


def _metric_response_schema(m):
    """Build a response schema for a metric, using DataFrame columns when available."""
    columns = m.get("columns", [])
    if not columns:
        return {"$ref": "#/components/schemas/MetricResponse"}

    # Build a typed record schema from column names
    properties = OrderedDict()
    for col in columns:
        col_clean = col.strip().rstrip(",")
        if not col_clean:
            continue
        # Infer column types from name patterns
        if col_clean in ("date", "created_at", "updated_at", "closed_at", "merged_at"):
            properties[col_clean] = {"type": "string", "format": "date-time"}
        elif col_clean in ("count", "total", "commits", "pull_requests", "issues",
                           "commit_comments", "pull_request_comments", "issue_comments",
                           "lines_added", "lines_removed", "whitespace", "files"):
            properties[col_clean] = {"type": "integer"}
        elif col_clean.endswith("_id") or col_clean == "id":
            properties[col_clean] = {"type": "integer"}
        elif col_clean in ("repo_name", "login", "email", "name", "action", "status"):
            properties[col_clean] = {"type": "string"}
        else:
            properties[col_clean] = {"type": "string"}

    return {
        "type": "array",
        "items": {
            "type": "object",
            "properties": properties,
        },
        "description": f"Array of records with columns: {', '.join(c.strip().rstrip(',') for c in columns if c.strip())}",
    }


def build_static_paths(routes):
    """Convert AST-parsed static routes into OpenAPI path items."""
    paths = OrderedDict()
    for r in routes:
        openapi_path = r["path"]
        # Skip frontend view routes (not under /api/)
        if not openapi_path.startswith("/api") and not openapi_path.startswith("/ping") \
                and not openapi_path.startswith("/status") and not openapi_path.startswith("/health") \
                and not openapi_path.startswith("/auggie"):
            continue

        for method in r["methods"]:
            method_lower = method.lower()

            op = OrderedDict()
            op["summary"] = _function_name_to_summary(r["function_name"])
            if r["description"]:
                op["description"] = r["description"]
            # Make operationId unique by incorporating path slug
            path_slug = openapi_path.strip("/").replace("/", "_").replace("{", "").replace("}", "")
            op["operationId"] = f"{method_lower}_{path_slug}"
            op["tags"] = [r["tag"]]

            # Build parameters
            parameters = []
            for pp in r["path_params"]:
                parameters.append({
                    "name": pp,
                    "in": "path",
                    "required": True,
                    "schema": _infer_schema(None, param_name=pp),
                })
            for qp_name, qp_default in r["query_params"].items():
                doc_info = r["param_docs"].get(qp_name, {})
                doc_desc = doc_info.get("desc", "") if isinstance(doc_info, dict) else ""
                doc_type = doc_info.get("type") if isinstance(doc_info, dict) else None
                parameters.append({
                    "name": qp_name,
                    "in": "query",
                    "required": False,
                    "description": doc_desc,
                    "schema": _infer_schema(qp_default, param_name=qp_name, docstring_type=doc_type),
                })

            if parameters:
                op["parameters"] = parameters

            # Security
            security = _build_security(r["auth"])
            if security:
                op["security"] = security

            # Request body for POST (only if we kept POST — means function actually uses body)
            if method_lower == "post":
                op["requestBody"] = {
                    "content": {
                        "application/json": {
                            "schema": {"type": "object"}
                        }
                    },
                    "required": True,
                }

            op["responses"] = {
                "200": {
                    "description": "Successful response",
                    "content": {
                        "application/json": {
                            "schema": {"type": "object"}
                        }
                    }
                }
            }

            if openapi_path not in paths:
                paths[openapi_path] = {}
            paths[openapi_path][method_lower] = op

    return paths


def build_health_paths():
    """Build health check endpoint paths."""
    paths = OrderedDict()

    redirect_op = {
        "summary": "Health Check Redirect",
        "description": "Redirects to the API status endpoint.",
        "operationId": "health_redirect",
        "tags": ["health"],
        "responses": {
            "302": {"description": "Redirect to status endpoint"}
        }
    }

    for route in ["/ping", "/status", "/healthcheck"]:
        paths[route] = {"get": dict(redirect_op, operationId=f"health_{route.strip('/')}")}

    status_op = {
        "summary": "API Status",
        "description": "Returns the API status and version.",
        "operationId": "api_status",
        "tags": ["health"],
        "responses": {
            "200": {
                "description": "API is running",
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/StatusResponse"}
                    }
                }
            }
        }
    }
    paths[f"{API_PREFIX}/"] = {"get": dict(status_op, operationId="api_root_status")}
    paths[f"{API_PREFIX}/status"] = {"get": dict(status_op, operationId="api_status_endpoint")}

    return paths


def build_graphql_path():
    """Build the GraphQL endpoint documentation."""
    paths = OrderedDict()

    graphql_op = OrderedDict()
    graphql_op["summary"] = "GraphQL API"
    graphql_op["description"] = (
        "Augur's GraphQL endpoint providing cursor-based paginated access to repository data.\n\n"
        "**Available Query Fields:**\n"
        "- `repos(after: String, limit: Int = 10)` - Paginated list of repositories\n"
        "- `repo(id: Int!)` - Single repository by ID\n"
        "- `issues(after: String, limit: Int = 10)` - Paginated list of issues\n"
        "- `issue(id: Int!)` - Single issue by ID\n"
        "- `prs(after: String, limit: Int = 10)` - Paginated list of pull requests\n"
        "- `pr(id: Int!)` - Single pull request by ID\n"
        "- `messages(after: String, limit: Int = 10)` - Paginated list of messages\n"
        "- `commits(after: String, limit: Int = 10)` - Paginated list of commits\n"
        "- `contributors(after: String, limit: Int = 10)` - Paginated list of contributors\n"
        "- `contributor(id: UUID!)` - Single contributor by UUID\n\n"
        "**Connection Types** return `{ items: [...], page_info: { next_cursor, has_next_page } }`.\n\n"
        "**Nested Fields:**\n"
        "- `RepoType` -> issues, prs, messages, releases\n"
        "- `IssueType` -> repo, messages, labels, assignees\n"
        "- `PullRequestType` -> repo, messages, reviews, labels, assignees, files\n"
        "- `ContributorType` -> issues_opened, pull_requests, pull_request_reviews, commits"
    )
    graphql_op["operationId"] = "graphql_query"
    graphql_op["tags"] = ["graphql"]
    graphql_op["security"] = [{"ApiKeyHeader": []}]
    graphql_op["requestBody"] = {
        "required": True,
        "content": {
            "application/json": {
                "schema": {"$ref": "#/components/schemas/GraphQLRequest"},
                "example": {
                    "query": '{ repos(limit: 5) { items { repo_id repo_name } page_info { has_next_page next_cursor } } }'
                }
            }
        }
    }
    graphql_op["responses"] = {
        "200": {
            "description": "GraphQL query result",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "data": {"type": "object", "description": "Query results"},
                            "errors": {
                                "type": "array",
                                "items": {"type": "object"},
                                "description": "GraphQL errors, if any"
                            }
                        }
                    }
                }
            }
        },
        "403": {
            "description": "Invalid or missing API key"
        }
    }

    paths[f"{API_PREFIX}/graphql"] = {"post": graphql_op, "get": dict(graphql_op, operationId="graphql_graphiql", summary="GraphQL Interactive Explorer (GraphiQL)")}

    return paths


# ============================================================================
# 4. COMPONENTS
# ============================================================================

def build_components():
    """Build the components section of the OpenAPI spec."""
    return {
        "securitySchemes": {
            "ApiKeyAuth": {
                "type": "apiKey",
                "in": "header",
                "name": "Authorization",
                "description": (
                    'Client API key. Pass as "Client <your_api_key>" in the Authorization header, '
                    'or as "client_secret" query/form parameter.'
                )
            },
            "BearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "description": "Bearer token obtained from user session generation."
            },
            "ApiKeyHeader": {
                "type": "apiKey",
                "in": "header",
                "name": "x-api-key",
                "description": "API key for GraphQL endpoint access."
            },
            "SessionAuth": {
                "type": "apiKey",
                "in": "cookie",
                "name": "session",
                "description": "Flask login session cookie."
            },
        },
        "parameters": {
            "repoGroupIdPath": {
                "name": "repo_group_id",
                "in": "path",
                "required": True,
                "schema": {"type": "integer"},
                "description": "The repository group's ID.",
            },
            "repoIdPath": {
                "name": "repo_id",
                "in": "path",
                "required": True,
                "schema": {"type": "integer"},
                "description": "The repository's ID.",
            },
            "periodQuery": {
                "name": "period",
                "in": "query",
                "required": False,
                "schema": {
                    "type": "string",
                    "enum": ["day", "week", "month", "year"],
                    "default": "day",
                },
                "description": "Periodicity for time series data.",
            },
            "beginDateQuery": {
                "name": "begin_date",
                "in": "query",
                "required": False,
                "schema": {"type": "string", "format": "date-time"},
                "description": "Start date filter (defaults to '1970-1-1 00:00:00').",
            },
            "endDateQuery": {
                "name": "end_date",
                "in": "query",
                "required": False,
                "schema": {"type": "string", "format": "date-time"},
                "description": "End date filter (defaults to current date/time).",
            },
            "groupByQuery": {
                "name": "group_by",
                "in": "query",
                "required": False,
                "schema": {
                    "type": "string",
                    "enum": ["week", "month", "year"],
                    "default": "week",
                },
                "description": "Grouping period for aggregation.",
            },
            "yearQuery": {
                "name": "year",
                "in": "query",
                "required": False,
                "schema": {"type": "integer"},
                "description": "Year filter.",
            },
            "thresholdQuery": {
                "name": "threshold",
                "in": "query",
                "required": False,
                "schema": {
                    "type": "number",
                    "format": "float",
                    "default": 0.8,
                    "minimum": 0,
                    "maximum": 1,
                },
                "description": "Threshold value (0.0 to 1.0).",
            },
        },
        "schemas": {
            "MetricResponse": {
                "type": "array",
                "items": {"type": "object", "additionalProperties": True},
                "description": "JSON array of metric data records (pandas DataFrame serialized as records).",
            },
            "StatusResponse": {
                "type": "object",
                "properties": {
                    "status": {"type": "string", "example": "OK"},
                    "version": {"type": "string", "example": "0.92.0"},
                },
            },
            "ErrorResponse": {
                "type": "object",
                "properties": {
                    "status": {"type": "string"},
                },
            },
            "GraphQLRequest": {
                "type": "object",
                "required": ["query"],
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "GraphQL query string.",
                    },
                    "variables": {
                        "type": "object",
                        "description": "Variables for the GraphQL query.",
                    },
                    "operationName": {
                        "type": "string",
                        "description": "Name of the operation to execute.",
                    },
                },
            },
            "PageInfo": {
                "type": "object",
                "properties": {
                    "next_cursor": {"type": "string"},
                    "has_next_page": {"type": "boolean"},
                },
            },
            "BatchRequest": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "method": {"type": "string", "enum": ["GET", "POST"]},
                        "path": {"type": "string"},
                        "body": {"type": "object"},
                    },
                    "required": ["method", "path"],
                },
            },
            "BatchResponse": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "status": {"type": "integer"},
                        "response": {"type": "string"},
                    },
                },
            },
        },
    }


# ============================================================================
# 5. ASSEMBLY
# ============================================================================

def assemble_spec(metric_paths, static_paths, health_paths, graphql_paths, components):
    """Assemble the complete OpenAPI 3.1.0 specification."""

    spec = OrderedDict()
    spec["openapi"] = "3.1.0"
    spec["info"] = OrderedDict([
        ("title", "Augur REST API"),
        ("description",
         "Python 3 package for free/libre and open-source software community "
         "metrics, models & data collection. Part of the CHAOSS project."),
        ("version", "0.92.0"),
        ("contact", OrderedDict([
            ("name", "Augur Team"),
            ("url", "https://github.com/chaoss/augur"),
            ("email", "outdoors@acm.org"),
        ])),
        ("license", OrderedDict([
            ("name", "MIT"),
            ("url", "https://opensource.org/licenses/MIT"),
        ])),
    ])
    spec["externalDocs"] = OrderedDict([
        ("description", "CHAOSS Metric Definitions"),
        ("url", "https://chaoss.community/kb-metrics-and-metrics-models/"),
    ])
    spec["servers"] = [
        {"url": "https://ai.chaoss.io", "description": "Production server"},
        {"url": "http://localhost:5000", "description": "Local development server"},
    ]

    # Tags
    spec["tags"] = [
        {"name": "health", "description": "Health check and status endpoints"},
        {"name": "utility", "description": "Utility endpoints for repos and repo groups"},
        {"name": "metrics-commits", "description": "Commit-related CHAOSS metrics"},
        {"name": "metrics-issues", "description": "Issue-related CHAOSS metrics"},
        {"name": "metrics-prs", "description": "Pull request-related CHAOSS metrics"},
        {"name": "metrics-contributors", "description": "Contributor-related CHAOSS metrics"},
        {"name": "metrics-releases", "description": "Release-related CHAOSS metrics"},
        {"name": "metrics-deps", "description": "Dependency-related CHAOSS metrics"},
        {"name": "metrics-repo-meta", "description": "Repository metadata CHAOSS metrics"},
        {"name": "metrics-messages", "description": "Message/comment-related CHAOSS metrics"},
        {"name": "metrics-insights", "description": "Insight-related CHAOSS metrics"},
        {"name": "metrics-toss", "description": "TOSS (Toward Open Source Sustainability) metrics"},
        {"name": "user", "description": "User authentication and management"},
        {"name": "application", "description": "Client application endpoints"},
        {"name": "config", "description": "Configuration management"},
        {"name": "collection-status", "description": "Data collection status"},
        {"name": "complexity", "description": "Code complexity analysis"},
        {"name": "metadata", "description": "Repository metadata queries"},
        {"name": "batch", "description": "Batch request execution"},
        {"name": "dei", "description": "DEI (Diversity, Equity, Inclusion) badging"},
        {"name": "nonstandard-metrics", "description": "Non-standard metric endpoints"},
        {"name": "auggie", "description": "Auggie assistant integration"},
        {"name": "graphql", "description": "GraphQL API endpoint"},
    ]

    # Merge all paths
    all_paths = OrderedDict()
    for source in [health_paths, static_paths, metric_paths, graphql_paths]:
        for path, methods in source.items():
            if path in all_paths:
                all_paths[path].update(methods)
            else:
                all_paths[path] = OrderedDict(methods)

    spec["paths"] = all_paths
    spec["components"] = components

    return spec


# ============================================================================
# 6. YAML OUTPUT
# ============================================================================

def write_yaml(spec, output_path):
    """Write the spec dict to a YAML file without YAML anchors/aliases."""
    import yaml

    class NoAliasDumper(yaml.SafeDumper):
        """YAML dumper that never emits anchors (&id001) or aliases (*id001)."""
        def ignore_aliases(self, data):
            return True

    def _dict_representer(dumper, data):
        return dumper.represent_mapping("tag:yaml.org,2002:map", data.items())

    NoAliasDumper.add_representer(OrderedDict, _dict_representer)
    NoAliasDumper.add_representer(dict, _dict_representer)

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "w", encoding="utf-8") as f:
        f.write("# Auto-generated OpenAPI 3.1.0 specification for Augur REST API\n")
        f.write("# Generated by: scripts/openapi/generate_openapi.py\n")
        f.write(f"# Version: {spec['info']['version']}\n")
        f.write("# Do not edit manually - regenerate with: python scripts/openapi/generate_openapi.py\n\n")
        yaml.dump(
            dict(spec),  # convert top-level OrderedDict for clean output
            f,
            Dumper=NoAliasDumper,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            width=120,
        )

    print(f"Wrote OpenAPI spec to: {output}")


# ============================================================================
# 7. HELPERS
# ============================================================================

def _ref_param(name):
    return {"$ref": f"#/components/parameters/{name}"}


def _infer_schema(default_value, param_name=None, docstring_type=None):
    """Infer an OpenAPI schema from default value, parameter name, and docstring type hints."""
    # Priority 1: Known parameter name patterns
    if param_name:
        name_schema = _schema_from_param_name(param_name)
        if name_schema:
            if default_value is not None and "default" not in name_schema:
                name_schema["default"] = default_value
            return name_schema

    # Priority 2: Docstring type annotation
    if docstring_type:
        type_map = {
            "str": {"type": "string"},
            "string": {"type": "string"},
            "int": {"type": "integer"},
            "integer": {"type": "integer"},
            "float": {"type": "number"},
            "bool": {"type": "boolean"},
            "boolean": {"type": "boolean"},
            "list": {"type": "array", "items": {"type": "string"}},
        }
        schema = type_map.get(docstring_type.lower(), {"type": "string"})
        if default_value is not None:
            schema = dict(schema)
            schema["default"] = default_value
        return schema

    # Priority 3: Default value type
    if default_value is not None:
        if isinstance(default_value, bool):
            return {"type": "boolean", "default": default_value}
        if isinstance(default_value, int):
            return {"type": "integer", "default": default_value}
        if isinstance(default_value, float):
            return {"type": "number", "default": default_value}
        if isinstance(default_value, str):
            return {"type": "string", "default": default_value}

    return {"type": "string"}


# Well-known parameter name -> schema mapping
_PARAM_NAME_SCHEMAS = {
    "page": {"type": "integer", "minimum": 0, "default": 0},
    "page_size": {"type": "integer", "minimum": 1, "default": 25},
    "repo_id": {"type": "integer"},
    "repo_group_id": {"type": "integer"},
    "issue_id": {"type": "integer"},
    "pr_id": {"type": "integer"},
    "commit_id": {"type": "integer"},
    "user_id": {"type": "integer"},
    "group_id": {"type": "integer"},
    "application_id": {"type": "integer"},
    "limit": {"type": "integer", "minimum": 1},
    "offset": {"type": "integer", "minimum": 0},
}


def _schema_from_param_name(name):
    """Infer schema from well-known parameter names."""
    if name in _PARAM_NAME_SCHEMAS:
        return dict(_PARAM_NAME_SCHEMAS[name])
    # Pattern-based inference
    if name.endswith("_id") or name == "id":
        return {"type": "integer"}
    if name.endswith("_date") or name in ("begin_date", "end_date", "start_date"):
        return {"type": "string", "format": "date-time"}
    if name in ("sort", "direction", "order", "order_by", "sort_by"):
        return {"type": "string"}
    if name in ("count", "total", "num", "number"):
        return {"type": "integer"}
    return None


def _function_name_to_summary(name):
    """Convert a Python function name to a human-readable summary."""
    return name.replace("_", " ").replace("-", " ").title()


def _build_security(auth_decorators):
    """Build OpenAPI security requirements from decorator names."""
    if not auth_decorators:
        return []
    security = []
    if "api_key_required" in auth_decorators:
        security.append({"ApiKeyAuth": []})
    if "login_required" in auth_decorators:
        security.append({"SessionAuth": []})
        security.append({"BearerAuth": []})
    return security


def validate_spec(spec):
    """Run basic structural validation on the generated spec."""
    errors = []
    operation_ids = set()

    paths = spec.get("paths", {})
    for path, methods in paths.items():
        if not path.startswith("/"):
            errors.append(f"Path does not start with /: {path}")

        for method, op in methods.items():
            if method not in ("get", "post", "put", "delete", "patch", "options", "head"):
                continue
            op_id = op.get("operationId", "")
            if op_id in operation_ids:
                errors.append(f"Duplicate operationId: {op_id}")
            operation_ids.add(op_id)

            if "responses" not in op:
                errors.append(f"Missing responses for {method.upper()} {path}")

            if "tags" not in op or not op["tags"]:
                errors.append(f"Missing tags for {method.upper()} {path}")

    # Check $ref resolution
    components = spec.get("components", {})
    for path, methods in paths.items():
        for method, op in methods.items():
            if method not in ("get", "post", "put", "delete", "patch", "options", "head"):
                continue
            for param in op.get("parameters", []):
                ref = param.get("$ref", "")
                if ref:
                    ref_parts = ref.split("/")
                    if len(ref_parts) == 4 and ref_parts[1] == "components":
                        section = ref_parts[2]
                        key = ref_parts[3]
                        if key not in components.get(section, {}):
                            errors.append(f"Unresolved $ref: {ref}")

    return errors


# ============================================================================
# MAIN
# ============================================================================

def main():
    global VERBOSE

    parser = argparse.ArgumentParser(
        description="Generate OpenAPI 3.1.0 spec from Augur Flask routes"
    )
    parser.add_argument(
        "--output", "-o",
        default=str(PROJECT_ROOT / "docs" / "source" / "rest-api" / "openapi.yml"),
        help="Output file path (default: docs/source/rest-api/openapi.yml)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print detailed discovery information",
    )
    parser.add_argument(
        "--skip-deprecated",
        action="store_true",
        help="Omit deprecated endpoint variants from the spec",
    )
    args = parser.parse_args()
    VERBOSE = args.verbose

    print("Augur OpenAPI Spec Generator")
    print("=" * 40)

    # Step 1: Discover metrics
    print("\n[1/6] Discovering metric functions...")
    metrics = discover_metric_functions()
    standard_count = sum(1 for m in metrics if m["type"] == "standard")
    toss_count = sum(1 for m in metrics if m["type"] == "toss")
    other_count = len(metrics) - standard_count - toss_count
    print(f"  Found {len(metrics)} metrics ({standard_count} standard, {toss_count} toss, {other_count} other)")

    # Step 2: Parse static routes
    print("\n[2/6] Parsing static routes via AST...")
    static_routes = parse_static_routes()
    print(f"  Found {len(static_routes)} static route definitions")

    # Step 3: Build metric paths
    print("\n[3/6] Building metric endpoint paths...")
    if args.skip_deprecated:
        print("  (--skip-deprecated: omitting deprecated route variants)")
    metric_paths = build_metric_paths(metrics, skip_deprecated=args.skip_deprecated)
    print(f"  Generated {len(metric_paths)} metric path items")

    # Step 4: Build static paths + health + GraphQL
    print("\n[4/6] Building static, health, and GraphQL paths...")
    static_paths = build_static_paths(static_routes)
    health_paths = build_health_paths()
    graphql_paths = build_graphql_path()
    print(f"  Generated {len(static_paths)} static + {len(health_paths)} health + {len(graphql_paths)} GraphQL path items")

    # Step 5: Build components
    print("\n[5/6] Building components (schemas, parameters, security)...")
    components = build_components()

    # Step 6: Assemble and write
    print("\n[6/6] Assembling and writing spec...")
    spec = assemble_spec(metric_paths, static_paths, health_paths, graphql_paths, components)

    # Validate
    errors = validate_spec(spec)
    if errors:
        print(f"\n  Validation warnings ({len(errors)}):")
        for err in errors[:20]:
            print(f"    - {err}")
        if len(errors) > 20:
            print(f"    ... and {len(errors) - 20} more")
    else:
        print("  Validation: OK (no structural errors)")

    write_yaml(spec, args.output)

    # Summary
    total_paths = len(spec["paths"])
    total_ops = sum(
        1 for methods in spec["paths"].values()
        for m in methods
        if m in ("get", "post", "put", "delete", "patch")
    )
    print(f"\nSummary:")
    print(f"  Total paths: {total_paths}")
    print(f"  Total operations: {total_ops}")
    print(f"  Metric endpoints: {len(metric_paths)}")
    print(f"  Static endpoints: {len(static_paths)}")
    print(f"  Health endpoints: {len(health_paths)}")
    print(f"  GraphQL endpoints: {len(graphql_paths)}")


if __name__ == "__main__":
    main()
