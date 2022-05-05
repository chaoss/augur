import datetime
import sqlalchemy as s
import pandas as pd
from augur.util import register_metric
import matplotlib.pyplot as plt
import json

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
	# print("hello")
	print(type(results))
	return results


# jsonData = {"RECORDS": [
#     {
#       "repo_name": "grimoirelab-sortinghat",
#       "repo_git": "https://github.com/chaoss/grimoirelab-sortinghat",
#       "repo_id": 25430,
#       "cluster_content": 0,
#       "message_count": 1600,
#       "issue_event_count": 3487,
#       "pull_request_event_count": 2220,
#       "msg_cluster_id": 1524
#     },
#     {
#       "repo_name": "grimoirelab-kibiter",
#       "repo_git": "https://github.com/chaoss/grimoirelab-kibiter",
#       "repo_id": 25433,
#       "cluster_content": 0,
#       "message_count": 143,
#       "issue_event_count": 666,
#       "pull_request_event_count": 558,
#       "msg_cluster_id": 1527
#     },
#     {
#       "repo_name": "grimoirelab-cereslib",
#       "repo_git": "https://github.com/chaoss/grimoirelab-cereslib",
#       "repo_id": 25435,
#       "cluster_content": 0,
#       "message_count": 43,
#       "issue_event_count": 193,
#       "pull_request_event_count": 157,
#       "msg_cluster_id": 1529
#     },
#     {
#       "repo_name": "grimoirelab-sigils",
#       "repo_git": "https://github.com/chaoss/grimoirelab-sigils",
#       "repo_id": 25436,
#       "cluster_content": 0,
#       "message_count": 724,
#       "issue_event_count": 2452,
#       "pull_request_event_count": 1974,
#       "msg_cluster_id": 1530
#     },
#     {
#       "repo_name": "grimoirelab-tutorial",
#       "repo_git": "https://github.com/chaoss/grimoirelab-tutorial",
#       "repo_id": 25438,
#       "cluster_content": 0,
#       "message_count": 520,
#       "issue_event_count": 1232,
#       "pull_request_event_count": 825,
#       "msg_cluster_id": 1532
#     },
#     {
#       "repo_name": "grimoirelab-bestiary",
#       "repo_git": "https://github.com/chaoss/grimoirelab-bestiary",
#       "repo_id": 25443,
#       "cluster_content": 0,
#       "message_count": 304,
#       "issue_event_count": 546,
#       "pull_request_event_count": 448,
#       "msg_cluster_id": 1537
#     },
#     {
#       "repo_name": "grimoirelab",
#       "repo_git": "https://github.com/chaoss/grimoirelab",
#       "repo_id": 25448,
#       "cluster_content": 0,
#       "message_count": 2437,
#       "issue_event_count": 4910,
#       "pull_request_event_count": 1072,
#       "msg_cluster_id": 1505
#     },
#     {
#       "repo_name": "grimoirelab-hatstall",
#       "repo_git": "https://github.com/chaoss/grimoirelab-hatstall",
#       "repo_id": 25450,
#       "cluster_content": 0,
#       "message_count": 154,
#       "issue_event_count": 594,
#       "pull_request_event_count": 448,
#       "msg_cluster_id": 1507
#     },
#     {
#       "repo_name": "grimoirelab-kidash",
#       "repo_git": "https://github.com/chaoss/grimoirelab-kidash",
#       "repo_id": 25454,
#       "cluster_content": 0,
#       "message_count": 100,
#       "issue_event_count": 263,
#       "pull_request_event_count": 154,
#       "msg_cluster_id": 1510
#     },
#     {
#       "repo_name": "grimoirelab-graal",
#       "repo_git": "https://github.com/chaoss/grimoirelab-graal",
#       "repo_id": 25456,
#       "cluster_content": 0,
#       "message_count": 380,
#       "issue_event_count": 1013,
#       "pull_request_event_count": 655,
#       "msg_cluster_id": 1512
#     },
#     {
#       "repo_name": "prospector",
#       "repo_git": "https://github.com/chaoss/prospector",
#       "repo_id": 25446,
#       "cluster_content": 1,
#       "message_count": 11,
#       "issue_event_count": 14,
#       "pull_request_event_count": 6,
#       "msg_cluster_id": 1503
#     },
#     {
#       "repo_name": "metrics",
#       "repo_git": "https://github.com/chaoss/metrics",
#       "repo_id": 25447,
#       "cluster_content": 1,
#       "message_count": 642,
#       "issue_event_count": null,
#       "pull_request_event_count": null,
#       "msg_cluster_id": 1504
#     },
#     {
#       "repo_name": "governance",
#       "repo_git": "https://github.com/chaoss/governance",
#       "repo_id": 25449,
#       "cluster_content": 1,
#       "message_count": 897,
#       "issue_event_count": 2135,
#       "pull_request_event_count": 1397,
#       "msg_cluster_id": 1506
#     },
#     {
#       "repo_name": "wg-diversity-inclusion",
#       "repo_git": "https://github.com/chaoss/wg-diversity-inclusion",
#       "repo_id": 25451,
#       "cluster_content": 1,
#       "message_count": 1098,
#       "issue_event_count": 2549,
#       "pull_request_event_count": 273,
#       "msg_cluster_id": 1508
#     },
#     {
#       "repo_name": "website",
#       "repo_git": "https://github.com/chaoss/website",
#       "repo_id": 25453,
#       "cluster_content": 1,
#       "message_count": 1660,
#       "issue_event_count": 4134,
#       "pull_request_event_count": 2377,
#       "msg_cluster_id": 1509
#     },
#     {
#       "repo_name": "wg-evolution",
#       "repo_git": "https://github.com/chaoss/wg-evolution",
#       "repo_id": 25455,
#       "cluster_content": 1,
#       "message_count": 1691,
#       "issue_event_count": 3375,
#       "pull_request_event_count": 2025,
#       "msg_cluster_id": 1511
#     },
#     {
#       "repo_name": "wg-value",
#       "repo_git": "https://github.com/chaoss/wg-value",
#       "repo_id": 25457,
#       "cluster_content": 1,
#       "message_count": 492,
#       "issue_event_count": 999,
#       "pull_request_event_count": 545,
#       "msg_cluster_id": 1513
#     },
#     {
#       "repo_name": "wg-risk",
#       "repo_git": "https://github.com/chaoss/wg-risk",
#       "repo_id": 25458,
#       "cluster_content": 1,
#       "message_count": 310,
#       "issue_event_count": 735,
#       "pull_request_event_count": 371,
#       "msg_cluster_id": 1514
#     },
#     {
#       "repo_name": "wg-common",
#       "repo_git": "https://github.com/chaoss/wg-common",
#       "repo_id": 25459,
#       "cluster_content": 1,
#       "message_count": 363,
#       "issue_event_count": 813,
#       "pull_request_event_count": 395,
#       "msg_cluster_id": 1515
#     },
#     {
#       "repo_name": "wg-app-ecosystem",
#       "repo_git": "https://github.com/chaoss/wg-app-ecosystem",
#       "repo_id": 25461,
#       "cluster_content": 1,
#       "message_count": 11,
#       "issue_event_count": 59,
#       "pull_request_event_count": 54,
#       "msg_cluster_id": 1517
#     },
#     {
#       "repo_name": "community-reports",
#       "repo_git": "https://github.com/chaoss/community-reports",
#       "repo_id": 25558,
#       "cluster_content": 1,
#       "message_count": 12,
#       "issue_event_count": 37,
#       "pull_request_event_count": 25,
#       "msg_cluster_id": 1518
#     },
#     {
#       "repo_name": "express",
#       "repo_git": "https://github.com/expressjs/express.git",
#       "repo_id": 25205,
#       "cluster_content": 2,
#       "message_count": 21836,
#       "issue_event_count": 68,
#       "pull_request_event_count": null,
#       "msg_cluster_id": 1520
#     },
#     {
#       "repo_name": "jquery",
#       "repo_git": "https://github.com/jquery/jquery.git",
#       "repo_id": 25206,
#       "cluster_content": 2,
#       "message_count": 26247,
#       "issue_event_count": null,
#       "pull_request_event_count": null,
#       "msg_cluster_id": 1521
#     },
#     {
#       "repo_name": "body-parser",
#       "repo_git": "https://github.com/expressjs/body-parser.git",
#       "repo_id": 25207,
#       "cluster_content": 2,
#       "message_count": 2291,
#       "issue_event_count": 2795,
#       "pull_request_event_count": 90,
#       "msg_cluster_id": 1522
#     },
#     {
#       "repo_name": "react",
#       "repo_git": "https://github.com/facebook/react.git",
#       "repo_id": 25208,
#       "cluster_content": 2,
#       "message_count": 65291,
#       "issue_event_count": null,
#       "pull_request_event_count": null,
#       "msg_cluster_id": 1523
#     },
#     {
#       "repo_name": "grimoirelab-elk",
#       "repo_git": "https://github.com/chaoss/grimoirelab-elk",
#       "repo_id": 25431,
#       "cluster_content": 3,
#       "message_count": 2738,
#       "issue_event_count": 6040,
#       "pull_request_event_count": 4793,
#       "msg_cluster_id": 1525
#     },
#     {
#       "repo_name": "grimoirelab-perceval",
#       "repo_git": "https://github.com/chaoss/grimoirelab-perceval",
#       "repo_id": 25432,
#       "cluster_content": 3,
#       "message_count": 4233,
#       "issue_event_count": 5692,
#       "pull_request_event_count": 3736,
#       "msg_cluster_id": 1526
#     },
#     {
#       "repo_name": "grimoirelab-kingarthur",
#       "repo_git": "https://github.com/chaoss/grimoirelab-kingarthur",
#       "repo_id": 25434,
#       "cluster_content": 3,
#       "message_count": 274,
#       "issue_event_count": 577,
#       "pull_request_event_count": 399,
#       "msg_cluster_id": 1528
#     },
#     {
#       "repo_name": "grimoirelab-sirmordred",
#       "repo_git": "https://github.com/chaoss/grimoirelab-sirmordred",
#       "repo_id": 25437,
#       "cluster_content": 3,
#       "message_count": 1360,
#       "issue_event_count": null,
#       "pull_request_event_count": 2223,
#       "msg_cluster_id": 1531
#     },
#     {
#       "repo_name": "grimoirelab-perceval-mozilla",
#       "repo_git": "https://github.com/chaoss/grimoirelab-perceval-mozilla",
#       "repo_id": 25439,
#       "cluster_content": 3,
#       "message_count": 157,
#       "issue_event_count": 310,
#       "pull_request_event_count": 230,
#       "msg_cluster_id": 1533
#     },
#     {
#       "repo_name": "grimoirelab-perceval-puppet",
#       "repo_git": "https://github.com/chaoss/grimoirelab-perceval-puppet",
#       "repo_id": 25441,
#       "cluster_content": 3,
#       "message_count": 53,
#       "issue_event_count": 159,
#       "pull_request_event_count": 142,
#       "msg_cluster_id": 1535
#     },
#     {
#       "repo_name": "grimoirelab-manuscripts",
#       "repo_git": "https://github.com/chaoss/grimoirelab-manuscripts",
#       "repo_id": 25442,
#       "cluster_content": 3,
#       "message_count": 538,
#       "issue_event_count": 1120,
#       "pull_request_event_count": 756,
#       "msg_cluster_id": 1536
#     },
#     {
#       "repo_name": "grimoirelab-toolkit",
#       "repo_git": "https://github.com/chaoss/grimoirelab-toolkit",
#       "repo_id": 25444,
#       "cluster_content": 3,
#       "message_count": 140,
#       "issue_event_count": 271,
#       "pull_request_event_count": 187,
#       "msg_cluster_id": 1538
#     },
#     {
#       "repo_name": "grimoirelab-perceval-opnfv",
#       "repo_git": "https://github.com/chaoss/grimoirelab-perceval-opnfv",
#       "repo_id": 25445,
#       "cluster_content": 3,
#       "message_count": 58,
#       "issue_event_count": 169,
#       "pull_request_event_count": 147,
#       "msg_cluster_id": 1539
#     },
#     {
#       "repo_name": "lodash",
#       "repo_git": "https://github.com/lodash/lodash.git",
#       "repo_id": 25204,
#       "cluster_content": 4,
#       "message_count": 19157,
#       "issue_event_count": null,
#       "pull_request_event_count": null,
#       "msg_cluster_id": 1519
#     },
#     {
#       "repo_name": "augur",
#       "repo_git": "https://github.com/chaoss/augur",
#       "repo_id": 25440,
#       "cluster_content": 5,
#       "message_count": 2680,
#       "issue_event_count": 12780,
#       "pull_request_event_count": 1300,
#       "msg_cluster_id": 1534
#     },
#     {
#       "repo_name": "augur-license",
#       "repo_git": "https://github.com/chaoss/augur-license",
#       "repo_id": 25460,
#       "cluster_content": 5,
#       "message_count": 6,
#       "issue_event_count": 61,
#       "pull_request_event_count": 53,
#       "msg_cluster_id": 1516
#     },
#     {
#       "repo_name": "whitepaper",
#       "repo_git": "https://github.com/chaoss/whitepaper",
#       "repo_id": 25452,
#       "cluster_content": null,
#       "message_count": null,
#       "issue_event_count": null,
#       "pull_request_event_count": null,
#       "msg_cluster_id": null
#     }
#   ]}

# df = pd.DataFrame(jsonData['RECORDS'])
# print (df)
# df.plot(x='cluster_content', y='message_count')



