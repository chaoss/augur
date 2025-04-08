from sqlalchemy import Column, String, Integer

class AugurData:
    dep_name = Column(String, comment="Name of the dependency found in project. ")
    dep_count = Column(Integer, comment="Number of times the dependency was found. ")
    dep_language = Column(String, comment="Language of the dependency. ")

    worker_run_id = Column(Integer, comment="This column is used to indicate analyzes run by a worker during the same execution period, and is useful for grouping, and time series analysis. ")

    pull_request_info = Column(String, comment='This is a representation of the repo:branch information in the pull request. Head is issuing the pull request and base is taking the pull request. For example:  (We do not store all of this)\n\n "head": {\n      "label": "chaoss:pull-request-worker",\n      "ref": "pull-request-worke') 