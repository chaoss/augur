"""
Metrics that provides data about issues & their associated activity
"""

import datetime
import sqlalchemy as s
import pandas as pd
from augur.util import logger, annotate, add_metrics

@annotate(tag='issue-messages-over-time')
def issue_messages_over_time(self, repo_group_id, repo_id=None, period='week', begin_date=None, end_date=None):
    """
    Returns a list of Repos within the repo group, the number of issues within the last 60 days, and the number of messages 
    on the issues
    In this timeseries there is a dataframe for each repo in the repo_group
    repo_id
    issues
    messages
    
    :param repo_group_id: The repository's group id
    """
    if not begin_date:
    #    begin_date = (datetime.datetime.today() - datetime.timedelta(days=60))
        begin_date = '1970-1-1 00:00:01'
    if not end_date:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if repo_id:
        issue_messages_over_time_SQL = s.sql.text("""
            SELECT 
                date_trunc(:period, msg_timestamp::DATE) as message_creation_date,
                COUNT(r.msg_id) as comments
            FROM augur_data.issues issues
                INNER JOIN augur_data.repo repo 
                    ON repo.repo_id = issues.repo_id
                INNER JOIN augur_data.issue_message_ref r
                                ON r.issue_id = issues.issue_id
                INNER JOIN augur_data.message m
                            ON m.msg_id = r.msg_id
            WHERE repo.repo_id = :repo_id
                AND m.msg_timestamp BETWEEN :begin_date AND :end_date
            GROUP BY message_creation_date
            ORDER BY message_creation_date
        """)

        results = pd.read_sql(issue_messages_over_time_SQL, self.database, params={'repo_id': repo_id, 'period': period, 'begin_date': begin_date, 'end_date': end_date})
    
    else:
        issue_messages_over_time_SQL = s.sql.text("""
            SELECT 
                date_trunc('week', msg_timestamp::DATE) as message_creation_date,
                COUNT(r.msg_id) as comments
            FROM augur_data.issues issues
                INNER JOIN augur_data.repo repo 
                ON repo.repo_id = issues.repo_id
                INNER JOIN augur_data.issue_message_ref r
                ON r.issue_id = issues.issue_id
                INNER JOIN augur_data.message m
                ON m.msg_id = r.msg_id
            WHERE repo.repo_id IN (SELECT repo_id FROM augur_data.repo WHERE repo_group_id=:repo_group_id)
                AND m.msg_timestamp BETWEEN :begin_date AND :end_date
            GROUP BY message_creation_date
            ORDER BY message_creation_date
        """)
        results = pd.read_sql(issue_messages_over_time_SQL, self.database, params={'repo_group_id': repo_group_id, 'period': period,
                                                                        'begin_date': begin_date, 'end_date': end_date})
    return results


@annotate(tag='issues-first-response')
def issues_first_response(self, repo_group_id, repo_id=None, period='month', begin_date=None, end_date=None):
    #TODO: add timeseries period and begin/end dates to query
    """
    Returns a timeseries of the average time between issue open and first response
    Each dataframe includes the timeframe (default: month) and average issue response time during that timeframe
    """
    if not begin_date:
        begin_date = '1970-1-1 00:00:01'
    if not end_date:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if repo_id:
        issuesFirstReponseSQL = s.sql.text("""
            SELECT  date_trunc(:period, created_at::DATE) as issue_creation_date,
                    AVG(dif) as response_time 
            FROM(
                SELECT  issues.issue_id as issue,
                        MIN(msg_timestamp - created_at) as dif,
                        repo_id as repo,
                        created_at
                FROM augur_data.issues
                    INNER JOIN augur_data.issue_message_ref r
                    ON r.issue_id = issues.issue_id
                    INNER JOIN augur_data.message m
                    ON m.msg_id = r.msg_id
                    WHERE issues.repo_id = :repo_id
                    AND issues.created_at BETWEEN :begin_date AND :end_date
                GROUP BY issues.issue_id
            ) a
            GROUP BY issue_creation_date
            ORDER BY issue_creation_date
        """)
        results = pd.read_sql(issuesFirstReponseSQL, self.database, params={'repo_id': repo_id, 'period': period,
                                                                        'begin_date': begin_date, 'end_date': end_date})                                                      
    else:
        issuesFirstReponseSQL = s.sql.text("""
            SELECT  date_trunc(:period, created_at::DATE) AS issue_creation_date, 
                    AVG(dif) AS response_time
                FROM(
                    SELECT  issues.issue_id AS issue,
                            MIN(msg_timestamp - created_at) AS dif,
                            repo_id,
                            created_at
                    FROM augur_data.issues
                    INNER JOIN augur_data.issue_message_ref r
                    ON r.issue_id = issues.issue_id
                    INNER JOIN augur_data.message m
                    ON m.msg_id = r.msg_id
                    WHERE repo_id IN (SELECT repo_id FROM repo WHERE repo_group_id=:repo_group_id)
                    AND issues.created_at BETWEEN :begin_date AND :end_date
                    GROUP BY issues.issue_id
                ) a
                GROUP BY issue_creation_date
                ORDER BY issue_creation_date
        """)
        results = pd.read_sql(issuesFirstReponseSQL, self.database, params={'repo_group_id': repo_group_id, 'period': period,
                                                                        'begin_date': begin_date, 'end_date': end_date})
    return results
