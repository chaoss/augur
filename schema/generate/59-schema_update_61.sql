BEGIN;
	INSERT INTO "augur_data"."platform" ("pltfrm_id", "pltfrm_name", "pltfrm_version", "pltfrm_release_date", "tool_source", "tool_version", "data_source", "data_collection_date") VALUES (25152, 'Gerrit', '3', '2021-06-05', 'Manual Entry', 'Sean Goggins', 'GitHub', '2021-06-05 17:23:42');

COMMIT; 

update "augur_operations"."augur_settings" set value = 61 where setting = 'augur_data_version';

