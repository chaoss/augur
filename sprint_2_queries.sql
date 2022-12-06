-- repo_id field will match repo id passed in from other metric 
SELECT COUNT(*) 
FILTER (WHERE pr_src_author_association = 'MEMBER'
	   AND repo_id = '26285') as maintainer_count
FROM augur_data.pull_requests


-- Organization or volunteer - driven returns the number of commits by users affiliated with an organization vs. users with no organizational affiliation.

SELECT 'Organizations' as null_state, COUNT(*)
FROM augur_data.pull_requests
inner join augur_data.contributors on pull_requests.pr_augur_contributor_id = contributors.cntrb_id
WHERE repo_id = '26285'
    AND cntrb_company is not null
union
SELECT 'Volunteers' as null_state, COUNT(*)
FROM augur_data.pull_requests
inner join augur_data.contributors on pull_requests.pr_augur_contributor_id = contributors.cntrb_id
WHERE repo_id = '26285'
    AND cntrb_company is null;
		   
		   
-- Organizational influence - returns the percent of pull requests that were made by each company during the period

SELECT
    lower(trim(LEADING '@' from trim(BOTH from cntrb_company))) as cntrb_company,
    COUNT(*)::float / (
        SELECT count(pr_created_at) AS total_contributions
        FROM augur_data.pull_requests
        WHERE repo_id = '26285'
        and pr_created_at between '2001/01/01' and '2022/12/31'
       ) AS percent_cntrb
FROM augur_data.contributors
    INNER JOIN (
        SELECT pr_augur_contributor_id, pr_merged_at
        FROM augur_data.pull_requests
        WHERE repo_id = 26285
            and pr_created_at between '2001/01/01' and '2022/12/31'
    ) AS pr_cntrb_id
    ON contributors.cntrb_id=pr_cntrb_id.pr_augur_contributor_id
    WHERE contributors.cntrb_company is not null
GROUP BY lower(trim(LEADING '@' from trim(BOTH from cntrb_company)));

		   
-- Peripheral organizations - returns the number of pull requests, date of first pull request, and date of latest pull request associated with each company

select lower(trim(LEADING '@' from trim(BOTH from cntrb_company))) as organization_name, count(pr_merged_at) as number_of_contributions,
min(pr_merged_at) as first_contribution, max(pr_merged_at) as last_contribution
from augur_data.pull_requests
inner join augur_data.contributors on pull_requests.pr_augur_contributor_id = contributors.cntrb_id
where cntrb_company is not null and pr_merged_at is not null
and repo_id = '26285'
group by lower(trim(LEADING '@' from trim(BOTH from cntrb_company)));

-- Organizations contributing – returns average PR’s per day while an organization was contributing, in the 60 days before they started, and in the 60 days after they stopped contributing.

CREATE TEMP TABLE tt2 (
    cntrb_per_day_before float,
    cntrb_per_day_during float,
    cntrb_per_day_after float
);

-- Find the start, end, and length (in days) of the company’s contribution, and store in temp table tt
SELECT
    min(pr_created_at) as first_contribution, max(pr_created_at) as last_contribution,
    (EXTRACT(epoch from (max(pr_created_at) - min(pr_created_at))) / 86400)::int as cntrb_len
    into temp table tt
FROM augur_data.pull_requests
    inner join augur_data.contributors on pull_requests.pr_augur_contributor_id = contributors.cntrb_id
WHERE
    lower(trim(LEADING '@' from trim(BOTH from cntrb_company))) = lower(trim(LEADING '@' from trim(BOTH from 'bitnami')))
    and repo_id = '26285';

-- find average # of PR's made per day while the company was contributing
INSERT INTO tt2 (cntrb_per_day_during)
SELECT count(*)::float / (select cntrb_len from tt)
FROM augur_data.pull_requests
WHERE pr_created_at between (select first_contribution from tt) and (select last_contribution from tt)
and repo_id = '26285';

-- find average # of PR's made per day in the 60 days before the company started contributing
UPDATE tt2 SET cntrb_per_day_before =(
SELECT count(*)::float / 60
FROM augur_data.pull_requests
WHERE pr_created_at BETWEEN (select (first_contribution - make_interval(days => 60)) from tt) and (select first_contribution from tt)
and repo_id = '26285');

-- find average # of PR's made per day in the 60 days after the company stopped contributing
UPDATE tt2 SET cntrb_per_day_after = (
SELECT count(*)::float / 60
FROM augur_data.pull_requests
WHERE pr_created_at BETWEEN (select (last_contribution) from tt) and (select (last_contribution + make_interval(days=>60)) from tt)
and repo_id = '26285');

SELECT * from tt2;

