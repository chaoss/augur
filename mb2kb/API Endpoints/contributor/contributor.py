"""
Metrics that provides data about contributors & their associated activity
"""

import datetime
import sqlalchemy as s
import pandas as pd
from augur.util import logger, annotate, add_metrics

@annotate(tag='contributors-organizations')
def contributors_organizations(self, repo_group_id, repo_id=None, period='month', begin_date=None, end_date=None):
    """
    Returns a list of organizations whose members have contributed to a project and their summed contributions
    This is a timeseries where there is a dataframe for each contributing organization for each period (Default: month)
    DataFrame has these columns:
    commits
    issues
    issue_comments
    total
    organization
    contrib_date
    """
    if not begin_date:
        begin_date = '1970-1-1 00:00:01'
    if not end_date:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if not repo_id:
        contributors_organizationsSQL = s.sql.text("""
            SELECT  SUM(issues)		    AS issues,
					SUM(commits)	    AS commits,
                    SUM(issue_comments) AS issue_comments,
                    SUM(a.issues + a.commits + a.issue_comments)   AS total,
                    organization,
                    date_trunc(:period, timestamp::DATE) as contrib_date
                FROM (
                    (SELECT reporter_id AS id,
                            repo_id,
                            COUNT(*)   AS issues,
					 		0		   AS commits,
                            0          AS issue_comments,
					 		TRIM('@' from cntrb_company) AS organization,
                            created_at AS timestamp
                    FROM augur_data.issues
					INNER JOIN augur_data.contributors c
					ON c.cntrb_id = issues.reporter_id
                    WHERE repo_id in (SELECT repo_id FROM augur_data.repo WHERE repo_group_id=:repo_group_id)
                        AND reporter_id IS NOT NULL
                        AND pull_request IS NULL
                        AND created_at BETWEEN :begin_date AND :end_date
                    GROUP BY id, repo_id, organization, timestamp)
                    UNION ALL
                    (SELECT cntrb_id	AS id,
                            repo_id,
                            0           AS issues,
                            COUNT(*)    AS commits,
                            0           AS issue_comments,
                            TRIM('@' from cntrb_company) AS organization,
                            cmt_author_timestamp AS timestamp
                    FROM augur_data.commits
                    INNER JOIN augur_data.contributors c
                    ON c.cntrb_email = commits.cmt_author_raw_email
                    WHERE repo_id in (SELECT repo_id FROM augur_data.repo WHERE repo_group_id=:repo_group_id)
                        AND cmt_author_raw_email IS NOT NULL
                        AND cmt_committer_date BETWEEN :begin_date AND :end_date
                    GROUP BY id, repo_id, organization, timestamp)
                    UNION ALL
					(SELECT reporter_id	AS id,
					 		repo_id,
					 		0			AS issues,
					 		0			AS commits,
					 		count(*)	AS issue_comments,
					 		TRIM('@' from cntrb_company) as organization,
                            msg_timestamp AS timestamp
					 FROM augur_data.issue_message_ref
					 INNER JOIN augur_data.issues i
					 ON i.issue_id = issue_message_ref.issue_id
					 INNER JOIN augur_data.contributors c
					 ON c.cntrb_id = i.reporter_id
                     INNER JOIN augur_data.message m
                     on m.msg_id = issue_message_ref.msg_id
					 WHERE repo_id in (SELECT repo_id FROM augur_data.repo WHERE repo_group_id=:repo_group_id)
                        AND reporter_id IS NOT NULL
                        AND created_at BETWEEN :begin_date AND :end_date
					 GROUP BY id, repo_id, organization, timestamp)
                ) a, augur_data.repo
                WHERE a.repo_id = repo.repo_id
                GROUP BY organization, contrib_date
                ORDER BY contrib_date
        """)
    results = pd.read_sql(contributors_organizationsSQL, self.database, params={'repo_group_id': repo_group_id, 'period': period, 
                                                                                'begin_date': begin_date, 'end_date': end_date})
    return results