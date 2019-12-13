from flask import Response


def create_experimental_routes(server):

	metrics = server._augur.metrics

	"""
	@api {get} /repo-groups/:repo_group_id/contributor-location Contributor Location (Repo Group)
	@apiName contributor-locationw-repo-group
	@apiGroup Evolution
	@apiDescription Time series of number of new issues opened during a certain period.
	                <a href="https://github.com/chaoss/wg-evolution/blob/master/metrics/Issues_New.md">CHAOSS Metric Definition</a>
	@apiParam {string} repo_group_id Repository Group ID
	@apiParam {string=day, week, month, year} [period="day"] Periodicity specification.
	@apiParam {string} [begin_date="1970-1-1 0:0:0"] Beginning date specification. E.g. values: `2018`, `2018-05`, `2019-05-01`
	@apiParam {string} [end_date="current date"] Ending date specification. E.g. values: `2018`, `2018-05`, `2019-05-01`
	@apiSuccessExample {json} Success-Response:
	                [
	                    {
	                        "repo_id": 21000,
	                        "repo_name": "rails",
	                        "date": "2019-01-01T00:00:00.000Z",
	                        "issues": 318
	                    },
	                    {
	                        "repo_id": 21002,
	                        "repo_name": "acts_as_list",
	                        "date": "2009-01-01T00:00:00.000Z",
	                        "issues": 1
	                    },
	                    {
	                        "repo_id": 21002,
	                        "repo_name": "acts_as_list",
	                        "date": "2010-01-01T00:00:00.000Z",
	                        "issues": 7
	                    }
	                ]
	"""
    server.addRepoGroupMetric(metrics.contributor_location,'contributor-location')