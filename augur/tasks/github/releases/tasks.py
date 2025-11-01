import logging

from augur.tasks.github.releases.core import *
from augur.tasks.init.celery_app import celery_app as celery
from augur.tasks.init.celery_app import AugurCoreRepoCollectionTask
from augur.application.db.lib import get_repo_by_repo_git, get_session
from augur.tasks.github.util.github_random_key_auth import GithubRandomKeyAuth

logger=logging.getLogger(__name__)
@celery.task(base=AugurCoreRepoCollectionTask)
def collect_releases(repo_git):

    repo_obj = get_repo_by_repo_git(repo_git)
    repo_id = repo_obj.repo_id

    key_auth = GithubRandomKeyAuth(logger)

    with get_session() as session:

        releases_model(session, key_auth, logger, repo_git, repo_id)