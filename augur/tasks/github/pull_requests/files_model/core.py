import httpx
from typing import List, Dict, Any
from augur.tasks.github.util.github_graphql_data_access import (
    GithubGraphQlDataAccess,
)
from augur.application.db.models import (
    PullRequest,
    Repo,
    PullRequestFile,
)
from augur.application.db.session import DatabaseSession
import logging
from augur.tasks.github.util.github_random_key_auth import GithubRandomKeyAuth
from augur.tasks.github.util.retry import (
    retry_on_exception,
    RateLimitError,
    AuthenticationError,
)
from augur.tasks.github.util.github_api_errors import GitHubAPIError
import sqlalchemy as s
from augur.tasks.github.util.util import get_owner_repo
from augur.application.db.util import execute_session_query
from augur.application.db.lib import get_secondary_data_last_collected, get_updated_prs

logger = logging.getLogger(__name__)


@retry_on_exception(
    retries=3,
    delay=1.0,
    backoff=2.0,
    exceptions=(GitHubAPIError, RateLimitError)
)
def get_pr_files_from_rest_api(
    owner: str,
    repo: str,
    pr_number: int,
    key_auth: GithubRandomKeyAuth
) -> List[Dict[str, Any]]:
    """
    Get PR files using REST API as a fallback

    Args:
        owner: Repository owner
        repo: Repository name
        pr_number: Pull request number
        key_auth: GitHub authentication

    Returns:
        List of files from the PR

    Raises:
        GitHubAPIError: On API errors
        RateLimitError: When rate limit is exceeded
        AuthenticationError: On authentication failure
    """
    url = (
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    )
    headers = {"Accept": "application/vnd.github.v3+json"}

    try:
        client = httpx.Client(auth=key_auth)
        response = client.get(url, headers=headers)
        client.close()

        # Check rate limit
        remaining = int(response.headers.get("X-RateLimit-Remaining", 0))
        reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
        if remaining == 0 or response.status_code == 403:
            raise RateLimitError(reset_time)

        # Handle different status codes
        if response.status_code == 401:
            raise AuthenticationError("Invalid GitHub token")
        elif response.status_code == 404:
            logger.warning(f"PR {pr_number} not found")
            return []
        elif response.status_code == 422:
            logger.warning(f"PR {pr_number} diff not available")
            return []

        response.raise_for_status()
        return response.json()

    except httpx.HTTPError as e:
        raise GitHubAPIError(f"HTTP error occurred: {str(e)}")
    except RateLimitError:
        raise
    except Exception as e:
        raise GitHubAPIError(f"Error getting PR files: {str(e)}")


@retry_on_exception(
    retries=3,
    delay=1.0,
    backoff=2.0,
    exceptions=(GitHubAPIError, RateLimitError)
)
def get_pr_files_from_graphql(
    owner: str,
    repo: str,
    pr_number: int,
    client: GithubGraphQlDataAccess
) -> List[Dict[str, Any]]:
    """
    Get PR files using GraphQL API

    Args:
        owner: Repository owner
        repo: Repository name
        pr_number: Pull request number
        client: GraphQL client

    Returns:
        List of files from the PR

    Raises:
        GitHubAPIError: On API errors
        RateLimitError: When rate limit is exceeded
    """
    query = """
    query($owner: String!, $repo: String!, $pr_number: Int!) {
        repository(owner: $owner, name: $repo) {
            pullRequest(number: $pr_number) {
                files(first: 100) {
                    nodes {
                        path
                        additions
                        deletions
                        changeType
                    }
                }
            }
        }
    }
    """
    variables = {"owner": owner, "repo": repo, "pr_number": pr_number}

    try:
        files = client.paginate_resource(
            query,
            variables,
            ["repository", "pullRequest", "files"]
        )
        if not files:
            logger.warning(f"PR {pr_number} not found in GraphQL")
            return []
        return files
    except Exception as e:
        if "rate limit exceeded" in str(e).lower():
            raise RateLimitError(0)  # GraphQL doesn't provide reset time
        raise GitHubAPIError(f"GraphQL error: {str(e)}")


def collect_pull_request_files(repo_id: int, pr_number: int, key_auth: GithubRandomKeyAuth) -> List[Dict[str, Any]]:
    """
    Collect files for a pull request using both GraphQL and REST APIs

    Args:
        repo_id: Repository ID
        pr_number: Pull request number
        key_auth: GitHub authentication

    Returns:
        List of files from the PR
    """
    try:
        with DatabaseSession() as session:
            # Get PR and repo info
            pr = (
                session.query(PullRequest)
                .filter(
                    PullRequest.repo_id == repo_id,
                    PullRequest.pr_src_number == pr_number,
                )
                .first()
            )

            if not pr:
                logger.warning(f"PR {pr_number} not found in database")
                return []

            repo = session.query(Repo).filter(Repo.repo_id == repo_id).first()
            if not repo:
                logger.warning(f"Repo {repo_id} not found in database")
                return []

            # Extract owner and repo from repo_git
            owner, repo_name = repo.repo_git.split("/")[-2:]
            repo_name = repo_name.replace(".git", "")

            # Try GraphQL first
            graphql_client = GithubGraphQlDataAccess(key_auth, logger)

            files = []
            try:
                files = get_pr_files_from_graphql(
                    owner,
                    repo_name,
                    pr_number,
                    graphql_client
                )
                if not files:
                    logger.warning(
                        "GraphQL returned no files for PR {}, "
                        "trying REST API".format(pr_number)
                    )
                    files = get_pr_files_from_rest_api(
                        owner,
                        repo_name,
                        pr_number,
                        key_auth
                    )
            except (GitHubAPIError, RateLimitError):
                logger.warning(
                    "GraphQL query failed for PR {}, "
                    "falling back to REST API".format(pr_number)
                )
                try:
                    files = get_pr_files_from_rest_api(
                        owner,
                        repo_name,
                        pr_number,
                        key_auth
                    )
                except (GitHubAPIError, RateLimitError):
                    logger.error(
                        "REST API also failed for PR {}".format(pr_number)
                    )
                    return []

            if not files:
                logger.warning(f"No files found for PR {pr_number}")
                return []

            # Process files from either API
            processed_files = []
            for file_data in files:
                if "node" in file_data:  # GraphQL response
                    if not file_data["node"].get("path"):
                        logger.warning(
                            "Skipping file with no path in PR {}".format(
                                pr_number
                            )
                        )
                        continue

                    processed_files.append({
                        'pull_request_id': pr.pull_request_id,
                        'repo_id': repo.repo_id,
                        'pr_file_path': file_data["node"]["path"],
                        'pr_file_additions': file_data["node"]["additions"],
                        'pr_file_deletions': file_data["node"]["deletions"],
                        'tool_source': file_data["node"]["changeType"].lower(),
                        'tool_version': "1.0",
                        'data_source': "GitHub GraphQL API",
                    })
                else:  # REST API response
                    if not file_data.get("filename"):
                        logger.warning(
                            "Skipping file with no filename in PR {}".format(
                                pr_number
                            )
                        )
                        continue

                    status = "modified"
                    if file_data.get("status"):
                        status = file_data["status"].lower()

                    processed_files.append({
                        'pull_request_id': pr.pull_request_id,
                        'repo_id': repo.repo_id,
                        'pr_file_path': file_data["filename"],
                        'pr_file_additions': file_data.get("additions", 0),
                        'pr_file_deletions': file_data.get("deletions", 0),
                        'tool_source': status,
                        'tool_version': "1.0",
                        'data_source': "GitHub REST API",
                    })

            return processed_files

    except Exception as e:
        logger.error(
            "Error processing PR {}: {}".format(pr_number, str(e)),
            exc_info=True
        )
        return []


def pull_request_files_model(repo_id, logger, augur_db, key_auth, full_collection=False):
    """
    Main function to collect PR files for a repository

    Args:
        repo_id: Repository ID
        logger: Logger instance
        augur_db: Database session
        key_auth: GitHub authentication
        full_collection: Whether to collect all PRs or only updated ones
    """
    if full_collection:
        # query existing PRs and the respective url we will append the commits url to
        pr_number_sql = s.sql.text("""
            SELECT DISTINCT pr_src_number as pr_src_number, pull_requests.pull_request_id
            FROM pull_requests
            WHERE repo_id = :repo_id
        """).bindparams(repo_id=repo_id)

        result = augur_db.execute_sql(pr_number_sql)
        pr_numbers = [dict(row) for row in result.mappings()]

    else:
        last_collected = get_secondary_data_last_collected(repo_id).date()
        prs = get_updated_prs(repo_id, last_collected)

        pr_numbers = []
        for pr in prs:
            pr_numbers.append({
                'pr_src_number': pr.pr_src_number,
                'pull_request_id': pr.pull_request_id
            })

    query = augur_db.session.query(Repo).filter(Repo.repo_id == repo_id)
    repo = execute_session_query(query, 'one')
    owner, name = get_owner_repo(repo.repo_git)

    logger.info(f"Getting pull request files for repo: {repo.repo_git}")
    pr_file_rows = []
    
    for index, pr_info in enumerate(pr_numbers):
        logger.info(f'Querying files for pull request #{index + 1} of {len(pr_numbers)}')
        
        files = collect_pull_request_files(
            repo_id,
            pr_info['pr_src_number'],
            key_auth
        )
        
        if files:
            pr_file_rows.extend(files)

    if len(pr_file_rows) > 0:
        # Execute a bulk upsert with sqlalchemy 
        pr_file_natural_keys = ["pull_request_id", "repo_id", "pr_file_path"]
        augur_db.insert_data(pr_file_rows, PullRequestFile, pr_file_natural_keys)
