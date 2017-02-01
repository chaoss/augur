# SQL Queries

The following queries are based on GHTorrent database.  The SQL is for all repos, but the addition
of a where clause will make any of them specific to a certain repo:



## Number of Members per Project


	select count(distinct project_members.user_id) as num_members, projects.name as project_name, url
	from project_members join projects on project_members.repo_id = projects.id
	group by repo_id




## Number of Contributors per Project:

GitHub defines contributors as those who have made "Contributions to master, excluding merge commits"

I do not see in the GHTorrent database schema a way to determine commits to master vs other branches,
Nor a way to differentiate merge commits from other commits.

Because of this, for the following SQL query I will define contributors as "users who have made a commit"

When viewing the table, one may notice that there is a separate author_id and committer_id for each commit
the commit author has written the code of the commit.
the commit committer has made the commit
example: author writes some code and does a pull request.  committer approves/merges the pull request

For the following SQL, I am considering the author to be the contributer.

	select projects.name as project_name, projects.url as url, count(distinct commits.author_id) as num_contributers
	from commits 
	join project_commits on commits.id = project_commits.commit_id
	join projects on projects.id = project_commits.project_id
	group by project_commits.project_id
	
## total number of commits per project:

	select count(commits.id) as num_commits, projects.name as project_name, projects.url as url
	from commits 
		join project_commits on commits.id = project_commits.project_id
		join projects on projects.id = project_commits.project_id
	group by projects.id          

### Activity Level of Contributors

For the purposes of this SQL, I have defined it as the median number of commits to this repo per contributer.
I decided against mean because this could lead to skewing if one committer commits 1000 and the rest commit 1

Unfortunately, there is no median calculaton in SQL.

I have found a median calculation for SQL on stackoverflow and tested it on a test table.
Here it is, column and table names modified for clarity

http://dba.stackexchange.com/questions/2519/how-do-i-find-the-median-value-of-a-column-in-mysql
answered by Jeff Humphreys

	SELECT AVG(column_name) median 
	FROM(
	  SELECT x.column_name, SUM(SIGN(1.0-SIGN(y.column_name-x.column_name))) diff, count(*) nofitems, floor(count(*)+1/2)
	  FROM table_name x, table_name y
	  GROUP BY x.column_name
	  HAVING SUM(SIGN(1.0-SIGN(y.column_name-x.column_name))) = floor((COUNT(*)+1)/2)
	      OR SUM(SIGN(1.0-SIGN(y.column_name-x.column_name))) = ceiling((COUNT(*)+1)/2)
	) x;

The following query finds the total number of commits per repo per contributor.
This query will then be combined with the median calculation from above 
to determine median commits per repo per contributor (or it could be used
in combination with other methods of determining activity level)

	select project_commits.project_id as project_id, commits.author_id as author_id, count(project_commits.commit_id) as num_commits
		from commits
	    join project_commits on commits.id = project_commits.commit_id
	    join projects on projects.id = project_commits.project_id
	group by project_id, author_id

I am working on a combination query for the median of contributer activity, but so far my attempts take too long to run and MySQL server times out.



### Pull Requests Accepted

Assume that a pull request with a history record of being 'merged' has been accepted

pull_request table includes both head_repo_id and base_repo_id
base repo is where the changes will go
head repo is where the changes are coming from
http://stackoverflow.com/questions/14034504/change-base-repo-for-github-pull-requests

Since we are talking about the approval of pull requests, I will choose the base repo since that is where the changes are going.
	
Note: some of these results look unusual, in that projects that I would believe would be very active have few approved pull requests.

Possibly these groups do not use pull requests as often and edit master directly?

	SELECT count(distinct pull_request_id) as num_approved, projects.name as project_name, projects.url as url
	FROM msr14.pull_request_history
		join pull_requests on pull_request_history.pull_request_id = pull_requests.id
		join projects on pull_requests.base_repo_id = projects.id
	where action = 'merged'
	group by projects.id
	


### Pull Requests Rejected

Assume that a pull request with a history record of being 'closed' but lacking one of being 'merged' has been rejected.

	SELECT count(distinct pull_request_id) as num_rejected, projects.name as project_name, projects.url as url
	FROM msr14.pull_request_history
		join pull_requests on pull_request_history.pull_request_id = pull_requests.id
		join projects on pull_requests.base_repo_id = projects.id
	where action = 'closed' AND pull_request_id not in 
		(SELECT pull_request_id
		FROM msr14.pull_request_history
		where action = 'merged')
	group by projects.id



### Project Watchers

	select count(user_id) as num_watchers, projects.name as project_name, url
	from watchers
		join projects on watchers.repo_id = projects.id
	group by projects.id




### Number of Open Issues (current)

	SELECT count(distinct issue_events.issue_id) as num_open_issues, projects.name as project_name, url as url
	FROM msr14.issue_events
		join issues on issues.id = issue_events.issue_id
		join projects on issues.repo_id = projects.id
	where issue_events.issue_id not in
		(SELECT issue_id FROM msr14.issue_events
		where action = 'closed')
	group by projects.id



### Average Comments per Issue per Project

	SELECT avg(avg_num_comments), project_name
	FROM
	(
		SELECT count(comment_id) as avg_num_comments, projects.name as project_name, projects.id as project_id
		FROM msr14.issue_comments
			join issues on issue_comments.issue_id = issues.id
			join projects on issues.repo_id = projects.id
		GROUP BY projects.id, issues.id
	) as comments_per_issue
	GROUP BY project_id



### Amount of time a closed issue was open before closing (excludes open issues)

[Information about MySQL date handling](https://dev.mysql.com/doc/refman/5.5/en/date-and-time-functions.html)
	
Days open by issue:

	select issue_id, open_date, closed_date, DATEDIFF(closed_date, open_date) as days_open, projects.name as project_name, url
	FROM
	(SELECT issues.id as issue_id, issues.created_at as open_date, issue_events.created_at as closed_date, repo_id
	FROM msr14.issue_events
		join issues on issues.id = issue_events.issue_id
	where action = 'closed') as closed_issues
	JOIN projects on projects.id = closed_issues.repo_id
	
Average days issue was open before closing by project:

	select avg(days_open) as average_days_til_issue_closed, project_name, url
	FROM
	(
		select DATEDIFF(closed_date, open_date) as days_open, projects.name as project_name, url, projects.id as project_id
		FROM
			(SELECT issues.id as issue_id, issues.created_at as open_date, issue_events.created_at as closed_date, repo_id
			FROM msr14.issue_events
				join issues on issues.id = issue_events.issue_id
			where action = 'closed') as closed_issues
		JOIN projects on projects.id = closed_issues.repo_id) as issues_days_open
	group by project_id

## Amount of time a currently open issue has been open (excludes closed issues):
	
	SELECT avg(date_difference) / 365.25 as average_in_years, avg(date_difference) as average_in_days, project_name, url
	FROM
	(
		SELECT CURDATE() as curr_date, open_date, DATEDIFF(CURDATE(), open_date) as date_difference, issue_id, project_name, url, project_id
		FROM
			(SELECT distinct issue_events.issue_id as issue_id, projects.name as project_name, url as url, issues.created_at as open_date, projects.id as project_id
				FROM msr14.issue_events
					join issues on issues.id = issue_events.issue_id
					join projects on issues.repo_id = projects.id
				where issue_events.issue_id not in
					(SELECT issue_id FROM msr14.issue_events
					where action = 'closed')
			) as open_issues
	) as date_diffs
	group by project_id
	
## Issue tags by project (all tags):
A note on this: I see some unusual results, such as projects with many issues but no "bug" tags.
A possibility is that some communities handle tags differently from others, and may use the "bug" tags more heavily than others.
This may become a problem in future queries I will write specifically targeting the "bug" tag (in that the results may not
be a good comparison between repos)
	
	SELECT count(issue_id) as num_issues_with_this_tag, repo_labels.name as tag, projects.name as project_name, url 
	FROM msr14.repo_labels
		join projects on repo_labels.repo_id = projects.id
		join issue_labels on issue_labels.label_id = repo_labels.id
	group by projects.id, repo_labels.id 

## Number of issues tagged as 'bug' by project:
	
	SELECT count(issue_id) num_bug_tags, repo_labels.name as tag, projects.name as project_name, url 
	FROM msr14.repo_labels
		join projects on repo_labels.repo_id = projects.id
		join issue_labels on issue_labels.label_id = repo_labels.id
	where repo_labels.name = 'bug'
	group by projects.id, repo_labels.id 
	
## Average days an issue tagged with 'bug' exists until a project member comments:

	SELECT avg(time_to_member_comment_in_days) as avg_days_to_member_comment, project_name, url
	FROM
	(
		SELECT DATEDIFF(earliest_member_comment, issue_created) time_to_member_comment_in_days, project_id, issue_id, project_name, url
		FROM
			(SELECT projects.id as project_id, 
					MIN(issue_comments.created_at) as earliest_member_comment, 
					issues.created_at as issue_created, 
					issues.id as issue_id, projects.name as project_name, url
			FROM msr14.repo_labels
				join projects on repo_labels.repo_id = projects.id
				join issue_labels on issue_labels.label_id = repo_labels.id
				join project_members on projects.id = project_members.repo_id
				join issues on issue_labels.issue_id = issues.id
				join issue_comments on issue_comments.issue_id = issues.id
			where repo_labels.name = 'bug'
				and issue_comments.user_id = project_members.user_id
			group by issues.id) as earliest_member_comments) as time_to_member_comment
	group by project_id

## Total number of organizations by project making pull requests:

	SELECT count(distinct org_id) as num_organizations, projects.name as project_name, url
	FROM
		organization_members
	    join users on organization_members.user_id = users.id
	    join pull_request_history on pull_request_history.actor_id = users.id
	    join pull_requests on pull_request_history.pull_request_id = pull_requests.id
	    join projects on pull_requests.base_repo_id = projects.id
	WHERE pull_request_history.action = 'opened'
	group by projects.id

Alternately, using the "company" field in the users table instead of the organization:

	SELECT count(distinct company) as num_companies, projects.name as project_name, url
	FROM
	    users
	    join pull_request_history on pull_request_history.actor_id = users.id
	    join pull_requests on pull_request_history.pull_request_id = pull_requests.id
	    join projects on pull_requests.base_repo_id = projects.id
	WHERE pull_request_history.action = 'opened' 
	GROUP BY projects.id
