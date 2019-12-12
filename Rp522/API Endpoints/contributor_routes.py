"""
Routes for contributors endpoint
"""

    """
    @api {get} /contributors/:contributor_email/contributions
    @apiName contributions
    @apiGroup Experimental
    @apiDescription Returns a list of contributions from a specified user.
    @apiParam {string} [contributor-name] Specify the contributor to retrieve contributions for
    @apiSuccessExample {json} Success-Response:
                    [
                        
                    ]
    """
    @server.app.route('/{}/contributors/<contributor_email>/contributions'.format(server.api_version))
    def contributions(contributor_email):
        response = server.transform(metrics.contributions, args=[contributor_email])
        return Response(response=response, status=200, mimetype="application/json")
