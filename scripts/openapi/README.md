# OpenAPI Spec Generator

Auto-generates an OpenAPI 3.1.0 specification from Augur's Flask route registrations and metric metadata. Produces a complete, accurate spec without requiring a running database or any external services.

## Quick Start

```bash
python scripts/openapi/generate_openapi.py
```

Output: `docs/source/rest-api/openapi.yml`

## How It Works

The generator uses two strategies to introspect routes without a live database:

1. **AST parsing** for all modules. The script parses Python source files as abstract syntax trees, extracting `@app.route()` decorators, HTTP methods, URL patterns, query parameters, auth decorators, and docstrings directly from the source code. This avoids importing `augur.api.server`, which creates a database connection at module level.

2. **Metric metadata extraction** via AST. The `@register_metric()` decorator in `augur/api/util.py` attaches metadata (endpoint name, metric type, model) to each function. The generator reads these from the source rather than importing them, then expands each metric into its standard route set (repo, repo-group, deprecated).

### Route expansion

Each metric type produces a different set of paths:

| Type | Routes Generated |
|------|-----------------|
| `standard` | 3: `/repos/{repo_id}/...`, `/repo-groups/{repo_group_id}/...`, `/repo-groups/{repo_group_id}/repos/{repo_id}/...` (deprecated) |
| `toss` | 1: `/repos/{repo_id}/...` |
| `repo_group_only` | Handled as static routes via `nonstandard_metrics.py` |

### Auth detection

The generator detects three auth decorators and maps them to OpenAPI security schemes:

| Decorator | Security Scheme | Header |
|-----------|----------------|--------|
| `@api_key_required` | `ApiKeyAuth` | `Authorization: Client <key>` |
| `@login_required` | `SessionAuth` | Flask session cookie |
| (GraphQL) | `ApiKeyHeader` | `x-api-key: <key>` |

### Parameter inference

Since Augur routes lack type annotations, parameter types are inferred from naming conventions:

| Pattern | Inferred Type |
|---------|--------------|
| `*_id`, `page`, `page_size` | `integer` |
| `*_date`, `begin_date`, `end_date` | `string` (format: `date-time`) |
| `period`, `group_by`, `sort` | `string` |
| `threshold` | `number` |

## Usage

```
python scripts/openapi/generate_openapi.py [OPTIONS]

Options:
  --output PATH    Output file path (default: docs/source/rest-api/openapi.yml)
  --verbose        Print detailed discovery information
```

### Examples

```bash
# Generate with default output
python scripts/openapi/generate_openapi.py

# Generate with verbose logging
python scripts/openapi/generate_openapi.py --verbose

# Generate to a custom path
python scripts/openapi/generate_openapi.py --output /tmp/augur-api.yml
```

## Output

The generated spec includes:

| Category | Count | Source |
|----------|-------|--------|
| Metric endpoints | 204 | `augur/api/metrics/*.py` (72 functions, expanded to 3 or 1 route each) |
| Static endpoints | 60 | `augur/api/routes/*.py` (12 files) |
| Health endpoints | 5 | Hardcoded (`/ping`, `/status`, `/healthcheck`, etc.) |
| GraphQL endpoint | 1 | Hardcoded (`POST /api/unstable/graphql`) |
| **Total paths** | **270** | |
| **Total operations** | **274** | (some paths have both GET and POST) |

### Components

The spec defines shared components under `#/components/`:

- **Security schemes**: `ApiKeyAuth`, `BearerAuth`, `ApiKeyHeader`, `SessionAuth`
- **Parameters**: `repoIdPath`, `repoGroupIdPath`, `periodQuery`, `beginDateQuery`, `endDateQuery`, `groupByQuery`, `yearQuery`, `thresholdQuery`
- **Schemas**: `MetricResponse`, `StatusResponse`, `ErrorResponse`, `GraphQLRequest`, `GraphQLResponse`

## Validation

```bash
# Validate YAML syntax
python -c "import yaml; yaml.safe_load(open('docs/source/rest-api/openapi.yml'))"

# Validate with a spec linter (if installed)
npx @redocly/cli lint docs/source/rest-api/openapi.yml
```

## Relationship to spec.yml

The repository contains two spec files:

| File | Status | Version |
|------|--------|---------|
| `docs/source/rest-api/spec.yml` | Manually maintained, outdated | v0.60.0 |
| `docs/source/rest-api/openapi.yml` | Auto-generated, current | v0.92.0 |

The `openapi.yml` file replaces `spec.yml` as the source of truth. The old file is kept for reference but should not be used for new integrations.

## Dependencies

The generator uses only Python standard library modules (`ast`, `inspect`, `importlib`, `pathlib`, `re`, `json`) plus `yaml` (PyYAML), which is already an Augur dependency. No additional packages are required.

## Regenerating After Code Changes

Run the generator whenever routes or metrics are added, modified, or removed:

```bash
python scripts/openapi/generate_openapi.py --verbose
git diff docs/source/rest-api/openapi.yml  # Review changes
```

The generated file includes a header comment indicating it should not be edited manually.
