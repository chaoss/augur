"""
    @api {get} /repo-groups/:repo_group_id/contributor-affiliation Contributor Affiliation (Repo)
    @apiNames contributor-affiliation
    @apiGroup Experimental
    @apiDescription Returns meta data on contributors.
    @apiParam {string} repo_group_id Repository Group ID
    @apiSuccessExample {json} Success-Response:
                    [
                        {
                            "cntrb_id": 277110,
                            "cntrb_company": "University of Missouri & Miner Technologies, LLC",
                            "cntrb_created_at": "2010-08-29T16:25:48.000Z",
                            "cntrb_location": "Columbia, MO",
                            "gh_login": "sgoggins",
                            "gh_html_url": "https://github.com/sgoggins",
                            "lat": 38.9517053,
                            "lng": -92.3340724
                        }
                    ]
    """
    server.addRepoGroupMetric(metrics.contributor_affiliation,'contributor-affiliation')
