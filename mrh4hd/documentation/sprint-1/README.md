# Semester Project Sprint 1

Fall 2019

Group 5: Jake Alongi, Matt Hudson, Tim Kuehker, Rebecca Parker

# Table of Contents

Use Cases

Data Sources

Technologies Needed

Design Overview / Endpoint Definitions

Appendix (notes we made during class)

## Use Cases

1. Repo contributor:

A repo contributor wants a personal &quot;GitHub Report.&quot; They gather data about their personal commits over time to produce a graph to visualize their commits over time.

1. Repo manager:

A manager of a repo identifies points of interest in the life of the repo to identify peak productivity. They want to see times of peak productivity in workers, so they use the endpoint to gather data to visualize the commits over time.

1. Repo manager:

A repo manager wants to see the distribution of work for an employee among multiple repos. They are able to gather data on which repos an employee commits most and/or least to, and use this insight to assign work to multiple developers among multiple repos.

## Data Sources

Augur Database:

1. Data selected from key **cntrb\_id** from **Contributors** table. Each cntrb\_id has a one-to-many commits that have the relevant info needed: cmt\_committer\_date is the only required data needed and the cntrb\_id to query the results.
2. From **repo** table we need the **repo\_id** key, from there we can select a count of unique cmt\_id keys from commits. If we want to organize by date we need the cmt\_author\_date as well.
3. Data would be selected from key **repo\_id** from the **repo** table which would give us a set of commits tables for that repo, for each **repo\_id** in the **commits** table we would match the **cmt\_committer\_name** with the commits from other repos to see if the same user is committing in different repos. Alternatively we could instead use the **contributors** table to query by **cntrb\_id** and count the number of **commit\_id** in **commits** affiliated with the **cntrb\_id**. We would still have to do this for all repos. **Commits** table has the date of each commit if we wanted to display this on a timeline in cmt\_author\_date.

## Technologies Needed

**Flask** - Python server framework for serving API endpoints. We chose this over NodeJS, even though some of us have Node experience, we noticed Flask is used in Augur, so we wanted to use the same framework. We will need to look into the tutorials on how to make Flask endpoints, but we have experience in serving JSON.

**SQL** (the Augur database) - we will need to execute SQL queries on the Augur database in order to grab the data we need for our project.

**A Linux Server** - these are the ones we got in class. We can use this to serve the endpoints and test our project by deploying the Flask there.

## Design Overview / Endpoint Definitions

To get the data:

1. Access the database through an SQL query
2. Get the results back, pack into JSON
3. Send JSON back

Specific to each endpoint:

1. Repo timeline

- --This endpoint is given a repo\_id, which we can use to search for the commits associated with this repo. Then, we will examine each commit and see when it was committed. We then construct an array of datapoints, like on a line graph, that map dates to numbers of commits. For example:

{repo\_id: \&lt;repoid\&gt;,

timeline: [{date: \&lt;date 1\&gt;, commits: 4}, {date: \&lt;date 2\&gt;, commits: 5}, etc. etc.]

}

2. Repo Group Timeline

- --This endpoint works on the same principle as [1], but is for an entire repo group rather than a single repo. This endpoint will return timelines for each repo in the group. So, we will find all repos with repo\_group = the provided, and return a list of timelines:
- --{repo\_group\_id: \&lt;repogroupid\&gt;,

timelines: [{repo\_id: \&lt;repoid\&gt;,

timeline: [{date: \&lt;date 1\&gt;, commits: 4}, {date: \&lt;date 2\&gt;, commits: 5}, etc. etc.]},

{another timeline here, etc}]

}

3. Repos/commits per contributor

- --For this endpoint, it will be provided the ID of a specific contributor. Then, we will use that ID to find every commit by that user, then return a list of repos the contributor has worked on, as well as how many commits per repo.

## Appendix (notes we made during class)

**Useful Links**

[ERD](https://raw.githubusercontent.com/chaoss/augur/master/persistence_schema/new-augur.0.1.0.0.png)

[Create A Metric](https://oss-augur.readthedocs.io/en/dev/getting-started/create-a-metric/create-a-metric-toc.html)



3 Metric Endpoints?

1. Individual commits organized in a timeline
2. Group commits with the same idea as (1)
3. How many repos a certain user has/is working on (add # of commits per repo?)



Possible methods:

1. 1)Python server (Flask) (might want to use because tutorials are also in python for SQL)
2. 2)Otherwise, run a node/express server - would need to research how to access SQL in this

^^ on this, assess background for team members; what would be best?

(Implement a first pass) - in the backlog, not relevant to this sprint

Need to design 3 use cases,

Document design decisions, plus

- --Describing how features will be built from data (so, how these endpoints will take in the data and pack into JSON)
- --Clarify requirements

What parts of the ERD are going to be relevant? (i.e. what data will we need to pull in?)

Simple design document (drafts) that specify what functions, etc we&#39;re going to need

1. 1)Timeline (points on a graph) -

- --Input: start date, end date (through route parameters or get parameters)
- --Also, need repo id and repo group id
- --Query: &#39;select \&lt;some stuff\&gt; from commits where repo\_id=provided and repo\_group\_id = provided&#39;
- --Some stuff = date of commit, user who committed it
- -- for each unique date, count number of commits, add number to array of points
- --So for example points = [{date: Nov 6 2018, commits: 6}, {date: Dec 6 2018, commits: 2}, etc. etc.] \&lt;= return this?

1. 2)Same as (1), but only search by repo group, get that data instead
2. 3)Input user id, get user id, go into commits, iterate, look for user\_id, if so, add the repo to an array, also count number of commits and add that, so

[{repo: &#39;rails&#39;, commits: &#39;46&#39;}, {repo: &#39;hive&#39;, commits: &#39;2&#39;}] \&lt;= return this
