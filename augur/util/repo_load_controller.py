import re
import logging

import sqlalchemy as s

from typing import List, Any, Dict


from augur.tasks.github.util.github_paginator import hit_api
from augur.tasks.github.util.github_paginator import GithubPaginator
from augur.tasks.github.util.github_task_session import GithubTaskSession
from augur.application.db.session import DatabaseSession
from augur.application.db.models import Repo, UserRepo, RepoGroup, UserGroup, User
from augur.application.db.util import execute_session_query


logger = logging.getLogger(__name__)

REPO_ENDPOINT = "https://api.github.com/repos/{}/{}"
ORG_REPOS_ENDPOINT = "https://api.github.com/orgs/{}/repos?per_page=100"
DEFAULT_REPO_GROUP_IDS = [1, 10]
CLI_USER_ID = 1

class RepoLoadController:

    def __init__(self, gh_session):
        self.session = gh_session


    def is_valid_repo(self, url: str) -> bool:
        """Determine whether repo url is valid.

        Args:
            url: repo_url

        Returns
            True if repo url is valid and False if not
        """

        owner, repo = self.parse_repo_url(url)
        if not owner or not repo:
            return False

        url = REPO_ENDPOINT.format(owner, repo)

        attempts = 0
        while attempts < 10:
            result = hit_api(self.session.oauths, url, logger)

            # if result is None try again
            if not result:
                attempts+=1
                continue

            # if there was an error return False
            if "message" in result.json().keys():
                return False

            return True


    def retrieve_org_repos(self, url: str) -> List[str]:
        """Get the repos for an org.

        Note:
            If the org url is not valid it will return []

        Args:
            url: org url

        Returns
            List of valid repo urls or empty list if invalid org
        """

        owner = self.parse_org_url(url)
        if not owner:
            # TODO: Change to return empty list so it matches the docs
            return False

        url = ORG_REPOS_ENDPOINT.format(owner)

        repos = []
        with GithubTaskSession(logger) as session:

            for page_data, page in GithubPaginator(url, session.oauths, logger).iter_pages():

                if page_data is None:
                    break

                repos.extend(page_data)

        repo_urls = [repo["html_url"] for repo in repos]

        return repo_urls


    def is_valid_repo_group_id(self, repo_group_id: int) -> bool:
        """Deterime is repo_group_id exists.

        Args:
            repo_group_id: id from the repo groups table

        Returns:
            True if it exists, False if it does not
        """

        query = self.session.query(RepoGroup).filter(RepoGroup.repo_group_id == repo_group_id)

        try:
            result = execute_session_query(query, 'one')
        except (s.orm.exc.NoResultFound, s.orm.exc.MultipleResultsFound):
            return False

        return True

    def add_repo_row(self, url: str, repo_group_id: int, tool_source):
        """Add a repo to the repo table.

        Args:
            url: repo url
            repo_group_id: group to assign repo to

        Note:
            If repo row exists then it will update the repo_group_id if param repo_group_id is not a default. If it does not exist is will simply insert the repo.
        """

        if not isinstance(url, str) or not isinstance(repo_group_id, int) or not isinstance(tool_source, str):
            return None

        if not self.is_valid_repo_group_id(repo_group_id):
            return None

        repo_data = {
            "repo_group_id": repo_group_id,
            "repo_git": url,
            "repo_status": "New",
            "tool_source": tool_source,
            "tool_version": "1.0",
            "data_source": "Git"
        }

        repo_unique = ["repo_git"]
        return_columns = ["repo_id"]
        result = self.session.insert_data(repo_data, Repo, repo_unique, return_columns, on_conflict_update=False)

        if not result:
            return None

        if repo_group_id not in DEFAULT_REPO_GROUP_IDS:
            # update the repo group id
            query = self.session.query(Repo).filter(Repo.repo_git == url)
            repo = execute_session_query(query, 'one')

            if not repo.repo_group_id == repo_group_id:
                repo.repo_group_id = repo_group_id
                self.session.commit()

        return result[0]["repo_id"]


    def add_repo_to_user_group(self, repo_id: int, group_id:int = 1) -> bool:
        """Add a repo to a user in the user_repos table.

        Args:
            repo_id: id of repo from repo table
            user_id: id of user_id from users table
        """

        if not isinstance(repo_id, int) or not isinstance(group_id, int):
            return False

        repo_user_group_data = {
            "group_id": group_id,
            "repo_id": repo_id
        }


        repo_user_group_unique = ["group_id", "repo_id"]
        return_columns = ["group_id", "repo_id"]

        try:
            data = self.session.insert_data(repo_user_group_data, UserRepo, repo_user_group_unique, return_columns)
        except s.exc.IntegrityError:
            return False

        return data[0]["group_id"] == group_id and data[0]["repo_id"] == repo_id

    def add_user_group(self, user_id:int, group_name:str) -> dict:
        """Add a group to the user.

        Args
            user_id: id of the user
            group_name: name of the group being added

        Returns:
            Dict with status key that indicates the success of the operation

        Note:
            If group already exists the function will return that it has been added, but a duplicate group isn't added.
            It simply detects that it already exists and doesn't add it.
        """

        if not isinstance(user_id, int) or not isinstance(group_name, str):
            return {"status": "Invalid input"}

        user_group_data = {
            "name": group_name,
            "user_id": user_id
        }

        try:
            result = self.session.insert_data(user_group_data, UserGroup, ["name", "user_id"], return_columns=["group_id"])
        except s.exc.IntegrityError:
            return {"status": "Error: User id does not exist"}


        if result:
            return {"status": "Group created"}
        else:
            return {"status": "Error while creating group"}

    def remove_user_group(self, user_id: int, group_name: str) -> dict:
        """ Delete a users group of repos.

        Args:
            user_id: id of the user
            group_name: name of the users group

        Returns:
            Dict with a status key that indicates the result of the operation

        """

        # convert group_name to group_id
        group_id = self.convert_group_name_to_id(user_id, group_name)
        if group_id is None:
            return {"status": "WARNING: Trying to delete group that does not exist"}

        group = self.session.query(UserGroup).filter(UserGroup.group_id == group_id).one()

        # delete rows from user repos with group_id
        for repo in group.repos:
            self.session.delete(repo)

        # delete group from user groups table
        self.session.delete(group)

        self.session.commit()

        return {"status": "Group deleted"}


    def convert_group_name_to_id(self, user_id: int, group_name: str) -> int:
        """Convert a users group name to the database group id.

        Args:
            user_id: id of the user
            group_name: name of the users group

        Returns:
            None on failure. The group id on success.

        """

        if not isinstance(user_id, int) or not isinstance(group_name, str):
            return None

        try:
            user_group = self.session.query(UserGroup).filter(UserGroup.user_id == user_id, UserGroup.name == group_name).one()
        except s.orm.exc.NoResultFound:
            return None

        return user_group.group_id

    def get_user_groups(self, user_id: int) -> List:

        return self.session.query(UserGroup).filter(UserGroup.user_id == user_id).all()

    def get_user_group_repos(self, group_id: int) -> List:
        user_repos = self.session.query(UserRepo).filter(UserRepo.group_id == group_id).all()

        return [user_repo.repo for user_repo in user_repos]


    def add_frontend_repo(self, url: List[str], user_id: int, group_name=None, group_id=None, valid_repo=False) -> dict:
        """Add list of repos to a users repos.

        Args:
            urls: list of repo urls
            user_id: id of user_id from users table
            group_name: name of group to add repo to.
            group_id: id of the group
            valid_repo: boolean that indicates whether the repo has already been validated

        Note:
            Either the group_name or group_id can be passed not both

        Returns:
            Dict that contains the key "status" and additional useful data
        """

        if group_name and group_id:
            return {"status": "Pass only the group name or group id not both"}

        if group_id is None:

            group_id = self.convert_group_name_to_id(user_id, group_name)
            if group_id is None:
                return {"status": "Invalid group name"}

        if not valid_repo and not self.is_valid_repo(url):
            return {"status": "Invalid repo", "repo_url": url}

        repo_id = self.add_repo_row(url, DEFAULT_REPO_GROUP_IDS[0], "Frontend")
        if not repo_id:
            return {"status": "Repo insertion failed", "repo_url": url}

        result = self.add_repo_to_user_group(repo_id, group_id)

        if not result:
            return {"status": "repo_user insertion failed", "repo_url": url}

        return {"status": "Repo Added", "repo_url": url}

    def remove_frontend_repo(self, repo_id:int, user_id:int, group_name:str) -> dict:
        """ Remove repo from a users group.

        Args:
            repo_id: id of the repo to remove
            user_id: id of the user
            group_name: name of group the repo is being removed from

        Returns:
            Dict with a key of status that indicates the result of the operation
        """

        if not isinstance(repo_id, int) or not isinstance(user_id, int) or not isinstance(group_name, str):
            return {"status": "Invalid input params"}

        group_id = self.convert_group_name_to_id(user_id, group_name)
        if group_id is None:
            return {"status": "Invalid group name"}

                # delete rows from user repos with group_id
        self.session.query(UserRepo).filter(UserRepo.group_id == group_id, UserRepo.repo_id == repo_id).delete()
        self.session.commit()

        return {"status": "Repo Removed"}


    def add_frontend_org(self, url: List[str], user_id: int, group_name: int):
        """Add list of orgs and their repos to a users repos.

        Args:
            urls: list of org urls
            user_id: id of user_id from users table
        """
        group_id = self.convert_group_name_to_id(user_id, group_name)
        if group_id is None:
            return {"status": "Invalid group name"}

        repos = self.retrieve_org_repos(url)

        if not repos:
            return {"status": "Invalid org", "org_url": url}

        # try to get the repo group with this org name
        # if it does not exist create one
        failed_repos = []
        for repo in repos:

            result = self.add_frontend_repo(repo, user_id, group_id=group_id, valid_repo=True)

            # keep track of all the repos that failed
            if result["status"] != "Repo Added":
                failed_repos.append(repo)

        failed_count = len(failed_repos)
        if failed_count > 0:
            # this should never happen because an org should never return invalid repos
            return {"status": f"{failed_count} repos failed", "repo_urls": failed_repos, "org_url": url}

        return {"status": "Org repos added", "org_url": url}

    def add_cli_repo(self, repo_data: Dict[str, Any], valid_repo=False):
        """Add list of repos to specified repo_groups

        Args:
            url_data: dict with repo_group_id and repo urls
        """

        url = repo_data["url"]
        repo_group_id = repo_data["repo_group_id"]

        if valid_repo or self.is_valid_repo(url):

            # if the repo doesn't exist it adds it
            # if the repo does exist it updates the repo_group_id
            repo_id = self.add_repo_row(url, repo_group_id, "CLI")

            if not repo_id:
                logger.warning(f"Invalid repo group id specified for {url}, skipping.")
                return {"status": f"Invalid repo group id specified for {url}, skipping."}

            self.add_repo_to_user_group(repo_id)

    def add_cli_org(self, org_name):
        """Add list of orgs and their repos to specified repo_groups

        Args:
            org_data: dict with repo_group_id and org urls
        """

        url = f"https://github.com/{org_name}"
        repos = self.retrieve_org_repos(url)

        if not repos:
            print(
                f"No organization with name {org_name} could be found")
            return {"status": "No organization found"}

        # check if the repo group already exists
        query = self.session.query(RepoGroup).filter(RepoGroup.rg_name == org_name)
        rg = execute_session_query(query, 'first')
        if rg:
            print(f"{rg.rg_name} is already a repo group")

            return {"status": "Already a repo group"}

        print(f'Organization "{org_name}" found')

        rg = RepoGroup(rg_name=org_name, rg_description="", rg_website="", rg_recache=0, rg_type="Unknown",
                    tool_source="Loaded by user", tool_version="1.0", data_source="Git")
        self.session.add(rg)
        self.session.commit()
        repo_group_id = rg.repo_group_id
        logger.info(f"{org_name} repo group created")

        for repo_url in repos:
            logger.info(
                f"Adding {repo_url}")
            self.add_cli_repo({"url": repo_url, "repo_group_id": repo_group_id}, valid_repo=True)

        return {"status": "Org added"}


    def get_user_repo_ids(self, user_id: int) -> List[int]:
        """Retrieve a list of repos_id for the given user_id.

        Args:
            user_id: id of the user

        Returns:
            list of repo ids
        """

        user_groups = self.session.query(UserGroup).filter(UserGroup.user_id == user_id).all()

        all_repo_ids = set()
        for group in user_groups:

            repo_ids = [user_repo.repo.repo_id for user_repo in group.repos]
            all_repo_ids.update(repo_ids)


        return list(all_repo_ids)


    def parse_repo_url(self, url: str) -> tuple:
        """ Gets the owner and repo from a url.

        Args:
            url: Github url

        Returns:
            Tuple of owner and repo. Or a tuple of None and None if the url is invalid.
        """

        if url.endswith(".github") or url.endswith(".github.io") or url.endswith(".js"):

            result = re.search(r"https?:\/\/github\.com\/([A-Za-z0-9 \- _]+)\/([A-Za-z0-9 \- _ \.]+)(.git)?\/?$", url)
        else:

            result = re.search(r"https?:\/\/github\.com\/([A-Za-z0-9 \- _]+)\/([A-Za-z0-9 \- _]+)(.git)?\/?$", url)

        if not result:
            return None, None

        capturing_groups = result.groups()


        owner = capturing_groups[0]
        repo = capturing_groups[1]

        return owner, repo

    def parse_org_url(self, url):
        """ Gets the owner from a org url.

        Args:
            url: Github org url

        Returns:
            Org name. Or None if the url is invalid.
        """

        result = re.search(r"https?:\/\/github\.com\/([A-Za-z0-9 \- _]+)\/?$", url)

        if not result:
            return None

        # if the result is not None then the groups should be valid so we don't worry about index errors here
        return result.groups()[0]
