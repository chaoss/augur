"""
Metrics that provides data about issues & their associated activity
"""

import datetime
import sqlalchemy as s
import pandas as pd
from augur.util import logger, annotate, add_metrics

@annotate(tag='contributor-location')
def contributor_location(self, repo_group_id, repo_id=None, period='day', begin_date=None, end_date=None):
    """Returns the lat and long of all contributors.

    :param repo_group_id: The repository's repo_group_id
    :param repo_id: The repository's repo_id, defaults to None
    :param period: To set the periodicity to 'day', 'week', 'month' or 'year', defaults to 'day'
    :param begin_date: Specifies the begin date, defaults to '1970-1-1 00:00:00'
    :param end_date: Specifies the end date, defaults to datetime.now()
    :return: DataFrame of contributor lat and long/period
    """

    if not begin_date:
        begin_date = '1970-1-1 00:00:00'

    if not end_date:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    contributor_location_SQL = ''

    if not repo_id:
        contributor_location_SQL = s.sql.text("""
            SELECT
                issues.repo_id,
                repo_name,
                date_trunc(:period, issues.created_at::DATE) as date,
                COUNT(issue_id) as issues
            FROM issues JOIN repo ON issues.repo_id = repo.repo_id
            WHERE issues.repo_id IN (SELECT repo_id FROM repo WHERE repo_group_id = :repo_group_id)
            AND issues.created_at BETWEEN to_timestamp(:begin_date, 'YYYY-MM-DD HH24:MI:SS') AND to_timestamp(:end_date, 'YYYY-MM-DD HH24:MI:SS')
            AND issues.pull_request IS NULL
            GROUP BY issues.repo_id, date, repo_name
            ORDER BY issues.repo_id, date
        """)

        results = pd.read_sql(contributor_location_SQL, self.database, params={'repo_group_id': repo_group_id, 'period': period,'begin_date': begin_date, 'end_date': end_date})

        # if necessary, do some more transformations or calculations on the result

        return results

    else:
        contributor_location_SQL = s.sql.text("""
            SELECT
                repo_name,
                date_trunc(:period, issues.created_at::DATE) as date,
                COUNT(issue_id) as issues
            FROM issues JOIN repo ON issues.repo_id = repo.repo_id
            WHERE issues.repo_id = :repo_id
            AND issues.created_at BETWEEN to_timestamp(:begin_date, 'YYYY-MM-DD HH24:MI:SS') AND to_timestamp(:end_date, 'YYYY-MM-DD HH24:MI:SS')
            AND issues.pull_request IS NULL
            GROUP BY date, repo_name
            ORDER BY date;
        """)

        results = pd.read_sql(contributor_location_SQL, self.database, params={'repo_id': repo_id, 'period': period, 'begin_date': begin_date, 'end_date': end_date})

        # if necessary, do some more transformations or calculations on the result

        return results