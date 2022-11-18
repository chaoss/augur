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
		   
		   
-- repo_id field will match repo id passed in from other metric 		   
-- returns the name and number of pull requests associated with each company that has contributed to this repo
select cntrb_company as organization_name, count(pr_merged_at) as number_of_contributions
from augur_data.pull_requests
inner join augur_data.contributors on pull_requests.pr_augur_contributor_id = contributors.cntrb_id
where cntrb_company is not null and pr_merged_at is not null and repo_id = '26285'
group by cntrb_company;

