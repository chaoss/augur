#SPDX-License-Identifier: MIT
"""
Metrics that provides data about contributors & their associated activity
"""

import datetime
import sqlalchemy as s
import pandas as pd
from augur.api.util import register_metric

from augur.application.db.engine import create_database_engine
engine = create_database_engine()

@register_metric()
def contributors(repo_group_id, repo_id=None, period='day', begin_date=None, end_date=None):
    """
    Returns a timeseries of all the contributions to a project.
    DataFrame has these columns:
    date
    commits
    pull_requests
    issues
    commit_comments
    pull_request_comments
    issue_comments
    total
    :param repo_id: The repository's id
    :param repo_group_id: The repository's group id
    :param period: To set the periodicity to 'day', 'week', 'month' or 'year', defaults to 'day'
    :param begin_date: Specifies the begin date, defaults to '1970-1-1 00:00:00'
    :param end_date: Specifies the end date, defaults to datetime.now()
    :return: DataFrame of persons/period
    """

    # In this version, pull request, pr request comments,issue comments haven't be calculated
    if not begin_date:
        begin_date = '1970-1-1 00:00:01'
    if not end_date:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if repo_id:
        contributorsSQL = s.sql.text("""
            SELECT COUNT(*) 
            FILTER (WHERE pr_src_author_association = 'MEMBER'
	        AND repo_id = :repo_id) as maintainer_count
            FROM augur_data.pull_requests
        """)

        results = pd.read_sql(contributorsSQL, engine, params={'repo_id': repo_id, 'period': period,
                                                                'begin_date': begin_date, 'end_date': end_date})
    else:
        contributorsSQL = s.sql.text("""
            SELECT COUNT(*) 
            FILTER (WHERE pr_src_author_association = 'MEMBER'
	        AND repo_id = :repo_id) as maintainer_count
            FROM augur_data.pull_requests
        """)

        results = pd.read_sql(contributorsSQL, engine, params={'repo_group_id': repo_group_id, 'period': period,
                                                                'begin_date': begin_date, 'end_date': end_date})
    return results