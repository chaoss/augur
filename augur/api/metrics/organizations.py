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
def maintainers(repo_group_id, repo_id=None, period='day', begin_date=None, end_date=None):
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

    # In this version, pull request, pr request comments,issue comments haven't been calculated
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
    # Not written for repo_group_id as written
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

def organizational_influence(repo_group_id, repo_id=None, begin_date=None, end_date=None):
    """
    Returns the percent of pull requests that were made by each company during the period.

    :param repo_id: The repository's id
    :param repo_group_id: The repository's group id
    :param begin_date: Specifies the begin date, defaults to '1970-1-1 00:00:00'
    :param end_date: Specifies the end date, defaults to datetime.now()
    """

    if not begin_date:
        begin_date = '1970-1-1 00:00:01'
    if not end_date:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if repo_id:
        orgInfluence = s.sql.text("""
            SELECT
                lower(trim(LEADING '@' from trim(BOTH from cntrb_company))) as cntrb_company,
                COUNT(*)::float / (
                    SELECT count(pr_created_at) AS total_contributions
                    FROM augur_data.pull_requests
                    WHERE repo_id = :repo_id
                    and pr_created_at between :begin_date and :end_date
                ) AS percent_cntrb
            FROM augur_data.contributors
                INNER JOIN (
                    SELECT pr_augur_contributor_id, pr_merged_at
                    FROM augur_data.pull_requests
                    WHERE repo_id = :repo_id
                        and pr_created_at between :begin_date and :end_date
                ) AS pr_cntrb_id
                ON contributors.cntrb_id=pr_cntrb_id.pr_augur_contributor_id
                WHERE contributors.cntrb_company is not null
            GROUP BY lower(trim(LEADING '@' from trim(BOTH from cntrb_company)));
        """)

        results = pd.read_sql(orgInfluence, engine, params={'repo_id': repo_id, 'begin_date': begin_date, 'end_date': end_date})

        # Not not written for repo_group_id as written
    else:
        orgInfluence = s.sql.text("""
            SELECT
                lower(trim(LEADING '@' from trim(BOTH from cntrb_company))) as cntrb_company,
                COUNT(*)::float / (
                    SELECT count(pr_created_at) AS total_contributions
                    FROM augur_data.pull_requests
                    WHERE repo_id = :repo_id
                    and pr_created_at between :begin_date and :end_date
                ) AS percent_cntrb
            FROM augur_data.contributors
                INNER JOIN (
                    SELECT pr_augur_contributor_id, pr_merged_at
                    FROM augur_data.pull_requests
                    WHERE repo_id = :repo_id
                        and pr_created_at between :begin_date and :end_date
                ) AS pr_cntrb_id
                ON contributors.cntrb_id=pr_cntrb_id.pr_augur_contributor_id
                WHERE contributors.cntrb_company is not null
            GROUP BY lower(trim(LEADING '@' from trim(BOTH from cntrb_company)));
        """)

        results = pd.read_sql(orgInfluence, engine, params={'repo_group_id': repo_group_id, 'begin_date': begin_date, 'end_date': end_date})

    return results

def peripheral_organizations(repo_group_id, repo_id=None):
    """
    Returns the number of pull requests, date of first pull request, and date of latest pull request associated with each company

    :param repo_id: The repository's id
    :param repo_group_id: The repository's group id
    """

    if repo_id:
        po = s.sql.text("""
            select lower(trim(LEADING '@' from trim(BOTH from cntrb_company))) as organization_name, count(pr_merged_at) as number_of_contributions,
            min(pr_merged_at) as first_contribution, max(pr_merged_at) as last_contribution
            from augur_data.pull_requests
            inner join augur_data.contributors on pull_requests.pr_augur_contributor_id = contributors.cntrb_id
            where cntrb_company is not null and pr_merged_at is not null
            and repo_id = :repo_id
            group by lower(trim(LEADING '@' from trim(BOTH from cntrb_company)));
        """)

        results = pd.read_sql(po, engine, params={'repo_id': repo_id,})

    # Not written for repo_group_id as written
    else:
        po = s.sql.text("""
            select lower(trim(LEADING '@' from trim(BOTH from cntrb_company))) as organization_name, count(pr_merged_at) as number_of_contributions,
            min(pr_merged_at) as first_contribution, max(pr_merged_at) as last_contribution
            from augur_data.pull_requests
            inner join augur_data.contributors on pull_requests.pr_augur_contributor_id = contributors.cntrb_id
            where cntrb_company is not null and pr_merged_at is not null
            and repo_id = :repo_id
            group by lower(trim(LEADING '@' from trim(BOTH from cntrb_company)));
        """)

        results = pd.read_sql(po, engine, params={'repo_group_id': repo_group_id,})

    return results