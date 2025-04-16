truncate table augur_data.dm_repo_annual;
truncate table augur_data.dm_repo_weekly;
truncate table augur_data.dm_repo_monthly;
truncate table augur_data.dm_repo_group_annual;
truncate table augur_data.dm_repo_group_weekly;
truncate table augur_data.dm_repo_group_monthly;

INSERT INTO augur_data.dm_repo_group_weekly ( repo_group_id, email, affiliation, week, YEAR, added, removed, WHITESPACE, files, patches, tool_source, tool_version, data_source ) SELECT
r.repo_group_id AS repo_group_id,
A.cmt_author_email AS email,
A.cmt_author_affiliation AS affiliation,
date_part( 'week', TO_TIMESTAMP( A.cmt_committer_date, 'YYYY-MM-DD' ) ) AS week,
date_part( 'year', TO_TIMESTAMP( A.cmt_committer_date, 'YYYY-MM-DD' ) ) AS YEAR,
SUM ( A.cmt_added ) AS added,
SUM ( A.cmt_removed ) AS removed,
SUM ( A.cmt_whitespace ) AS WHITESPACE,
COUNT ( DISTINCT A.cmt_filename ) AS files,
COUNT ( DISTINCT A.cmt_commit_hash ) AS patches,
info.A AS tool_source,
info.b AS tool_version,
info.C AS data_source 
FROM
	( SELECT 'manual query' AS A, '1.0' AS b, 'query' AS C ) AS info,--(SELECT 'manual query' AS a, '1.0' AS b, 'query' AS c) AS info,
--FROM VALUES(('manual query', '1.0', 'query') info(a,b,c)),
	augur_data.commits
	A JOIN augur_data.repo r ON r.repo_id = A.repo_id
	JOIN augur_data.repo_groups P ON P.repo_group_id = r.repo_group_id
	LEFT JOIN augur_data.EXCLUDE e ON ( A.cmt_author_email = e.email AND ( e.projects_id = r.repo_group_id OR e.projects_id = 0 ) ) 
	OR ( A.cmt_author_email LIKE CONCAT ( '%%', e.DOMAIN ) AND ( e.projects_id = r.repo_group_id OR e.projects_id = 0 ) ) 
WHERE
	e.email IS NULL 
	AND e.DOMAIN IS NULL --         AND p.rg_recache = 1
GROUP BY
	week,
	YEAR,
	affiliation,
	A.cmt_author_email,
	r.repo_group_id,
	info.A,
	info.b,
	info.C --.bindparams(tool_source='manual creation',tool_version='1.0',data_source='manual creation');
	;
INSERT INTO augur_data.dm_repo_group_monthly ( repo_group_id, email, affiliation, MONTH, YEAR, added, removed, WHITESPACE, files, patches, tool_source, tool_version, data_source ) SELECT
r.repo_group_id AS repo_group_id,
A.cmt_author_email AS email,
A.cmt_author_affiliation AS affiliation,--date_part('week', TO_TIMESTAMP(a.cmt_committer_date, 'YYYY-MM-DD')) AS week,
date_part( 'month', TO_TIMESTAMP( A.cmt_committer_date, 'YYYY-MM-DD' ) ) AS MONTH,
date_part( 'year', TO_TIMESTAMP( A.cmt_committer_date, 'YYYY-MM-DD' ) ) AS YEAR,
SUM ( A.cmt_added ) AS added,
SUM ( A.cmt_removed ) AS removed,
SUM ( A.cmt_whitespace ) AS WHITESPACE,
COUNT ( DISTINCT A.cmt_filename ) AS files,
COUNT ( DISTINCT A.cmt_commit_hash ) AS patches,
info.A AS tool_source,
info.b AS tool_version,
info.C AS data_source 
FROM
	( SELECT 'manual query' AS A, '1.0' AS b, 'query' AS C ) AS info,
	augur_data.commits
	A JOIN augur_data.repo r ON r.repo_id = A.repo_id
	JOIN augur_data.repo_groups P ON P.repo_group_id = r.repo_group_id
	LEFT JOIN augur_data.EXCLUDE e ON ( A.cmt_author_email = e.email AND ( e.projects_id = r.repo_group_id OR e.projects_id = 0 ) ) 
	OR ( A.cmt_author_email LIKE CONCAT ( '%%', e.DOMAIN ) AND ( e.projects_id = r.repo_group_id OR e.projects_id = 0 ) ) 
WHERE
	e.email IS NULL 
	AND e.DOMAIN IS NULL --AND p.rg_recache = 1
GROUP BY
	MONTH,
	YEAR,
	affiliation,
	A.cmt_author_email,
	r.repo_group_id,
	info.A,
	info.b,
	info.C;
	
INSERT INTO augur_data.dm_repo_group_annual ( repo_group_id, email, affiliation, YEAR, added, removed, WHITESPACE, files, patches, tool_source, tool_version, data_source ) SELECT
r.repo_group_id AS repo_group_id,
A.cmt_author_email AS email,
A.cmt_author_affiliation AS affiliation,
date_part( 'year', TO_TIMESTAMP( A.cmt_committer_date, 'YYYY-MM-DD' ) ) AS YEAR,
SUM ( A.cmt_added ) AS added,
SUM ( A.cmt_removed ) AS removed,
SUM ( A.cmt_whitespace ) AS WHITESPACE,
COUNT ( DISTINCT A.cmt_filename ) AS files,
COUNT ( DISTINCT A.cmt_commit_hash ) AS patches,
info.A AS tool_source,
info.b AS tool_version,
info.C AS data_source 
FROM
	( SELECT 'manual query' AS A, '1.0' AS b, 'query' AS C ) AS info,
	augur_data.commits
	A JOIN augur_data.repo r ON r.repo_id = A.repo_id
	JOIN raugur_data.epo_groups P ON P.repo_group_id = r.repo_group_id
	LEFT JOIN augur_data.EXCLUDE e ON ( A.cmt_author_email = e.email AND ( e.projects_id = r.repo_group_id OR e.projects_id = 0 ) ) 
	OR ( A.cmt_author_email LIKE CONCAT ( '%%', e.DOMAIN ) AND ( e.projects_id = r.repo_group_id OR e.projects_id = 0 ) ) 
WHERE
	e.email IS NULL 
	AND e.DOMAIN IS NULL --AND p.rg_recache = 1
GROUP BY
	YEAR,
	affiliation,
	A.cmt_author_email,
	r.repo_group_id,
	info.A,
	info.b,
	info.C
	;
INSERT INTO augur_data.dm_repo_weekly ( repo_id, email, affiliation, week, year, added, removed, whitespace, files, patches, tool_source, tool_version, data_source ) SELECT a
.repo_id AS repo_id,
a.cmt_author_email AS email,
a.cmt_author_affiliation AS affiliation,
date_part( 'week', TO_TIMESTAMP( A.cmt_committer_date, 'YYYY-MM-DD' ) ) AS week,
date_part( 'year', TO_TIMESTAMP( A.cmt_committer_date, 'YYYY-MM-DD' ) ) AS YEAR,
SUM ( a.cmt_added ) AS added,
SUM ( a.cmt_removed ) AS removed,
SUM ( a.cmt_whitespace ) AS whitespace,
COUNT ( DISTINCT a.cmt_filename ) AS files,
COUNT ( DISTINCT a.cmt_commit_hash ) AS patches,
info.a AS tool_source,
info.b AS tool_version,
info.c AS data_source 
FROM
	( SELECT 'manual query' AS A, '1.0' AS b, 'query' AS C ) AS info,
--(VALUES(:tool_source,:tool_version,:data_source)) info(a,b,c),
	augur_data.commits
	a JOIN augur_data.repo r ON r.repo_id = a.repo_id
	JOIN augur_data.repo_groups p ON p.repo_group_id = r.repo_group_id
	LEFT JOIN augur_data.exclude e ON ( a.cmt_author_email = e.email AND ( e.projects_id = r.repo_group_id OR e.projects_id = 0 ) ) 
	OR ( a.cmt_author_email LIKE CONCAT ( '%%', e.domain ) AND ( e.projects_id = r.repo_group_id OR e.projects_id = 0 ) ) 
WHERE
	e.email IS NULL 
	AND e.domain IS NULL --AND p.rg_recache = 1
GROUP BY
	week,
	year,
	affiliation,
	a.cmt_author_email,
	a.repo_id,
	info.a,
	info.b,
	info.c
	;


INSERT INTO augur_data.dm_repo_monthly ( repo_id, email, affiliation, month, year, added, removed, whitespace, files, patches, tool_source, tool_version, data_source ) SELECT a
.repo_id AS repo_id,
a.cmt_author_email AS email,
a.cmt_author_affiliation AS affiliation,
date_part( 'month', TO_TIMESTAMP( A.cmt_committer_date, 'YYYY-MM-DD' ) ) AS MONTH,
date_part( 'year', TO_TIMESTAMP( A.cmt_committer_date, 'YYYY-MM-DD' ) ) AS YEAR,
SUM ( a.cmt_added ) AS added,
SUM ( a.cmt_removed ) AS removed,
SUM ( a.cmt_whitespace ) AS whitespace,
COUNT ( DISTINCT a.cmt_filename ) AS files,
COUNT ( DISTINCT a.cmt_commit_hash ) AS patches,
info.a AS tool_source,
info.b AS tool_version,
info.c AS data_source 
FROM
	( SELECT 'manual query' AS A, '1.0' AS b, 'query' AS C ) AS info,
--         FROM (VALUES(:tool_source,:tool_version,:data_source)) info(a,b,c),
	augur_data.commits
	a JOIN augur_data.repo r ON r.repo_id = a.repo_id
	JOIN augur_data.repo_groups p ON p.repo_group_id = r.repo_group_id
	LEFT JOIN augur_data.exclude e ON ( a.cmt_author_email = e.email AND ( e.projects_id = r.repo_group_id OR e.projects_id = 0 ) ) 
	OR ( a.cmt_author_email LIKE CONCAT ( '%%', e.domain ) AND ( e.projects_id = r.repo_group_id OR e.projects_id = 0 ) ) 
WHERE
	e.email IS NULL 
	AND e.domain IS NULL --AND p.rg_recache = 1
GROUP BY
	month,
	year,
	affiliation,
	a.cmt_author_email,
	a.repo_id,
	info.a,
	info.b,
	info.c
	;

INSERT INTO augur_data.dm_repo_annual ( repo_id, email, affiliation, year, added, removed, whitespace, files, patches, tool_source, tool_version, data_source ) SELECT a
.repo_id AS repo_id,
a.cmt_author_email AS email,
a.cmt_author_affiliation AS affiliation,
date_part( 'year', TO_TIMESTAMP( A.cmt_committer_date, 'YYYY-MM-DD' ) ) AS YEAR,
SUM ( a.cmt_added ) AS added,
SUM ( a.cmt_removed ) AS removed,
SUM ( a.cmt_whitespace ) AS whitespace,
COUNT ( DISTINCT a.cmt_filename ) AS files,
COUNT ( DISTINCT a.cmt_commit_hash ) AS patches,
info.a AS tool_source,
info.b AS tool_version,
info.c AS data_source 
FROM
	( SELECT 'manual query' AS A, '1.0' AS b, 'query' AS C ) AS info,
--         FROM (VALUES(:tool_source,:tool_version,:data_source)) info(a,b,c),
	augur_data.commits
	a JOIN augur_data.repo r ON r.repo_id = a.repo_id
	JOIN augur_data.repo_groups p ON p.repo_group_id = r.repo_group_id
	LEFT JOIN augur_data.exclude e ON ( a.cmt_author_email = e.email AND ( e.projects_id = r.repo_group_id OR e.projects_id = 0 ) ) 
	OR ( a.cmt_author_email LIKE CONCAT ( '%%', e.domain ) AND ( e.projects_id = r.repo_group_id OR e.projects_id = 0 ) ) 
WHERE
	e.email IS NULL 
	AND e.domain IS NULL --AND p.rg_recache = 1
GROUP BY
	year,
	affiliation,
	a.cmt_author_email,
	a.repo_id,
	info.a,
	info.b,
	info.c;
