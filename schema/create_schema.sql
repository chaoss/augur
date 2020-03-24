-- Generate core schema
\i schema/generate/01-schema.sql
\i schema/generate/02-augur_data.sql
\i schema/generate/03-augur_operations.sql
\i schema/generate/04-spdx.sql
\i schema/generate/05-seed_data.sql

-- Update scripts
\i schema/generate/06-schema_update_8.sql
\i schema/generate/07-schema_update_9.sql
\i schema/generate/08-schema_update_10.sql
\i schema/generate/09-schema_update_11.sql
\i schema/generate/10-schema_update_12.sql