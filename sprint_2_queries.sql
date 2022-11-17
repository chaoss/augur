-- repo_id field will match repo id passed in from other metric 
SELECT COUNT(*) 
FILTER (WHERE pr_src_author_association = 'MEMBER'
	   AND repo_id = '26285') as maintainer_count
FROM augur_data.pull_requests
