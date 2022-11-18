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
		   
		   
		   
-- Queries for organizational influence
-- repo_id will be passed in from other metric
-- The start date and end date will also be passed in by the user

-- returns the number of pull requests made by all contributors during the period
select count(pr_merged_at) as total_contributions
from augur_data.pull_requests
where pr_merged_at is not null
and repo_id = '26285'
and pr_merged_at between '2021/01/01' and '2021/12/31';

-- returns the number of pull requests made by each company during the period; we need to divide this by total_contributions
select cntrb_company as organization_name, count(pr_merged_at) as org_contributions
from augur_data.pull_requests
inner join augur_data.contributors on pull_requests.pr_augur_contributor_id = contributors.cntrb_id
where cntrb_company is not null and pr_merged_at is not null and repo_id = '26285'
and pr_merged_at between '2021/01/01' and '2021/12/31'
group by cntrb_company;
		   
	
	
-- repo_id field will match repo id passed in from other metric 		   
-- returns the number of pull requests, date of first pull request, and date of latest pull request associated with each company
select contributors.cntrb_company as organization_name, count(pr_merged_at) as number_of_contributions, 
min(pr_merged_at) as first_contribution, max(pr_merged_at) as last_contribution
from augur_data.pull_requests
inner join augur_data.contributors on pull_requests.pr_augur_contributor_id = contributors.cntrb_id
where cntrb_company is not null and pr_merged_at is not null
and repo_id = '26285'
group by cntrb_company;
