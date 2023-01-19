import logging 
import traceback
from augur.tasks.github.util.github_task_session import GithubTaskSession
from augur.tasks.github.pull_requests.commits_model.core import *
from augur.tasks.init.celery_app import celery_app as celery
from augur.application.db.util import execute_session_query


@celery.task
def process_pull_request_commits(repo_git_identifiers: [str]) -> None:
    logger = logging.getLogger(process_pull_request_commits.__name__)

    for repo_git in repo_git_identifiers:
        with GithubTaskSession(logger) as session:
            query = session.query(Repo).filter(Repo.repo_git == repo_git)
            repo = execute_session_query(query, 'one')
            try:
                pull_request_commits_model(repo.repo_id, logger)
            except Exception as e:
                logger.error(f"Could not complete pull_request_commits_model!\n Reason: {e} \n Traceback: {''.join(traceback.format_exception(None, e, e.__traceback__))}")
                raise e
