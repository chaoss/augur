import logging
from augur.application.db.session import DatabaseSession
from augur.tasks.git.scc_value_tasks.core import *
from augur.tasks.init.celery_app import celery_app as celery
from augur.tasks.init.celery_app import AugurFacadeRepoCollectionTask
from augur.application.db.util import execute_session_query
from augur.application.db.lib import get_value
from augur.tasks.git.util.facade_worker.facade_worker.utilitymethods import get_absolute_repo_path


@celery.task(base=AugurFacadeRepoCollectionTask, bind=True)
def process_scc_value_metrics(self, repo_git):

    engine = self.app.engine

    logger = logging.getLogger(process_scc_value_metrics.__name__)

    with DatabaseSession(logger,engine) as session:
        logger.info(f"repo_git: {repo_git}")

        query = session.query(Repo).filter(Repo.repo_git == repo_git)
        repo = execute_session_query(query, 'one')

        absolute_repo_path = get_absolute_repo_path(get_value("Facade", "repo_directory"),repo.repo_id,repo.repo_path,repo.repo_name)

        value_model(session,repo_git,repo.repo_id, absolute_repo_path)