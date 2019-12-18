from flask import Response

def create_insight_routes(server):

    metrics = server._augur.metrics

    """
    @api {get} /top-insights Top Insights
    @apiName top-insights
    @apiGroup Utility
    @apiDescription Get all the downloaded repo groups.
    @apiSuccessExample {json} Success-Response:
                    [
                        {
                            "repo_group_id": 20,
                            "rg_name": "Rails",
                            "rg_description": "Rails Ecosystem.",
                            "rg_website": "",
                            "rg_recache": 0,
                            "rg_last_modified": "2019-06-03T15:55:20.000Z",
                            "rg_type": "GitHub Organization",
                            "tool_source": "load",
                            "tool_version": "one",
                            "data_source": "git",
                            "data_collection_date": "2019-06-05T13:36:25.000Z"
                        },
                        {
                            "repo_group_id": 23,
                            "rg_name": "Netflix",
                            "rg_description": "Netflix Ecosystem.",
                            "rg_website": "",
                            "rg_recache": 0,
                            "rg_last_modified": "2019-06-03T15:55:20.000Z",
                            "rg_type": "GitHub Organization",
                            "tool_source": "load",
                            "tool_version": "one",
                            "data_source": "git",
                            "data_collection_date": "2019-06-05T13:36:36.000Z"
                        }
                    ]
    """
    server.addRepoGroupMetric(metrics.top_insights, 'top-insights')

	
    """
    API Documentation
    @api {get} /repo/repo_id/testing-coverage Testing Coverage (Repo)
    @apiName testing-coverage-repo
    @apiGroup Risk
    @apiDescription Determine how much code has been tested for a repo 
        <a href="https://github.com/chaoss/wg-risk/blob/master/metrics/Test_Coverage.md">CHAOSS Metric Definition</a>
    @apiParam {string} repo_group_id Repository Group ID
    @apiParam {string} [begin_date="1970-1-1 0:0:0"] Beginning date specification. E.g. values: `2018`, `2018-05`, `2019-05-01`
    @apiParam {string} [end_date="current date"] Ending date specification. E.g. values: `2018`, `2018-05`, `2019-05-01`
    @apiSuccessExample {json} Success-Response:
	    [
	                {
	                    "repo_id": 21000,
	                    "repo_name": "rails",
	                    "date": "2019-01-01T00:00:00.000Z",
	                    "file_statement_count": 318
			    "file_subroutine_count": 222
			    "file_statements_tested": 300
			    "file_subroutines_tested": 210
	                },
	                {
	                    "repo_id": 21002,
	                    "repo_name": "acts_as_list",
	                    "date": "2009-01-01T00:00:00.000Z",
	                    "file_statement_count": 435
			    "file_subroutine_count": 430
			    "file_statements_tested": 354
			    "file_subroutines_tested": 320
	                },
	                {
	                    "repo_id": 21002,
	                    "repo_name": "acts_as_list",
	                    "date": "2010-01-01T00:00:00.000Z",
	                    "file_statement_count": 214
			    "file_subroutine_count": 198
			    "file_statements_tested": 321
			    "file_subroutines_tested": 298
	                }
	    ]
    """
    server.addRepoGroupMetric(metrics.testing_coverage,'testing-coverage')
    
