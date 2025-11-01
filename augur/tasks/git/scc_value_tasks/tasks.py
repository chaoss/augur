import logging
from augur.application.db.lib import get_session
from augur.tasks.git.scc_value_tasks.core import *
from augur.tasks.init.celery_app import celery_app as celery
from augur.tasks.init.celery_app import AugurFacadeRepoCollectionTask

logger=logging.getLogger(__name__)
@celery.task(base=AugurFacadeRepoCollectionTask)
def process_scc_value_metrics(repo_git):


    value_model(logger,repo_git,)