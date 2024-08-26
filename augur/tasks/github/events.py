import logging
import traceback
import sqlalchemy as s
from sqlalchemy.sql import text
from abc import ABC, abstractmethod

from augur.tasks.init.celery_app import celery_app as celery
from augur.tasks.init.celery_app import AugurCoreRepoCollectionTask
from augur.application.db.data_parse import *
from augur.tasks.github.util.github_data_access import GithubDataAccess
from augur.tasks.github.util.github_random_key_auth import GithubRandomKeyAuth
from augur.tasks.github.util.util import get_owner_repo
from augur.tasks.util.worker_util import remove_duplicate_dicts
from augur.application.db.models import PullRequestEvent, IssueEvent, Contributor, CollectionStatus
from augur.application.db.lib import get_repo_by_repo_git, bulk_insert_dicts, get_issues_by_repo_id, get_pull_requests_by_repo_id, update_issue_closed_cntrbs_by_repo_id, get_session, get_engine


platform_id = 1

@celery.task(base=AugurCoreRepoCollectionTask)
def collect_events(repo_git: str):

    logger = logging.getLogger(collect_events.__name__)

    owner, repo = get_owner_repo(repo_git)

    logger.debug(f"Collecting Github events for {owner}/{repo}")

    key_auth = GithubRandomKeyAuth(logger)

    if bulk_events_collection_endpoint_contains_all_data(key_auth, logger, owner, repo):
        collection_strategy = BulkGithubEventCollection(logger)
    else:
        collection_strategy = ThoroughGithubEventCollection(logger)

    collection_strategy.collect(repo_git, key_auth)

def bulk_events_collection_endpoint_contains_all_data(key_auth, logger, owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}/issues/events?per_page=100"

    github_data_access = GithubDataAccess(key_auth, logger)

    page_count = github_data_access.get_resource_page_count(url)

    if page_count > 300:
        raise Exception(f"Either github raised the paginator page limit for things like events and messages, or is_pagination_limited_by_max_github_pages is being used on a resource that does not have a page limit. Url: {url}")

    return page_count != 300

class NotMappableException(Exception):
    pass

class GithubEventCollection(ABC):
    
    def __init__(self, logger):
        self._logger = logger
        self._tool_source = "Github events task"
        self._tool_version = "2.0"
        self._data_source = "Github API"

    @abstractmethod
    def collect(self, repo_git, key_auth):
        pass

    def _insert_issue_events(self, events):
        issue_event_natural_keys = ["issue_id", "issue_event_src_id"]
        bulk_insert_dicts(self._logger, events, IssueEvent, issue_event_natural_keys)

    def _insert_pr_events(self, events):
        pr_event_natural_keys = ["node_id"]
        bulk_insert_dicts(self._logger, events, PullRequestEvent, pr_event_natural_keys)

    def _insert_contributors(self, contributors):
        bulk_insert_dicts(self._logger, contributors, Contributor, ["cntrb_id"])

    def _process_github_event_contributors(self, event):

        if event["actor"]:

            event_cntrb = extract_needed_contributor_data(event["actor"], self._tool_source, self._tool_version, self._data_source)
            event["cntrb_id"] = event_cntrb["cntrb_id"]

        else:
            event["cntrb_id"] = None
            return event, None
        
        return event, event_cntrb

class BulkGithubEventCollection(GithubEventCollection):

    def __init__(self, logger):

        self.task_name = f"Bulk Github Event task"
        self.repo_identifier = ""

        super().__init__(logger)

    def collect(self, repo_git, key_auth):

        repo_obj = get_repo_by_repo_git(repo_git)
        repo_id = repo_obj.repo_id

        owner, repo = get_owner_repo(repo_git)
        self.repo_identifier = f"{owner}/{repo}"

        events = []
        for event in self._collect_events(repo_git, key_auth):
            events.append(event)

            # making this a decent size since process_events retrieves all the issues and prs each time
            if len(events) >= 500:
                self._process_events(events, repo_id)
                events.clear()
    
        if events:
            self._process_events(events, repo_id)
        
    def _collect_events(self, repo_git: str, key_auth):

        owner, repo = get_owner_repo(repo_git)

        url = f"https://api.github.com/repos/{owner}/{repo}/issues/events"
            
        github_data_access = GithubDataAccess(key_auth, self._logger)

        return github_data_access.paginate_resource(url)    

    def _process_events(self, events, repo_id):

        issue_events = []
        pr_events = []
        not_mappable_events = []
        for event in events:

            try:
                if self._is_pr_event(event):
                    pr_events.append(event)
                else:
                    issue_events.append(event)
            except NotMappableException:
                not_mappable_events.append(event)

        self._logger.warning(f"{self.repo_identifier} - {self.task_name}: Unable to map these github events to an issue or pr: {not_mappable_events}")

        self._process_issue_events(issue_events, repo_id)
        self._process_pr_events(pr_events, repo_id)

        update_issue_closed_cntrbs_by_repo_id(repo_id)

    def _process_issue_events(self, issue_events, repo_id):
        
        issue_event_dicts = []
        contributors = []

        issue_url_to_id_map = self._get_map_from_issue_url_to_id(repo_id)

        for event in issue_events:

            event, contributor = self._process_github_event_contributors(event)

            issue_url = event["issue"]["url"]

            try:
                issue_id = issue_url_to_id_map[issue_url]
            except KeyError:
                self._logger.warning(f"{self.repo_identifier} - {self.task_name}: Could not find related issue. We were searching for: {issue_url}")
                continue

            issue_event_dicts.append(
                extract_issue_event_data(event, issue_id, platform_id, repo_id,
                                        self._tool_source, self._tool_version, self._data_source)
            )

            if contributor:
                contributors.append(contributor)

        contributors = remove_duplicate_dicts(contributors)

        self._insert_contributors(contributors)

        self._insert_issue_events(issue_event_dicts)

    def _process_pr_events(self, pr_events, repo_id):
                
        pr_event_dicts = []
        contributors = []

        pr_url_to_id_map = self._get_map_from_pr_url_to_id(repo_id)

        for event in pr_events:

            event, contributor = self._process_github_event_contributors(event)

            pr_url = event["issue"]["pull_request"]["url"]

            try:
                pull_request_id = pr_url_to_id_map[pr_url]
            except KeyError:
                self._logger.warning(f"{self.repo_identifier} - {self.task_name}: Could not find related pr. We were searching for: {pr_url}")
                continue

            pr_event_dicts.append(
                extract_pr_event_data(event, pull_request_id, int(event['issue']["id"]), platform_id, repo_id,
                                    self._tool_source, self._tool_version, self._data_source)
            )

            if contributor:
                contributors.append(contributor)

        contributors = remove_duplicate_dicts(contributors)

        self._insert_contributors(contributors)

        self._insert_pr_events(pr_event_dicts)

    def _get_map_from_pr_url_to_id(self, repo_id):

        pr_url_to_id_map = {}
        prs = get_pull_requests_by_repo_id(repo_id)
        for pr in prs:            
            pr_url_to_id_map[pr.pr_url] = pr.pull_request_id

        return pr_url_to_id_map
    
    def _get_map_from_issue_url_to_id(self, repo_id):

        issue_url_to_id_map = {}
        issues = get_issues_by_repo_id(repo_id)
        for issue in issues:
            issue_url_to_id_map[issue.issue_url] = issue.issue_id

        return issue_url_to_id_map

    def _is_pr_event(self, event):

        if event["issue"] is None:
            raise NotMappableException("Not mappable to pr or issue")

        return event["issue"].get('pull_request', None) != None

class ThoroughGithubEventCollection(GithubEventCollection):

    def __init__(self, logger):
        super().__init__(logger)

    def collect(self, repo_git, key_auth):

        repo_obj = get_repo_by_repo_git(repo_git)
        repo_id = repo_obj.repo_id

        owner, repo = get_owner_repo(repo_git)
        self.repo_identifier = f"{owner}/{repo}"

        self._collect_and_process_issue_events(owner, repo, repo_id, key_auth)
        self._collect_and_process_pr_events(owner, repo, repo_id, key_auth)

    def _collect_and_process_issue_events(self, owner, repo, repo_id, key_auth):

        engine = get_engine()

        with engine.connect() as connection:

            # TODO: Remove src id if it ends up not being needed
            query = text(f"""
                select issue_id as issue_id, gh_issue_number as issue_number, gh_issue_id as gh_src_id  from issues WHERE repo_id={repo_id} order by created_at desc;
            """)

            issue_result = connection.execute(query).fetchall()

        events = []
        contributors = []
        github_data_access = GithubDataAccess(key_auth, self._logger)
        for db_issue in issue_result:
            issue = db_issue._asdict()

            issue_number = issue["issue_number"]

            event_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/events"
            
            for event in github_data_access.paginate_resource(event_url):

                event, contributor = self._process_github_event_contributors(event)

                contributors.append(contributor)

                events.append(
                    extract_issue_event_data(event, issue["issue_id"], platform_id, repo_id,
                                        self._tool_source, self._tool_version, self._data_source)
                )

            if len(events) > 500:
                self._insert_contributors(contributors)
                self._insert_issue_events(events)
                events.clear()
        
        if events:
            self._insert_contributors(contributors)
            self._insert_issue_events(events)
            events.clear()
            

    def _collect_and_process_pr_events(self, owner, repo, repo_id, key_auth):

        engine = get_engine()

        with engine.connect() as connection:

            query = text(f"""
                select pull_request_id, pr_src_number as gh_pr_number, pr_src_id from pull_requests order by pr_created_at desc; from pull_requests WHERE repo_id={repo_id} order by pr_created_at desc;
            """)

            pr_result = connection.execute(query).fetchall()

        events = []
        contributors = []
        github_data_access = GithubDataAccess(key_auth, self._logger)
        for db_pr in pr_result:
            pr = db_pr._asdict()

            pr_number = pr["gh_pr_number"]

            event_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/events"
            
            for event in github_data_access.paginate_resource(event_url):

                event, contributor = self._process_github_event_contributors(event)

                contributors.append(contributor)

                events.append(
                    extract_pr_event_data(event, pr["pull_request_id"], pr["pr_src_id"] , platform_id, repo_id,
                                        self._tool_source, self._tool_version, self._data_source)
                )

            if len(events) > 500:
                self._insert_contributors(contributors)
                self._insert_pr_events(events)
                events.clear()
        
        if events:
            self._insert_contributors(contributors)
            self._insert_pr_events(events)
            events.clear()
