BEGIN;
	INSERT INTO "augur_data"."platform" ("pltfrm_id", "pltfrm_name", "pltfrm_version", "pltfrm_release_date", "tool_source", "tool_version", "data_source", "data_collection_date") VALUES (25152, 'Gerrit', '3', '2021-06-05', 'Manual Entry', 'Sean Goggins', 'GitHub', '2021-06-05 17:23:42');

COMMIT; 

INSERT INTO "augur_operations"."worker_history" ("history_id", "repo_id", "worker", "job_model", "oauth_id", "timestamp", "status", "total_results") VALUES (1, 1, 'workers.insight_worker.49025', 'insights', NULL, '2021-07-14 15:16:16', 'Success', 0);
INSERT INTO "augur_operations"."worker_history" ("history_id", "repo_id", "worker", "job_model", "oauth_id", "timestamp", "status", "total_results") VALUES (2, 1, 'workers.linux_badge_worker.47216', 'badges', NULL, '2021-07-14 15:16:19', 'Success', 1);

update "augur_operations"."augur_settings" set value = 61 where setting = 'augur_data_version';

