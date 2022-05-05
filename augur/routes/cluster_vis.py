import datetime
import sqlalchemy as s
import pandas as pd
from augur.util import register_metric

def clusters(self, repo_group_id, repo_id=None, period='day', begin_date=None, end_date=None):
	if not begin_date:
		begin_date = '1970-1-1 00:00:01'
	if not end_date:
		end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	if repo_id:
	    clustersSQL = s.sql.text("""
	    	SELECT
			    repo.repo_name,
			    repo.repo_git,
			    repo.repo_id,
			    A.cluster_content,
			    d.message_count,
			    e.issue_event_count,
			    f.pull_request_event_count,
			    MAX ( msg_cluster_id ) AS msg_cluster_id 
			FROM
			    repo
			    LEFT OUTER JOIN (
			    SELECT
			        repo.repo_id,
			        repo_cluster_messages.cluster_content,
			        repo_cluster_messages.msg_cluster_id,
			        repo.repo_name 
			    FROM
			        ( SELECT MAX ( msg_cluster_id ) AS msg_cluster_id, repo_id, MAX ( data_collection_date ) AS data_collection_date FROM repo_cluster_messages GROUP BY repo_id )
			        C LEFT OUTER JOIN repo ON repo.repo_id = C.repo_id
			        LEFT OUTER JOIN repo_cluster_messages ON C.msg_cluster_id = repo_cluster_messages.msg_cluster_id 
			    ) A ON repo.repo_id = A.repo_id 
			    AND A.msg_cluster_id = msg_cluster_id
			    LEFT OUTER JOIN ( SELECT repo_id, COUNT ( * ) AS message_count FROM message WHERE repo_id IS NOT NULL GROUP BY repo_id ) d ON repo.repo_id = d.repo_id
			    LEFT OUTER JOIN ( SELECT repo_id, COUNT ( * ) AS issue_event_count FROM issue_events GROUP BY repo_id ) e ON repo.repo_id = e.repo_id
			    LEFT OUTER JOIN ( SELECT repo_id, COUNT ( * ) AS pull_request_event_count FROM pull_request_events GROUP BY repo_id ) f ON repo.repo_id = f.repo_id 
			GROUP BY
			    repo.repo_name,
			    repo.repo_git,
			    A.cluster_content,
			    repo.repo_id,
			    d.message_count,
			    e.issue_event_count,
			    f.pull_request_event_count;
	    	""")

	    results = pd.read_sql(clustersSQL, self.database, params={'repo_id': repo_id, 'period': period,
	                                                            'begin_date': begin_date, 'end_date': end_date})
	else: ## This is if the repo_id is not specified
	    clustersSQL = s.sql.text("""
	    	SELECT
			    repo.repo_name,
			    repo.repo_git,
			    repo.repo_id,
			    A.cluster_content,
			    d.message_count,
			    e.issue_event_count,
			    f.pull_request_event_count,
			    MAX ( msg_cluster_id ) AS msg_cluster_id 
			FROM
			    repo
			    LEFT OUTER JOIN (
			    SELECT
			        repo.repo_id,
			        repo_cluster_messages.cluster_content,
			        repo_cluster_messages.msg_cluster_id,
			        repo.repo_name 
			    FROM
			        ( SELECT MAX ( msg_cluster_id ) AS msg_cluster_id, repo_id, MAX ( data_collection_date ) AS data_collection_date FROM repo_cluster_messages GROUP BY repo_id )
			        C LEFT OUTER JOIN repo ON repo.repo_id = C.repo_id
			        LEFT OUTER JOIN repo_cluster_messages ON C.msg_cluster_id = repo_cluster_messages.msg_cluster_id 
			    ) A ON repo.repo_id = A.repo_id 
			    AND A.msg_cluster_id = msg_cluster_id
			    LEFT OUTER JOIN ( SELECT repo_id, COUNT ( * ) AS message_count FROM message WHERE repo_id IS NOT NULL GROUP BY repo_id ) d ON repo.repo_id = d.repo_id
			    LEFT OUTER JOIN ( SELECT repo_id, COUNT ( * ) AS issue_event_count FROM issue_events GROUP BY repo_id ) e ON repo.repo_id = e.repo_id
			    LEFT OUTER JOIN ( SELECT repo_id, COUNT ( * ) AS pull_request_event_count FROM pull_request_events GROUP BY repo_id ) f ON repo.repo_id = f.repo_id 
			GROUP BY
			    repo.repo_name,
			    repo.repo_git,
			    A.cluster_content,
			    repo.repo_id,
			    d.message_count,
			    e.issue_event_count,
			    f.pull_request_event_count;
	       
	    """)

	    results = pd.read_sql(clustersSQL, self.database, params={'repo_group_id': repo_group_id, 'period': period,
	                                                            'begin_date': begin_date, 'end_date': end_date})
	print("hello")
	print(type(results))
	return results





