#SPDX-License-Identifier: MIT
from augur.api.routes import AUGUR_API_VERSION
from ..server import app, engine

import base64
import sqlalchemy as s
import pandas as pd
import json
from typing import Dict, Tuple
from flask import Response, request
from werkzeug.datastructures import MultiDict

from augur.application.db.session import DatabaseSession
from augur.application.logs import AugurLogger
from augur.application.config import AugurConfig

logger = AugurLogger("augur").get_logger()

# Magic number configuration for pagination
PAGE_DEFAULT = 1
PAGE_MINMAX = (1, 4000)
COUNT_DEFAULT = 20
COUNT_MINMAX = (1, 50)

def get_args(args: MultiDict, defaults: Dict[str, int]) -> Dict[str, int]:
    """
    Read from the provided `request.args` object, based on defaults.

    Every key in `defaults` is checked on `args`. If that argument is not provided (None), the default is selected.
    So if you have `?foo=12345` and `defaults` is `{"foo": 67890}`, the resulting dict would be `{"foo": 12345}`.
    If instead you had `?bingo=bongos` and the same `defaults`, the resulting dict would be identical to `defaults`.

    If the value is pulled from the URL query, it will be cast to int, and ValueError is thrown if that fails
    """
    return {k: args.get(k, default=v, type=int) for k, v in defaults.items()}

def limit_args(args: Dict[str, int], limits: Dict[str, Tuple[int, int]]) -> bool:
    """
    Checks that each argument is within given bounds, inclusive both ends. If `limits` is `{"foo": (123, 456)}` then
    `args["foo"]` must exist and be some n such that 123<=n<=456. If any argument fails this check, the result is False.

    The list of arguments checked is the list of keys in `limits`.
    """
    return all([limits[key][0] <= args[key] <= limits[key][1] for key in limits])

def paginate(args: MultiDict) -> Tuple[int, int] | Response:
    """
    Sanitize pagination URL parameters and generate the LIMIT and OFFSET values for a paginated SQL query.
    If the parameters are invalid, a response is made with an appropriate error in the JSON body.
    If the parameters are valid, a tuple is returned. The first item is LIMIT, the second is OFFSET.
    """

    # Sanitize query
    # TODO: sanitization is inferior to solutions that make unsafe user input impossible
    try:
        query = get_args(request.args, {"page": PAGE_DEFAULT, "count": COUNT_DEFAULT})
        assert(limit_args(query, {"page": PAGE_MINMAX, "count": COUNT_MINMAX}))
    except ValueError:
        return Response(response='{"status": "Invalid query: page and (optionally) count must be integers"}',
                        status=400,
                        mimetype='application/json')
    except AssertionError:
        return Response(response=('{"status": "Invalid query: '
                                 f'page must be between {PAGE_MINMAX[0]} and {PAGE_MINMAX[1]}, '
                                 f'count between {COUNT_MINMAX[0]} and {COUNT_MINMAX[0]}"}}'),
                        status=400,
                        mimetype='application/json')

    # If a Response hasn't been made yet, the query has been parsed successfully
    return (query["count"], query["count"] * (query["page"] - 1))

@app.route('/{}/repo-groups'.format(AUGUR_API_VERSION))
def get_all_repo_groups(): #TODO: make this name automatic - wrapper?

    # Handle pagination in the URL parameters
    params = paginate(request.args)

    # If the param validation fails, `paginate` generates an HTTP response which we now give to Flask
    if isinstance(params, Response):
        return params

    # If the param validation succeeds, `paginate` generates the integers for the LIMIT/OFFSET query, which we now use
    repoGroupsSQL = s.sql.text("""
        SELECT *
        FROM repo_groups
        ORDER BY rg_name
        LIMIT :len OFFSET :off
    """)
    results = pd.read_sql(repoGroupsSQL,  engine, params={
        "len": params[0],
        "off": params[1]
    })
    data = results.to_json(orient="records", date_format='iso', date_unit='ms')
    return Response(response=data,
                    status=200,
                    mimetype="application/json")

@app.route('/{}/repos'.format(AUGUR_API_VERSION))
def get_all_repos():

    # Handle pagination in the URL parameters
    params = paginate(request.args)

    # If the param validation fails, `paginate` generates an HTTP response which we now give to Flask
    if isinstance(params, Response):
        return params

    # If the param validation succeeds, `paginate` generates the integers for the LIMIT/OFFSET query, which we now use
    get_all_repos_sql = s.sql.text("""
        SELECT
            repo.repo_id,
            repo.repo_name,
            repo.description,
            repo.repo_git AS url,
            a.commits_all_time,
            b.issues_all_time,
            c.pull_requests_all_time,
            rg_name,
            repo.repo_group_id
        FROM
            repo
            left outer join
            (select * from api_get_all_repos_commits ) a on
            repo.repo_id = a.repo_id
            left outer join
            (select * from api_get_all_repos_issues) b
            on
            repo.repo_id = b.repo_id
            left outer join
            (select * from api_get_all_repo_prs) c
            on repo.repo_id=c.repo_id
            JOIN repo_groups ON repo_groups.repo_group_id = repo.repo_group_id
        order by repo_name
        LIMIT :len OFFSET :off
    """)
    results = pd.read_sql(get_all_repos_sql, engine, params={
        "len": params[0],
        "off": params[1]
    })
    results['url'] = results['url'].apply(lambda datum: datum.split('//')[1])

    b64_urls = []
    for i in results.index:
        b64_urls.append(base64.b64encode((results.at[i, 'url']).encode()))
    results['base64_url'] = b64_urls

    data = results.to_json(orient="records", date_format='iso', date_unit='ms')
    return Response(response=data,
                    status=200,
                    mimetype="application/json")

@app.route('/{}/repo-groups/<repo_group_id>/repos'.format(AUGUR_API_VERSION))
def get_repos_in_repo_group(repo_group_id):

    # Handle pagination in the URL parameters
    params = paginate(request.args)

    # If the param validation fails, `paginate` generates an HTTP response which we now give to Flask
    if isinstance(params, Response):
        return params

    # If the param validation succeeds, `paginate` generates the integers for the LIMIT/OFFSET query, which we now use
    repos_in_repo_groups_SQL = s.sql.text("""
        SELECT
            repo.repo_id,
            repo.repo_name,
            repo.description,
            repo.repo_git AS url,
            a.commits_all_time,
            b.issues_all_time,
            c.pull_requests_all_time
        FROM
            repo
            left outer join
            (select * from api_get_all_repos_commits) a on
            repo.repo_id = a.repo_id
            left outer join
            (select * from api_get_all_repos_issues) b
            on
            repo.repo_id = b.repo_id
            left outer join
            (select * from api_get_all_repo_prs) c
            on repo.repo_id=c.repo_id
            JOIN repo_groups ON repo_groups.repo_group_id = repo.repo_group_id
        WHERE
            repo_groups.repo_group_id = :repo_group_id
        ORDER BY repo.repo_git
        LIMIT :len OFFSET :off
    """)

    results = pd.read_sql(repos_in_repo_groups_SQL, engine, params={
        'repo_group_id': repo_group_id,
        "len": params[0],
        "off": params[1]
    })
    data = results.to_json(orient="records", date_format='iso', date_unit='ms')
    return Response(response=data,
                    status=200,
                    mimetype="application/json")

@app.route('/{}/owner/<owner>/repo/<repo>'.format(AUGUR_API_VERSION))
def get_repo_by_git_name(owner, repo):

    get_repo_by_git_name_sql = s.sql.text("""
        SELECT repo.repo_id, repo.repo_group_id, rg_name
        FROM repo JOIN repo_groups ON repo_groups.repo_group_id = repo.repo_group_id
        WHERE repo_name = :repo AND repo_path LIKE :owner
        GROUP BY repo_id, rg_name
    """)

    results = pd.read_sql(get_repo_by_git_name_sql, engine, params={'owner': '%{}_'.format(owner), 'repo': repo,})
    data = results.to_json(orient="records", date_format='iso', date_unit='ms')
    return Response(response=data,
                    status=200,
                    mimetype="application/json")

@app.route('/{}/rg-name/<rg_name>/repo-name/<repo_name>'.format(AUGUR_API_VERSION))
def get_repo_by_name(rg_name, repo_name):

    get_repo_by_name_sql = s.sql.text("""
        SELECT repo_id, repo.repo_group_id, repo_git as url
        FROM repo, repo_groups
        WHERE repo.repo_group_id = repo_groups.repo_group_id
        AND LOWER(rg_name) = LOWER(:rg_name)
        AND LOWER(repo_name) = LOWER(:repo_name)
    """)
    results = pd.read_sql(get_repo_by_name_sql, engine, params={'rg_name': rg_name, 'repo_name': repo_name})
    results['url'] = results['url'].apply(lambda datum: datum.split('//')[1])
    data = results.to_json(orient="records", date_format='iso', date_unit='ms')
    return Response(response=data,
                    status=200,
                    mimetype="application/json")

@app.route('/{}/rg-name/<rg_name>'.format(AUGUR_API_VERSION))
def get_group_by_name(rg_name):
    groupSQL = s.sql.text("""
        SELECT repo_group_id, rg_name
        FROM repo_groups
        WHERE lower(rg_name) = lower(:rg_name)
    """)
    results = pd.read_sql(groupSQL, engine, params={'rg_name': rg_name})
    data = results.to_json(orient="records", date_format='iso', date_unit='ms')
    return Response(response=data,
                    status=200,
                    mimetype="application/json")

@app.route('/{}/dosocs/repos'.format(AUGUR_API_VERSION))
def get_repos_for_dosocs():
    get_repos_for_dosocs_SQL = s.sql.text("""
        SELECT b.repo_id, CONCAT(a.value || b.repo_group_id || chr(47) || b.repo_path || b.repo_name) AS path
        FROM settings a, repo b
        WHERE a.setting='repo_directory'
    """)

    results = pd.read_sql(get_repos_for_dosocs_SQL,  engine)
    data = results.to_json(orient="records", date_format='iso', date_unit='ms')
    return Response(response=data,
                    status=200,
                    mimetype='application/json')

@app.route('/{}/repo-groups/<repo_group_id>/get-issues'.format(AUGUR_API_VERSION))
@app.route('/{}/repos/<repo_id>/get-issues'.format(AUGUR_API_VERSION))
def get_issues(repo_group_id, repo_id=None):
    if not repo_id:
        get_issues_sql = s.sql.text("""
            SELECT issue_title,
                issues.issue_id,
                issues.repo_id,
                issues.html_url,
                issue_state                                 AS STATUS,
                issues.created_at                           AS DATE,
                count(issue_events.event_id),
                MAX(issue_events.created_at)                AS LAST_EVENT_DATE,
                EXTRACT(DAY FROM NOW() - issues.created_at) AS OPEN_DAY
            FROM issues,
                issue_events
            WHERE issues.repo_id IN (SELECT repo_id FROM repo WHERE repo_group_id = :repo_group_id)
            AND issues.issue_id = issue_events.issue_id
            AND issues.pull_request is NULL
            GROUP BY issues.issue_id
            ORDER by OPEN_DAY DESC
        """)
        results = pd.read_sql(get_issues_sql, engine, params={'repo_group_id': repo_group_id})
    else:
        get_issues_sql = s.sql.text("""
            SELECT issue_title,
                issues.issue_id,
                issues.repo_id,
                issues.html_url,
                issue_state                                 AS STATUS,
                issues.created_at                           AS DATE,
                count(issue_events.event_id),
                MAX(issue_events.created_at)                AS LAST_EVENT_DATE,
                EXTRACT(DAY FROM NOW() - issues.created_at) AS OPEN_DAY,
                repo_name
            FROM issues JOIN repo ON issues.repo_id = repo.repo_id, issue_events
            WHERE issues.repo_id = :repo_id
            AND issues.pull_request IS NULL
            AND issues.issue_id = issue_events.issue_id
            GROUP BY issues.issue_id, repo_name
            ORDER by OPEN_DAY DESC
        """)
        results = pd.read_sql(get_issues_sql, engine, params={'repo_id': repo_id})
    data = results.to_json(orient="records", date_format='iso', date_unit='ms')
    return Response(response=data,
                    status=200,
                    mimetype='application/json')

@app.route('/{}/api-port'.format(AUGUR_API_VERSION))
def api_port():

    with DatabaseSession(logger) as session:

        response = {'port': AugurConfig(logger, session).get_value('Server', 'port')}
        return Response(response=json.dumps(response),
                        status=200,
                        mimetype="application/json")
