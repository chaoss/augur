## Matt Hudson's Contributions to Software Engineering Group 5 Project (Fall 2019)

1. Performed deployment of Augur on my atmosphere server for testing purposes. Tasks included: researching augur installation process, solving dependency issue with gUnicorn,
installing augur data and setting up postgresql, fixing augur.config.json.

2. Adding route stubs to the routes.py files in augur/metrics/commit and augur/metrics/contributor. These functions set up the three API endpoints we developed.

3. Working on the commit.py and contributor.py files in /augur/metrics/commit and augur/metrics/contributor directories, respectively. This included defining the business
logic to return data for our three endpoints. 

4. Writing documentation for each sprint (Other contributors helped write the documentation as well)

5. Organizing group meetings and delegating tasks to other group members.

## Group 5's contributions

Our project involved creating three new API endpoints for Augur's backend server:

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

We modified the following files to add our three endpoints:<br>
(modified) [commit.py](./augur/metrics/commit/commit.py)<br>
Contains business logic for the first and second endpoints. These are the `repo_timeline` (line 201) and `repo_group_timeline` (line 215) methods, respectively.<br>
(modified) [contributors.py](./augur/metrics/contributor/contributor.py)<br>
contributors.py contains the business logic for the third endpoint. This is the `contributions` (line 571) method.<br>
(modified) [commit](./augur/metrics/commit/routes.py) and [contributor](./augur/metrics/contributor/routes.py) routes.py files <br>
Both routes.py files were updated to define the routes for all three endpoints. Routes in [commit](./augur/metrics/commit) are defined using the `server.addRepoMetric()` and `server.addRepoGroupMetric()` methods already present in Augur. The route in [contributor](./augur/metrics/contributor) is defined manually using the `@server.app.route()` annotation and defining the function `contributions` for this endpoint.<br>
(modified) test\_contributor\_functions.py<br>
test created to make sure the queries returned the correct values<br>
(modified) test\_contributor\_routes.py<br>
test created to make sure the routes correctly returned data<br>
