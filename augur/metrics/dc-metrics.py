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
                    repo.repo_id,
                    repo.repo_group_id, 
                    EXTRACT(TIMEZONE_HOUR from cmt_author_timestamp) as timezone, 
                    count(*) as timezone_commits
                FROM
                    commits, repo
                WHERE
                  commits.repo_id = repo.repo_id
                GROUP BY 
                    repo.repo_id, 
                    repo.repo_group_id, 
                    timezone
            """
        )

    results = pd.read_sql(timezonesSQL, self.database, params={'repo_id': repo_id, 
        'repo_group_id': repo_group_id,'begin_date': begin_date, 'end_date': end_date, 'period':period})

    return results

@register_metric()
def emails(self, repo_group_id, repo_id=None, begin_date=None, end_date=None, period='month'):
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

    emailsSQL = None

    if repo_id:
        emailsSQL = s.sql.text(
            """
                SELECT 
	                repo.repo_id,
	                repo.repo_group_id,
	                trim( leading '@' from (substr(commits.cmt_author_raw_email, strpos(commits.cmt_author_raw_email,'@')))) as contributor_email_domain,
                  count(*) as email_domain_count
                FROM
	                commits, repo
                WHERE
                  commits.repo_id = repo.repo_id
                GROUP BY 
	                repo.repo_id, 
	                repo.repo_group_id, 
	                contributor_email_domain
                LIMIT 1000
            """
        )

    results = pd.read_sql(emailsSQL, self.database, params={'repo_id': repo_id, 
        'repo_group_id': repo_group_id,'begin_date': begin_date, 'end_date': end_date, 'period':period})

    return results

@register_metric()
def companies(self, repo_group_id, repo_id=None, begin_date=None, end_date=None, period='month'):
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

    companiesSQL = None

    if repo_id:
        companiesSQL = s.sql.text(
            """
                SELECT
                  repo.repo_id,
                  repo.repo_group_id,
                  contributors.cntrb_company as company,
                  count(*) as company_count
                FROM
                  contributors, repo
                GROUP BY
                  repo.repo_id,
                  repo.repo_group_id,
                  company
                LIMIT 1000
            """
        )

    results = pd.read_sql(companiesSQL, self.database, params={'repo_id': repo_id, 
        'repo_group_id': repo_group_id,'begin_date': begin_date, 'end_date': end_date, 'period':period})

    return results

@register_metric()
def locations(self, repo_group_id, repo_id=None, begin_date=None, end_date=None, period='month'):
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

    locationsSQL = None

    if repo_id:
        locationsSQL = s.sql.text(
            """
                SELECT
	                repo.repo_id,
	                repo.repo_group_id,
	                contributors.cntrb_location as contributor_loc,
	                count(*) as loc_count
                FROM
                  contributors, repo
                GROUP BY
	                repo.repo_id,
	                repo.repo_group_id,
                 contributor_loc
                LIMIT 1000
            """
        )

    results = pd.read_sql(locationsSQL, self.database, params={'repo_id': repo_id, 
        'repo_group_id': repo_group_id,'begin_date': begin_date, 'end_date': end_date, 'period':period})

    return results