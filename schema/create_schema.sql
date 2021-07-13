-- #SPDX-License-Identifier: MIT
-- Generate core schema
\i schema/generate/01-schema.sql
--\i schema/generate/02-augur_data.sql
\i schema/generate/02-augur_data_v2.sql
--\i schema/generate/03-augur_operations.sql
\i schema/generate/03-augur_operations_v2.sql
\i schema/generate/04-spdx.sql
\i schema/generate/05-seed_data.sql

-- Update scripts
-- Starting with Augur Version 0.20.0 the update scripts start at 59-schema_update_61.sql


