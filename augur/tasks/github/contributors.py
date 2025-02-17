"""
import time
import logging
import traceback 

from augur.tasks.init.celery_app import celery_app as celery
from augur.tasks.init.celery_app import AugurCoreRepoCollectionTask
from augur.tasks.github.util.github_paginator import hit_api
from augur.tasks.github.facade_github.tasks import *
from augur.application.db.models import Contributor
from augur.application.db.util import execute_session_query
from augur.application.db.lib import bulk_insert_dicts, get_session
from augur.tasks.github.util.github_random_key_auth import GithubRandomKeyAuth
""" 
import time
import logging
import traceback
import random

from sqlalchemy.exc import OperationalError
from psycopg2.errors import DeadlockDetected

from augur.tasks.init.celery_app import celery_app as celery
from augur.tasks.init.celery_app import AugurCoreRepoCollectionTask
from augur.tasks.github.util.github_paginator import hit_api
from augur.tasks.github.facade_github.tasks import * 
from augur.application.db.models import Contributor
from augur.application.db.util import execute_session_query
from augur.application.db.lib import bulk_insert_dicts, get_session
from augur.tasks.github.util.github_random_key_auth import GithubRandomKeyAuth


"""  
@celery.task
def process_contributors():

    logger = logging.getLogger(process_contributors.__name__)

    tool_source = "Contributors task"
    tool_version = "2.0"
    data_source = "Github API"

    key_auth = GithubRandomKeyAuth(logger)

    with get_session() as session:

        query = session.query(Contributor).filter(Contributor.data_source == data_source, Contributor.cntrb_created_at is None, Contributor.cntrb_last_used is None)
        contributors = execute_session_query(query, 'all')

    contributors_len = len(contributors)

    if contributors_len == 0:
        logger.info("No contributors to enrich...returning...")
        return

    print(f"Length of contributors to enrich: {contributors_len}")
    enriched_contributors = []
    for index, contributor in enumerate(contributors):

        logger.info(f"Contributor {index + 1} of {contributors_len}")

        contributor_dict = contributor.__dict__

        del contributor_dict["_sa_instance_state"]

        url = f"https://api.github.com/users/{contributor_dict['cntrb_login']}" 

        data = retrieve_dict_data(url, key_auth, logger)

        if data is None:
            print(f"Unable to get contributor data for: {contributor_dict['cntrb_login']}")
            continue

        new_contributor_data = {
            "cntrb_created_at": data["created_at"],
            "cntrb_last_used": data["updated_at"]
        }

        contributor_dict.update(new_contributor_data)

        enriched_contributors.append(contributor_dict)

    logger.info(f"Enriching {len(enriched_contributors)} contributors")
    bulk_insert_dicts(enriched_contributors, Contributor, ["cntrb_id"])


""" 

@celery.task
def process_contributors():
    logger = logging.getLogger(process_contributors.__name__)

    tool_source = "Contributors task"
    tool_version = "3.0"
    data_source = "Github API"

    key_auth = GithubRandomKeyAuth(logger)

    with get_session() as session:
        query = session.query(Contributor).filter(
            Contributor.data_source == data_source,
            Contributor.cntrb_created_at.is_(None),
            Contributor.cntrb_last_used.is_(None)
        )
        contributors = execute_session_query(query, 'all')

    contributors_len = len(contributors)

    if contributors_len == 0:
        logger.info("No contributors to enrich...returning...")
        return

    logger.info(f"Length of contributors to enrich: {contributors_len}")

    batch_size = 50  # Adjust batch size as needed
    max_retries = 5
    enriched_contributors = []

    for index, contributor in enumerate(contributors):
        logger.info(f"Processing Contributor {index + 1} of {contributors_len}")

        contributor_dict = contributor.__dict__
        del contributor_dict["_sa_instance_state"]

        url = f"https://api.github.com/users/{contributor_dict['cntrb_login']}" 
        data = retrieve_dict_data(url, key_auth, logger)

        if data is None:
            logger.warning(f"Unable to get contributor data for: {contributor_dict['cntrb_login']}")
            continue

        new_contributor_data = {
            "cntrb_created_at": data["created_at"],
            "cntrb_last_used": data["updated_at"]
        }

        contributor_dict.update(new_contributor_data)
        enriched_contributors.append(contributor_dict)

        # Process in batches to reduce deadlocks
        if len(enriched_contributors) >= batch_size:
            _insert_with_retries(enriched_contributors, max_retries, logger)
            enriched_contributors = []

    # Insert remaining contributors
    if enriched_contributors:
        _insert_with_retries(enriched_contributors, max_retries, logger)

def _insert_with_retries(contributors_batch, max_retries, logger):
    """Handles deadlocks by retrying transactions with exponential backoff."""
    retries = 0
    while retries < max_retries:
        try:
            bulk_insert_dicts(contributors_batch, Contributor, ["cntrb_id"])
            return  # Exit function if successful
        except (OperationalError, DeadlockDetected) as e:
            wait_time = 2 ** retries + random.uniform(0, 1)  # Exponential backoff
            logger.warning(f"Deadlock detected, retrying in {wait_time:.2f} seconds... (Attempt {retries + 1}/{max_retries})")
            time.sleep(wait_time)
            retries += 1
        except Exception as e:
            logger.error(f"Unexpected error during batch insert: {e}")
            break  # Exit on non-deadlock errors

    logger.error("Max retries reached. Some records may not have been inserted.")


def retrieve_dict_data(url: str, key_auth, logger):

    num_attempts = 0
    while num_attempts <= 10:

        response = hit_api(key_auth, url, logger)

        # increment attempts
        if response is None:
            num_attempts += 1
            continue
        # update rate limit here

        page_data = response.json()

        if "message" in page_data:

            if page_data['message'] == "Not Found":
                logger.info(
                    "Github repo was not found or does not exist for endpoint: "
                    f"{response.url}\n"
                )
                break

            elif "You have exceeded a secondary rate limit. Please wait a few minutes before you try again" in page_data['message']:
                logger.info('\n\n\n\nSleeping for 100 seconds due to secondary rate limit issue.\n\n\n\n')
                time.sleep(100)
                continue

            elif "You have triggered an abuse detection mechanism." in page_data['message']:
                #self.update_rate_limit(response, temporarily_disable=True,platform=platform)
                continue
        else:
            return page_data


    return None


@celery.task(base=AugurCoreRepoCollectionTask, bind=True)
def grab_comitters(self, repo_git,platform="github"):

    engine = self.app.engine

    logger = logging.getLogger(grab_comitters.__name__)

    try:
        key_auth = GithubRandomKeyAuth(logger)
        grab_committer_list(logger, key_auth, repo_git, platform)
    except Exception as e:
        logger.error(f"Could not grab committers from github endpoint!\n Reason: {e} \n Traceback: {''.join(traceback.format_exception(None, e, e.__traceback__))}")

