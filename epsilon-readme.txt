Our SQL queries have been tested using pgAdmin, and are wrapped in Python. The python can be found in augur/api/metrics/organizations.py.

A description of our endpoints, the metrics they create data for, and their output values can be found in "Endpoint Documentation.pdf"

Four endpoints, "Maintainers", "Contributor Affiliations", "Peripheral Organizations", and "Organizations Contributing" can be
accessed on the server. We believe that "Peripheral Organizations" returns no data because no pull requests in our database have
been made by users with company affiliations. We don't know why attempting to access Organizational Influence gives a server error.

On the Organizations Contributing endpoint:
Originally we planned for this endpoint to return information on all the companies that have contributed to a project. However,
this proved to be too difficult so we changed it so that it takes a company name as input and only returns information on that
one company. By default, the company name will be "bitnami". We later discovered that standard metrics can only take a repo id
as input. Yet Organizations Contributing can still be accessed despite it not conforming to the standard metric parameters.