#SPDX-License-Identifier: MIT
"""
Group dc metrics for timezone
"""

import datetime
import sqlalchemy as s
import pandas as pd
from augur.util import register_metric

@register_metric()
def timezones(self, repo_group_id, repo_id=None, begin_date=None, end_date=None, period='month'):
    """
    :param repo_id: The repository's id
    :param repo_group_id: The repository's group id
    :param period: To set the periodicity to 'day', 'week', 'month' or 'year', defaults to 'day'
    :param begin_date: Specifies the begin date, defaults to '1970-1-1 00:00:00'
    :param end_date: Specifies the end date, defaults to datetime.now()
    :return: DataFrame of persons/period
    """
    if not begin_date:
        begin_date = '1970-1-1 00:00:01'
    if not end_date:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    timezonesSQL = None

    if repo_id:
        timezonesSQL = s.sql.text(
            """
                SELECT
                    repo_id,
                    cmt_commit_hash,
                    EXTRACT(TIMEZONE_HOUR from cmt_author_timestamp) from commits
                FROM
                    commits, repo
            """
        )

    results = pd.read_sql(timezonesSQL, self.database, params={'repo_id': repo_id, 
        'repo_group_id': repo_group_id,'begin_date': begin_date, 'end_date': end_date, 'period':period})

    return results
