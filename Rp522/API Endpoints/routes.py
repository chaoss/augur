"""
Routes for two new endpoints in the routes.py file of the commit folder in metrics
"""

    """
    @api {get} /repo-groups/:repo_group_id/repos/:repo_id/repo-timeline Timeline for Repo
    @apiName repo-timeline
    @apiGroup Experimental
    @apiDescription This is an Augur-specific metric. We are currently working to define these more formally. Source: Git Repository
    @apiParam {String} repo_url_base Base64 version of the URL of the GitHub repository as it appears in the Facade DB
    @apiSuccessExample {json} Success-Response:
                        [
                           "repo-id": 1,
                           "timeline": [
                            {"date": "10-07-19", "commits": 5},
                            {"date": "10-09-19", "commits": 2},
                            {"date": "11-02-19", "commits": 4}
                           ]
                        ]
    """
    server.addRepoMetric(metrics.repo_timeline,'repo-timeline')

    """
    @api {get} /repo-groups/:repo_group_id/repo-group-timeline Timeline for Repo Group
    @apiName repo-group-timeline
    @apiGroup Experimental
    @apiDescription This is an Augur-specific metric. We are currently working to define these more formally. Source: Git Repository
    @apiParam {String} repo_url_base Base64 version of the URL of the GitHub repository as it appears in the Facade DB
    @apiSuccessExample {json} Success-Response:
                        [
                            "repo_group_id": 1,
                            "timelines": [
                                {
                                   "repo_id": 1,
                                    "timeline": [
                                    { "date": "10-07-19", "commits": 5},
                                    { "date": "10-09-19", "commits": 2},
                                    { "date": "11-02-19", "commits": 4}
                                    ]
                                },
                                {
                                    "repo_id": 2,
                                    "timeline": [
                                    { "date": "10-09-19": "commits": 1}
                                    ]
                                }
                            ]
                        ]
    """
    server.addRepoGroupMetric(metrics.repo_group_timeline,'repo-group-timeline')
