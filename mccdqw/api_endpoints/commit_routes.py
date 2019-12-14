from flask import Response

    """
    @api {get} /repo-groups/:repo_group_id/committer-data Committer Data (Repo Group)
    @apiName committer-data
    @apiGroup Experimental
    @apiDescription Returns information on contributors to a repo group, including a prediction of their gender.
    @apiParam {String} repo_group_id Repository Group ID
    @apiSuccessExample {json} Success-Response:
                        [
                            {
                                "cmt_author_name": "Alberto Martín",
                                "cmt_author_affiliation": "NULL",
                                "repo_id": 25431,
                                "gender": "male",
                                "genderProb": -0.9371237245,
                                "eth": "HL",
                                "ethProb": 0.8202765757
                            }
                        ]
    """
    server.addRepoGroupMetric(metrics.committer_data,'committer-data')
