# Group 5 Sprint 3 (Software Engineering Fall 2019)

## Jake Alongi, Matt Hudson, Tim Kuehner, Rebecca Parker

## Links to running endpoints

http://129.114.16.101:5000/api/unstable/ - base server address for the api

Endpoint 1 (Repo Timeline) - http://129.114.16.101:5000/api/unstable/repo-groups/20/repos/25430/repo-timeline

Endpoint 2 (Repo Group Timeline) - http://129.114.16.101:5000/api/unstable/repo-groups/20/repo-group-timeline

Endpoint 3 (Contributions) - http://129.114.16.101:5000/api/unstable/contributors/s@goggins.com/contributions

## Endpoints

We defined endpoints 1 and 2 in the [commit](../augur/metrics/commit/commit.py) file and endpoint 3 in the [contributor](../augur/metrics/contributor/contributor.py) file. For each of these endpoints, we defined SQL queries to connect to the
database and retrieve the required information. For endpoint 1, we are given the repo id, so we find `commit` entries that
match the given repo id. For these, we find, for each date, the number of commits (using COUNT(\*)), and present this in a list
of objects containing this information. We also group by and order by the date ascendinging.

For endpoint 2, we did two queries: one to get all the repo ids given the group, then to find the same information as endpoint
1 using a second query. The difficulty in this was converting between Panda's DataFrame structure and python's native lists
and dictionaries. The output format is also different, this is something we can change in sprint 4.

For endpoint 3, we did a single query given the email of the contributor instead of the id. We decided this because the email
is also a unique identifier but is more readable and knowable than the contributor id. We return a list of repos the contributor has commits in, and the number of contributions in that repository. 

## Tests
We modeled them after the existing design in order to stay consistent with the current tests. First, we created functional tests to ensure that the function will actually execute. We first mocked the metrics model and then called the new functions to test that some values were returned. In addition, we tested the routes on the live development server to ensure that the function executes on the live server as well, returning non-empty data. 
