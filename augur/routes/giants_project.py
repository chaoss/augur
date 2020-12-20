#SPDX-License-Identifier: MIT
import base64
import sqlalchemy as s
import pandas as pd
import json
from flask import Response
import datetime
import traceback
from typing import Optional, Tuple

def create_routes(server):
    
    def try_func(func):
        def f(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                traceback.print_exc()
                raise e
        return f
    
    @try_func
    def helper_get_issues_with_timestamp_field_between(repo_id, field: str, begin: datetime.datetime, end: datetime.datetime) -> int:
        begin_str = begin.strftime('%Y-%m-%d %H:%M:%S')
        end_str = end.strftime('%Y-%m-%d %H:%M:%S')
        
        issueCountSQL = s.sql.text(f"""
            SELECT
                repo.repo_id,
                COUNT(issue_id) as issue_count
            FROM repo JOIN issues ON repo.repo_id = issues.repo_id
            WHERE repo.repo_id = :repo_id
            AND issues.{field} BETWEEN to_timestamp(:begin_str, 'YYYY-MM-DD HH24:MI:SS') AND to_timestamp(:end_str, 'YYYY-MM-DD HH24:MI:SS')
            GROUP BY repo.repo_id
        """)
        results = pd.read_sql(issueCountSQL, server.augur_app.database, params={
            'repo_id': repo_id,
            'begin_str': begin_str,
            'end_str': end_str
        })
        data_str = results.to_json(orient="records", date_format='iso', date_unit='ms')
        data = json.loads(data_str)
        
        if len(data) < 1:
            return 0
        else:
            return data[0]['issue_count']
    
    @try_func
    def helper_get_open_issues_with_timestamp_field_between(repo_id, field: str, begin: datetime.datetime, end: datetime.datetime) -> int:
        begin_str = begin.strftime('%Y-%m-%d %H:%M:%S')
        end_str = end.strftime('%Y-%m-%d %H:%M:%S')
        
        issueCountSQL = s.sql.text(f"""
            SELECT
                repo.repo_id,
                COUNT(issue_id) as issue_count
            FROM repo JOIN issues ON repo.repo_id = issues.repo_id
            WHERE repo.repo_id = :repo_id
            WHERE issues.closed_at IS NULL
            AND issues.{field} BETWEEN to_timestamp(:begin_str, 'YYYY-MM-DD HH24:MI:SS') AND to_timestamp(:end_str, 'YYYY-MM-DD HH24:MI:SS')
            GROUP BY repo.repo_id
        """)
        results = pd.read_sql(issueCountSQL, server.augur_app.database, params={
            'repo_id': repo_id,
            'begin_str': begin_str,
            'end_str': end_str
        })
        data_str = results.to_json(orient="records", date_format='iso', date_unit='ms')
        data = json.loads(data_str)
        
        if len(data) < 1:
            return 0
        else:
            return data[0]['issue_count']
        
    @try_func
    def helper_get_author_of_most_commits(repo_id) -> Optional[Tuple[str, int]]:
        authorCommitCountSQL = s.sql.text("""
            SELECT
                cmt_author_email,
                COUNT(*) as cmt_count
            FROM commits
            WHERE commits.repo_id = :repo_id
            GROUP BY cmt_author_email
            ORDER BY cmt_count DESC
        """)
        results = pd.read_sql(authorCommitCountSQL, server.augur_app.database, params={
            'repo_id': repo_id
        })
        data_str = results.to_json(orient="records", date_format="iso", date_unit="ms")
        data = json.loads(data_str)
        
        if len(data) < 1:
            return None
        else:
            return (data[0]['cmt_author_email'], data[0]['cmt_count'])
        
    @try_func
    def helper_get_author_of_most_lines_added(repo_id) -> Optional[Tuple[str, int]]:
        authorCommitCountSQL = s.sql.text("""
            SELECT
                cmt_author_email,
                SUM(cmt_added) as line_added_count
            FROM commits
            WHERE commits.repo_id = :repo_id
            GROUP BY cmt_author_email
            ORDER BY line_added_count DESC
        """)
        results = pd.read_sql(authorCommitCountSQL, server.augur_app.database, params={
            'repo_id': repo_id
        })
        data_str = results.to_json(orient="records", date_format="iso", date_unit="ms")
        data = json.loads(data_str)
        
        if len(data) < 1:
            return None
        else:
            return (data[0]['cmt_author_email'], data[0]['line_added_count'])

    @server.app.route('/{}/giants-project/repos'.format(server.api_version))
    def get_all_repo_ids_name_names():
        reposSQL = s.sql.text("""
            SELECT repo.repo_id, repo.repo_name
            FROM repo
            ORDER BY repo.repo_name
        """)
        results = pd.read_sql(reposSQL, server.augur_app.database)
        data_str = results.to_json(orient="records", date_format='iso', date_unit='ms')
        #data = json.loads(data_str)
        #list_data = [item['repo_id'] for item in data]
        #list_data_str = json.dumps(list_data)
        return Response(response=data_str,
                        status=200,
                        mimetype="application/json")

    @server.app.route('/{}/giants-project/status/<repo_id>'.format(server.api_version))
    @try_func
    def get_repo_status(repo_id):
        reposSQL = s.sql.text("""
            SELECT repo.repo_id, repo.repo_name, repo.repo_git AS url
            FROM repo
            WHERE repo.repo_id = :repo_id
        """)
        results = pd.read_sql(reposSQL, server.augur_app.database, params={'repo_id': repo_id})
        data_str = results.to_json(orient="records", date_format='iso', date_unit='ms')
		# TODO: also add basic metric information like listed on https://github.com/zachs18/augur/issues/6
        data = json.loads(data_str)
        
        now = datetime.datetime.now()
        week = datetime.timedelta(days=7)
        year = datetime.timedelta(days=365)
        
        issues_created_past_week = helper_get_issues_with_timestamp_field_between(repo_id, "created_at", now - week, now)
        issues_created_past_year = helper_get_issues_with_timestamp_field_between(repo_id, "created_at", now - year, now)
        
        issues_closed_past_week = helper_get_issues_with_timestamp_field_between(repo_id, "closed_at", now - week, now)
        issues_closed_past_year = helper_get_issues_with_timestamp_field_between(repo_id, "closed_at", now - year, now)
        
        data[0]['issues_created_past_week'] = issues_created_past_week
        data[0]['issues_created_past_year'] = issues_created_past_year
        data[0]['issues_closed_past_week'] = issues_closed_past_week
        data[0]['issues_closed_past_year'] = issues_closed_past_year
        
        author_of_most_commits = helper_get_author_of_most_commits(repo_id)
        
        if author_of_most_commits is not None:
            data[0]['author_of_most_commits'] = author_of_most_commits[0]
            data[0]['author_of_most_commits_count'] = author_of_most_commits[1]
        else:
            data[0]['author_of_most_commits'] = None
            data[0]['author_of_most_commits_count'] = None
        
        author_of_most_lines_added = helper_get_author_of_most_lines_added(repo_id)
        
        if author_of_most_lines_added is not None:
            data[0]['author_of_most_lines_added'] = author_of_most_lines_added[0]
            data[0]['author_of_most_lines_added_count'] = author_of_most_lines_added[1]
        else:
            data[0]['author_of_most_lines_added'] = None
            data[0]['author_of_most_lines_added_count'] = None
        
        return Response(response=json.dumps(data),
                        status=200,
                        mimetype="application/json")
