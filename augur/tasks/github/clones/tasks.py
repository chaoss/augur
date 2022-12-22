import time
import logging


from augur.tasks.init.celery_app import celery_app as celery, engine
from augur.application.db.data_parse import *
from augur.tasks.github.util.github_paginator import GithubPaginator, hit_api
from augur.tasks.github.util.github_task_session import GithubTaskSession
from augur.tasks.util.worker_util import remove_duplicate_dicts
from augur.tasks.github.util.util import get_owner_repo
from augur.application.db.models import RepoClone
from augur.application.db.util import execute_session_query

@celery.task
def collect_github_clones(repo_git: str) -> None:
    pass