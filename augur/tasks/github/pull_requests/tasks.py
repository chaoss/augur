import logging
from datetime import datetime, timedelta, timezone

from augur.tasks.github.pull_requests.core import extract_data_from_pr_list
from augur.tasks.init.celery_app import celery_app as celery
from augur.tasks.init.celery_app import AugurCoreRepoCollectionTask, AugurSecondaryRepoCollectionTask
from augur.application.db.data_parse import *
from augur.tasks.github.util.github_data_access import GithubDataAccess, UrlNotFoundException
from augur.tasks.util.worker_util import remove_duplicate_dicts
from augur.tasks.github.util.util import add_key_value_pair_to_dicts, get_owner_repo
from augur.application.db.models import PullRequest, Message, PullRequestReview, PullRequestLabel, PullRequestReviewer, PullRequestMeta, PullRequestAssignee, PullRequestReviewMessageRef, Contributor, Repo
from augur.tasks.github.util.github_task_session import GithubTaskManifest
from augur.tasks.github.util.github_random_key_auth import GithubRandomKeyAuth
from augur.application.db.lib import get_session, get_repo_by_repo_git, bulk_insert_dicts, get_pull_request_reviews_by_repo_id, batch_insert_contributors
from augur.application.db.util import execute_session_query
from ..messages import process_github_comment_contributors
from augur.application.db.lib import get_secondary_data_last_collected, get_updated_prs, get_core_data_last_collected

from typing import Generator, List, Dict


platform_id = 1

@celery.task(base=AugurCoreRepoCollectionTask)
def collect_pull_requests(repo_git: str, full_collection: bool) -> int:

    logger = logging.getLogger(collect_pull_requests.__name__)

    with GithubTaskManifest(logger) as manifest:

        augur_db = manifest.augur_db

        repo_id = augur_db.session.query(Repo).filter(
        Repo.repo_git == repo_git).one().repo_id

        owner, repo = get_owner_repo(repo_git)

        if full_collection:
            core_data_last_collected = None
        else:
            # subtract 2 days to ensure all data is collected 
            core_data_last_collected = (get_core_data_last_collected(repo_id) - timedelta(days=2)).replace(tzinfo=timezone.utc)

        total_count = 0
        all_data = []
        for pr in retrieve_all_pr_data(repo_git, logger, manifest.key_auth, core_data_last_collected):
            
            all_data.append(pr)

            if len(all_data) >= 1000:
                process_pull_requests(all_data, f"{owner}/{repo}: Github Pr task", repo_id, logger, augur_db)
                total_count += len(all_data)
                all_data.clear()

        if len(all_data):
            process_pull_requests(all_data, f"{owner}/{repo}: Github Pr task", repo_id, logger, augur_db)
            total_count += len(all_data)

        if total_count > 0:
            return total_count
        else:
            logger.debug(f"{owner}/{repo} has no pull requests")
            return 0
        
        
    
# TODO: Rename pull_request_reviewers table to pull_request_requested_reviewers
# TODO: Fix column names in pull request labels table
def retrieve_all_pr_data(repo_git: str, logger, key_auth, since): #-> Generator[List[Dict]]:

    owner, repo = get_owner_repo(repo_git)

    logger.debug(f"Collecting pull requests for {owner}/{repo}")

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=all&direction=desc&sort=updated"

    github_data_access = GithubDataAccess(key_auth, logger)

    num_pages = github_data_access.get_resource_page_count(url)

    logger.debug(f"{owner}/{repo}: Retrieving {num_pages} pages of pull requests")

    # returns a generator so this method can be used by doing for x in retrieve_all_pr_data()

    for pr in github_data_access.paginate_resource(url):

        yield pr

        # return if last pr on the page was updated before the since date
        if since and datetime.fromisoformat(pr["updated_at"].replace("Z", "+00:00")).replace(tzinfo=timezone.utc) < since:
            return 

def process_pull_requests(pull_requests, task_name, repo_id, logger, augur_db):
    """
    Parse and insert all retrieved PR data.

    Arguments:
        pull_requests: List of paginated pr endpoint data
        task_name: Name of the calling task and the repo
        repo_id: augur id of the repository
        logger: logging object
        augur_db: sqlalchemy db object
    """
    tool_source = "Pr Task"
    tool_version = "2.0"
    data_source = "Github API"

    pr_dicts, pr_mapping_data, pr_numbers, contributors = extract_data_from_pr_list(pull_requests, repo_id, tool_source, tool_version, data_source)

    # remove duplicate contributors before inserting
    contributors = remove_duplicate_dicts(contributors)

    # insert contributors from these prs
    logger.info(f"{task_name}: Inserting {len(contributors)} contributors")
    augur_db.insert_data(contributors, Contributor, ["cntrb_id"])


    # insert the prs into the pull_requests table. 
    # pr_urls are gloablly unique across github so we are using it to determine whether a pull_request we collected is already in the table
    # specified in pr_return_columns is the columns of data we want returned. This data will return in this form; {"pr_url": url, "pull_request_id": id}
    logger.info(f"{task_name}: Inserting prs of length: {len(pr_dicts)}")
    pr_natural_keys = ["repo_id", "pr_src_id"]
    pr_return_columns = ["pull_request_id", "pr_url"]
    pr_string_fields = ["pr_src_title", "pr_body"]
    pr_return_data = augur_db.insert_data(pr_dicts, PullRequest, pr_natural_keys, 
                            return_columns=pr_return_columns, string_fields=pr_string_fields)

    if pr_return_data is None:
        return


    # loop through the pr_return_data (which is a list of pr_urls 
    # and pull_request_id in dicts) so we can find the labels, 
    # assignees, reviewers, and assignees that match the pr
    pr_label_dicts = []
    pr_assignee_dicts = []
    pr_reviewer_dicts = []
    pr_metadata_dicts = []
    for data in pr_return_data:

        pr_url = data["pr_url"]
        pull_request_id = data["pull_request_id"]

        try:
            other_pr_data = pr_mapping_data[pr_url]
        except KeyError as e:
            logger.info(f"Cold not find other pr data. This should never happen. Error: {e}")


        # add the pull_request_id to the labels, assignees, reviewers, or metadata then add them to a list of dicts that will be inserted soon
        dict_key = "pull_request_id"
        pr_label_dicts += add_key_value_pair_to_dicts(other_pr_data["labels"], dict_key, pull_request_id)
        pr_assignee_dicts += add_key_value_pair_to_dicts(other_pr_data["assignees"], dict_key, pull_request_id)
        pr_reviewer_dicts += add_key_value_pair_to_dicts(other_pr_data["reviewers"], dict_key, pull_request_id)
        pr_metadata_dicts += add_key_value_pair_to_dicts(other_pr_data["metadata"], dict_key, pull_request_id)
        

    logger.info(f"{task_name}: Inserting other pr data of lengths: Labels: {len(pr_label_dicts)} - Assignees: {len(pr_assignee_dicts)} - Reviewers: {len(pr_reviewer_dicts)} - Metadata: {len(pr_metadata_dicts)}")

    # inserting pr labels
    # we are using pr_src_id and pull_request_id to determine if the label is already in the database.
    pr_label_natural_keys = ['pr_src_id', 'pull_request_id']
    pr_label_string_fields = ["pr_src_description"]
    augur_db.insert_data(pr_label_dicts, PullRequestLabel, pr_label_natural_keys, string_fields=pr_label_string_fields)

    # inserting pr assignees
    # we are using pr_assignee_src_id and pull_request_id to determine if the label is already in the database.
    pr_assignee_natural_keys = ['pr_assignee_src_id', 'pull_request_id']
    augur_db.insert_data(pr_assignee_dicts, PullRequestAssignee, pr_assignee_natural_keys)


    # inserting pr requested reviewers
    # we are using pr_src_id and pull_request_id to determine if the label is already in the database.
    pr_reviewer_natural_keys = ["pull_request_id", "pr_reviewer_src_id"]
    augur_db.insert_data(pr_reviewer_dicts, PullRequestReviewer, pr_reviewer_natural_keys)
    
    # inserting pr metadata
    # we are using pull_request_id, pr_head_or_base, and pr_sha to determine if the label is already in the database.
    pr_metadata_natural_keys = ['pull_request_id', 'pr_head_or_base', 'pr_sha']
    pr_metadata_string_fields = ["pr_src_meta_label"]
    augur_db.insert_data(pr_metadata_dicts, PullRequestMeta,
                        pr_metadata_natural_keys, string_fields=pr_metadata_string_fields)


























def process_pull_request_review_contributor(pr_review: dict, tool_source: str, tool_version: str, data_source: str):

    # get contributor data and set pr cntrb_id
    user = pr_review["user"]
    if user is None:
        return None
    
    pr_review_cntrb = extract_needed_contributor_data(user, tool_source, tool_version, data_source)
    pr_review["cntrb_id"] = pr_review_cntrb["cntrb_id"]

    return pr_review_cntrb

@celery.task(base=AugurSecondaryRepoCollectionTask)
def collect_pull_request_review_comments(repo_git: str, full_collection: bool) -> None:

    owner, repo = get_owner_repo(repo_git)

    review_msg_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/comments"

    logger = logging.getLogger(collect_pull_request_review_comments.__name__)
    logger.debug(f"Collecting pull request review comments for {owner}/{repo}")

    repo_id = get_repo_by_repo_git(repo_git).repo_id

    if not full_collection:
        last_collected_date = get_secondary_data_last_collected(repo_id)
        
        if last_collected_date:
            # subtract 2 days to ensure all data is collected 
            core_data_last_collected = (last_collected_date - timedelta(days=2)).replace(tzinfo=timezone.utc)
            review_msg_url += f"?since={core_data_last_collected.isoformat()}"
        else:
            logger.warning(f"core_data_last_collected is NULL for recollection on repo: {repo_git}")

    pr_reviews = get_pull_request_reviews_by_repo_id(repo_id)

    # maps the github pr_review id to the auto incrementing pk that augur stores as pr_review id
    pr_review_id_mapping = {}
    for review in pr_reviews:
        pr_review_id_mapping[review.pr_review_src_id] = review.pr_review_id


    tool_source = "Pr review comment task"
    tool_version = "2.0"
    data_source = "Github API"

    key_auth = GithubRandomKeyAuth(logger)
    github_data_access = GithubDataAccess(key_auth, logger)

    all_raw_pr_review_messages = list(github_data_access.paginate_resource(review_msg_url))

    contributors = []
    for comment in all_raw_pr_review_messages:
        
        _, contributor = process_github_comment_contributors(comment, tool_source, tool_version, data_source)
        if contributor is not None:
            contributors.append(contributor)

    logger.info(f"{owner}/{repo} Pr review messages: Inserting {len(contributors)} contributors")
    batch_insert_contributors(logger, contributors)


    pr_review_comment_dicts = []
    pr_review_msg_mapping_data = {}

    pr_review_comments_len = len(all_raw_pr_review_messages)
    for comment in all_raw_pr_review_messages:

        # pull_request_review_id is required to map it to the correct pr review
        if not comment["pull_request_review_id"]:
            continue

        pr_review_comment_dicts.append(
                                extract_needed_message_data(comment, platform_id, repo_id, tool_source, tool_version, data_source)
        )

        # map github message id to the data that maps it to the pr review
        github_msg_id = comment["id"]
        pr_review_msg_mapping_data[github_msg_id] = comment



    logger.info(f"Inserting {len(pr_review_comment_dicts)} pr review comments")
    message_natural_keys = ["platform_msg_id", "pltfrm_id"]
    message_return_columns = ["msg_id", "platform_msg_id"]
    message_string_fields = ["msg_text"]
    message_return_data = bulk_insert_dicts(logger, pr_review_comment_dicts, Message, message_natural_keys, 
                                            return_columns=message_return_columns, string_fields=message_string_fields)
    if message_return_data is None:
        return


    pr_review_message_ref_insert_data = []
    for data in message_return_data:

        augur_msg_id = data["msg_id"]
        github_msg_id = data["platform_msg_id"]

        comment = pr_review_msg_mapping_data[github_msg_id]
        comment["msg_id"] = augur_msg_id

        github_pr_review_id = comment["pull_request_review_id"]

        try:
            augur_pr_review_id = pr_review_id_mapping[github_pr_review_id]
        except KeyError:
            logger.warning(f"{owner}/{repo}: Could not find related pr review. We were searching for pr review with id: {github_pr_review_id}")
            continue

        pr_review_message_ref = extract_pr_review_message_ref_data(comment, augur_pr_review_id, github_pr_review_id, repo_id, tool_version, data_source)
        pr_review_message_ref_insert_data.append(pr_review_message_ref)


    logger.info(f"Inserting {len(pr_review_message_ref_insert_data)} pr review refs")
    pr_comment_ref_natural_keys = ["pr_review_msg_src_id"]
    pr_review_msg_ref_string_columns = ["pr_review_msg_diff_hunk"]
    bulk_insert_dicts(logger, pr_review_message_ref_insert_data, PullRequestReviewMessageRef, pr_comment_ref_natural_keys, string_fields=pr_review_msg_ref_string_columns)




@celery.task(base=AugurSecondaryRepoCollectionTask)
def collect_pull_request_reviews(repo_git: str, full_collection: bool) -> None:

    logger = logging.getLogger(collect_pull_request_reviews.__name__)

    owner, repo = get_owner_repo(repo_git)

    tool_version = "2.0"
    tool_source = "pull_request_reviews"
    data_source = "Github API"

    repo_id = get_repo_by_repo_git(repo_git).repo_id
    with GithubTaskManifest(logger) as manifest:

        augur_db = manifest.augur_db

        query = augur_db.session.query(Repo).filter(Repo.repo_git == repo_git)
        repo_id = execute_session_query(query, 'one').repo_id

        if full_collection:

            query = augur_db.session.query(PullRequest).filter(PullRequest.repo_id == repo_id).order_by(PullRequest.pr_src_number)
            prs = execute_session_query(query, 'all')
        else:
            last_collected = get_secondary_data_last_collected(repo_id).date()
            prs = get_updated_prs(repo_id, last_collected)

        pr_count = len(prs)

        github_data_access = GithubDataAccess(manifest.key_auth, logger)

        all_pr_reviews = {}
        for index, pr in enumerate(prs):

            pr_number = pr.pr_src_number
            pull_request_id = pr.pull_request_id

            logger.debug(f"{owner}/{repo} Collecting Pr Reviews for pr {index + 1} of {pr_count}")

            pr_review_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/reviews"

            try:
                pr_reviews = list(github_data_access.paginate_resource(pr_review_url))
            except UrlNotFoundException as e:
                logger.warning(e)
                continue

            if pr_reviews:
                all_pr_reviews[pull_request_id] = pr_reviews

        if not list(all_pr_reviews.keys()):
            logger.debug(f"{owner}/{repo} No pr reviews for repo")
            return

        contributors = []
        for pull_request_id, reviews in all_pr_reviews.items():

            for review in reviews:
                contributor = process_pull_request_review_contributor(review, tool_source, tool_version, data_source)
                if contributor:
                    contributors.append(contributor)

            logger.info(f"{owner}/{repo} Pr reviews: Inserting {len(contributors)} contributors")
            augur_db.insert_data(contributors, Contributor, ["cntrb_id"])


        pr_reviews = []
        for pull_request_id, reviews in all_pr_reviews.items():

            for review in reviews:
                
                if "cntrb_id" in review:
                    pr_reviews.append(extract_needed_pr_review_data(review, pull_request_id, repo_id, platform_id, tool_source, tool_version))

            logger.info(f"{owner}/{repo}: Inserting pr reviews of length: {len(pr_reviews)}")
            pr_review_natural_keys = ["pr_review_src_id",]
            augur_db.insert_data(pr_reviews, PullRequestReview, pr_review_natural_keys)














