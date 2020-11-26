
import datetime
import sqlalchemy as s
import pandas as pd
from augur.util import register_metric

@register_metric(type="toss")
def toss_pull_request_acceptance_rate(self, repo_id, begin_date=None, end_date=None, group_by='week'):
    """
    Timeseries of pull request acceptance rate (expressed as the ratio of pull requests merged on a date to the count of pull requests opened on a date)

    :param repo_group_id: The repository's repo_group_id
    :param repo_id: The repository's repo_id, defaults to None
    :return: DataFrame with ratio/day
    """
    if not begin_date:
        begin_date = '1970-1-1 00:00:01'
    if not end_date:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    pr_acceptance_rate_sql = s.sql.text("""
        SELECT CAST
            ( merged.num_approved AS DECIMAL ) / CAST ( opened.num_opened AS DECIMAL ) AS "rate"
        FROM
            (
            SELECT COUNT
                ( pull_request_events.pull_request_id ) AS num_approved,
                repo_id
            FROM
                pull_requests
                JOIN pull_request_events ON pull_request_events.pull_request_id = pull_requests.pull_request_id
            WHERE
                pull_requests.repo_id = :repo_id
                AND ACTION = 'merged'
                OR ACTION = 'ready_for_review'
                AND pull_request_events.created_at BETWEEN :begin_date
                AND :end_date
            GROUP BY
                repo_id
            ) merged
            JOIN (
            SELECT COUNT
                ( pull_request_events.pull_request_id ) AS num_opened,
                repo_id
            FROM
                pull_requests
                JOIN pull_request_events ON pull_request_events.pull_request_id = pull_requests.pull_request_id
            WHERE
                pull_requests.repo_id = :repo_id
                AND ACTION = 'closed'
                AND pull_request_events.created_at BETWEEN :begin_date
                AND :end_date
            GROUP BY
            repo_id
            ) opened ON merged.repo_id = opened.repo_id
    """)
    results = pd.read_sql(pr_acceptance_rate_sql, self.database, params={'repo_id': repo_id, 'group_by': group_by,
                                                    'begin_date': begin_date, 'end_date': end_date})
    return results


@register_metric(type="toss")
def toss_review_duration(self, repo_id, begin_date=None, end_date=None):
    """
    Timeseries of pull request acceptance rate (expressed as the ratio of pull requests merged on a date to the count of pull requests opened on a date)

    :param repo_group_id: The repository's repo_group_id
    :param repo_id: The repository's repo_id, defaults to None
    :return: DataFrame with ratio/day
    """
    if not begin_date:
        begin_date = '1970-1-1 00:00:01'
    if not end_date:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    pr_acceptance_rate_sql = s.sql.text("""
        SELECT SUM
            ( EXTRACT ( EPOCH FROM ( pr_merged_at - pr_created_at ) ) ) / COUNT ( * ) AS duration
        FROM
            pull_requests
            JOIN repo ON pull_requests.repo_id = repo.repo_id
        WHERE
            pull_requests.repo_id = :repo_id
            AND pr_merged_at IS NOT NULL
            AND pr_created_at BETWEEN :begin_date
            AND :end_date
    """)
    results = pd.read_sql(pr_acceptance_rate_sql, self.database, params={'repo_id': repo_id,
                                                    'begin_date': begin_date, 'end_date': end_date})
    results.iloc[0]['duration'] = results.iloc[0]['duration'] / 60 / 60 / 24
    return results