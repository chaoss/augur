-- repo_id field will match repo id passed in from other metric 
SELECT COUNT(*) 
FILTER (WHERE pr_src_author_association = 'MEMBER'
	   AND repo_id = '26285') as maintainer_count
FROM augur_data.pull_requests


-- repo_id field will match repo id passed in from other metric
-- returns count of contributions made by a user with a company affiliation
SELECT COUNT(cntrb_company) AS organization_cntrb
FROM augur_data.contributors
INNER JOIN (SELECT pr_augur_contributor_id
		   FROM augur_data.pull_requests 
		   WHERE repo_id = 26285) AS pr_cntrb_id
		   ON contributors.cntrb_id=pr_cntrb_id.pr_augur_contributor_id
		   
		   
