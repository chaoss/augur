-- SPDX-License-Identifier: MIT
/*
"Hello World" for DBT Analytical Transformation Workflows
This model calculates the total number of commits and issues for each repository
*/
{{ config(materialized='table') }}

WITH commits AS (
    SELECT repo_id, COUNT(*) AS total_commits 
    FROM augur_data.commits 
    GROUP BY repo_id
),
issues AS (
    SELECT repo_id, COUNT(*) AS total_issues 
    FROM augur_data.issues 
    GROUP BY repo_id
)

SELECT 
    c.repo_id, 
    c.total_commits, 
    COALESCE(i.total_issues, 0) AS total_issues
FROM commits c
LEFT JOIN issues i 
    ON c.repo_id = i.repo_id
