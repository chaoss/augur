# Group 5 Sprint 2

Jacob Alongi, Matt Hudson, Tim Kuehner, Rebecca Parker (API)

**Link to deployed project:** (API) -> http://129.114.16.101:5000/api/unstable/

New API endpoints (partially implemented): http://129.114.16.101:5000/api/unstable/repo-groups/20/repos/25430/repo-timeline (Endpoint 1)

http://129.114.16.101:5000/api/unstable/repo-groups/1/repo-group-timeline (Endpoint 2 partially implemented)

http://129.114.16.101:5000/api/unstable/contributors/hudso1898/contributions (Endpoint 3 partially implemented)

## What we are trying to accomplish

For this sprint, a lot of our group time was devoted to getting augur deployed and running on our Linux servers. Here are list of the problems we faced and how we solved them:

- Running `make install` generates a ton of errors; however, we eventually figured out we can still run augur even with these 'build failures'.

- We figured out we needed to install the augur database schema in `make install` in order to have the database work properly.

- The augur user was unable to log in; this was due to repeated entries in my .pgpass file due to repeated failed installs. Resetting the file fixed this issue.

- Augur's backend server was unable to run due to a newer, broken version of `gunicorn`, which is the web server that serves the API. Downgrading that to version 19.9.0 fixed this issue.

- We believed at first to set the server IP to the public IP (what we used to SSH and access through a web browser). However, augur would not start the server at that IP: "invalid IP address".
Changing this to the private IP address of the server fixed this and allows access through a web browser (probably because it defines the local listening address).

On Tuesday/Thursday, we were focused on figuring out how to add the route stubs and define new endpoints. We went over how to define JSON objects, and in which files we needed to add to in
order to implement new endpoints. We met on Sunday to finish the Sprint, but all of our time was devoted to getting augur (just the master branch with no changes) to build and run. We finally
managed to get augur running on Monday, so we could add our endpoints and fix up our route stubs.

## Intended Design

This is what we sent Dr. Goggins on Slack for our endpoints: 

1) Repo timeline
This endpoint is given a repo\_id, which we can use to search for the commits associated with this repo. Then, we will examine each commit and see when it was committed. We then construct an array of datapoints, like on a line graph, that map dates to numbers of commits. For example:
{repo\_id: <repoid>,
timeline: [{date: <date 1>, commits: 4}, {date: <date 2>, commits: 5}, etc. etc.]
}
2) Repo Group Timeline
This endpoint works on the same principle as [1], but is for an entire repo group rather than a single repo. This endpoint will return timelines for each repo in the group. So, we will find all repos with repo\_group = the provided, and return a list of timelines:
{repo\_group\_id: <repogroupid>,
timelines: [{repo\_id: <repoid>,
timeline: [{date: <date 1>, commits: 4}, {date: <date 2>, commits: 5}, etc. etc.]},
{another timeline here, etc}]
}
3) Repos/commits per contributor
For this endpoint, it will be provided the ID of a specific contributor. Then, we will use that ID to find every commit by that user, then return a list of repos the contributor has worked on, as well as how many commits per repo.

As clarified, 1) is an endpoint for a specific repository. (2) would be an endpoint for the entire repo group and return timelines for every repo in that group.

In this sprint, we were able to get augur deployed on our server, and then to add new endpoints that return data. Currently, we haven't implemented database access, only returning static JSON.
However, all 3 endpoints are up, and all that is left to do is to add the SQL and business logic. 

## Routes.py stubs

You can find the stubs:

1) In the 'commits' metrics folder.

2) In the 'commits' metrics folder.

3) In the 'contributor' metrics folder.

We discovered how to add these stubs to the existing folders based on the category of our endpoints. We agreed that (1) and (2) are metrics best defined by commits, and (3) as a metric best
defined by contributors. For the first two endpoints, we used the existing methods and followed the existing patterns to add Repo and RepoGroup metrics. For (3), we used a custom route for
our contributor since we'll be implementing the endpoint for contributors, and that doesn't follow the standard repo-groups/:gid/repos/:rid/<something> path the former makes.

## Endpoint Implementation

We've defined basic python functions to serve the 3 endpoints we defined. Currently, they return JSON to demonstrate successful deployment. Endpoint (1), however, actually implements an SQL query, and returns JSON in the format
we specified for the repo timeline and runs the SQL query we designed for the endpoint. We put these functions in [this file for commit](./augur/metrics/commit/commit.py) and [this file for contributor](./augur/metrics/contributor/contributor.py).

## Future for Sprint 3

Now that we have augur deployed and are serving new endpoints, Sprint 3 should focus on defining the SQL queries and business logic for actually forming the data response.

