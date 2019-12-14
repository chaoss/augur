# My contributions:
Designed the API endpoints that would be made conceptually. 

## The 3 endpoints I designed that we implemented:
  
1.	Data selected from key cntrb_id from Contributors table. Each cntrb_id has a one-to-many commits that have the relevant info needed: cmt_committer_date is the only required data needed and the cntrb_id to query the results.

	Repo timeline
	--This endpoint is given a repo_id, which we can use to search for the commits associated with this repo. Then, we will examine each commit and see when it was committed. We then construct an array of datapoints, like on a line graph, that map dates to numbers of commits. For example:
{repo_id: &lt;repoid&gt;,
timeline: [{date: &lt;date 1&gt;, commits: 4}, {date: &lt;date 2&gt;, commits: 5}, etc. etc.]
}


2.	From repo table we need the repo_id key, from there we can select a count of unique cmt_id keys from commits. If we want to organize by date we need the cmt_author_date as well.
	Repo Group Timeline
	--This endpoint works on the same principle as [1], but is for an entire repo group rather than a single repo. This endpoint will return timelines for each repo in the group. So, we will find all repos with repo_group = the provided, and return a list of timelines:
	--{repo_group_id: &lt;repogroupid&gt;,
timelines: [{repo_id: &lt;repoid&gt;,
timeline: [{date: &lt;date 1&gt;, commits: 4}, {date: &lt;date 2&gt;, commits: 5}, etc. etc.]},
{another timeline here, etc}]
}


3.	Data would be selected from key repo_id from the repo table which would give us a set of commits tables for that repo, for each repo_id in the commits table we would match the cmt_committer_name with the commits from other repos to see if the same user is committing in different repos. Alternatively we could instead use the contributors table to query by cntrb_id and count the number of commit_id in commits affiliated with the cntrb_id. We would still have to do this for all repos. Commits table has the date of each commit if we wanted to display this on a timeline in cmt_author_date.
	Repos/commits per contributor
	--For this endpoint, it will be provided the ID of a specific contributor. Then, we will use that ID to find every commit by that user, then return a list of repos the contributor has worked on, as well as how many commits per repo.

	Repo timeline This endpoint is given a repo_id, which we can use to search for the commits associated with this repo. Then, we will examine each commit and see when it was committed. We then construct an array of datapoints, like on a line graph, that map dates to numbers of commits. For example: {repo_id: , timeline: [{date: <date 1>, commits: 4}, {date: <date 2>, commits: 5}, etc. etc.] }
	Repo Group Timeline This endpoint works on the same principle as [1], but is for an entire repo group rather than a single repo. This endpoint will return timelines for each repo in the group. So, we will find all repos with repo_group = the provided, and return a list of timelines: {repo_group_id: , timelines: [{repo_id: , timeline: [{date: <date 1>, commits: 4}, {date: <date 2>, commits: 5}, etc. etc.]}, {another timeline here, etc}] }
	Repos/commits per contributor For this endpoint, it will be provided the ID of a specific contributor. Then, we will use that ID to find every commit by that user, then return a list of repos the contributor has worked on, as well as how many commits per repo.


## Wrote the SQL queries to create the endpoints and assisted matt with implementing them
      
      
Helped write the documentiation, showed up for the meetings, contributed constructively and helped design our implementation for the project
