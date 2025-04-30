import logging
import time
import httpx
from typing import Dict, Any, List, Optional, Generator
from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed,
    retry_if_exception,
    RetryError,
)

URL = "https://api.github.com/graphql"


class RatelimitException(Exception):
    """Exception raised when GitHub API rate limit is exceeded."""
    def __init__(
        self,
        response: httpx.Response,
        message: str = "Github Rate limit exceeded"
    ) -> None:
        self.response = response
        super().__init__(message)


class NotFoundException(Exception):
    """Exception raised when a resource is not found."""
    pass


class InvalidDataException(Exception):
    """Exception raised when data is invalid."""
    def __init__(
        self,
        message: str,
        data: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(message)
        self.data = data


class GitHubAPIError(Exception):
    """Exception raised when GitHub API request fails."""
    pass


class RateLimitError(Exception):
    """Exception raised when GitHub API rate limit is exceeded."""
    pass


class GithubGraphQlDataAccess:
    """Class for accessing GitHub's GraphQL API with error handling and retries."""
    
    def __init__(
        self,
        key_manager: Any,
        logger: logging.Logger,
        ignore_not_found_error: bool = False,
    ) -> None:
        self.logger = logger
        self.key_manager = key_manager
        self.ignore_not_found_error = ignore_not_found_error

    def get_resource(
        self,
        query: str,
        variables: Dict[str, Any],
        result_keys: List[str]
    ) -> Dict[str, Any]:
        """Get a single resource from GitHub's GraphQL API."""
        result_json = self.make_request_with_retries(query, variables).json()
        data = self.__extract_data_section(result_keys, result_json)
        return data

    def paginate_resource(
        self,
        query: str,
        variables: Dict[str, Any],
        result_keys: List[str]
    ) -> Generator[Dict[str, Any], None, None]:
        """Get paginated resources from GitHub's GraphQL API."""
        params = {"numRecords": 100, "cursor": None}
        params.update(variables)

        result_json = self.make_request_with_retries(query, params).json()
        data = self.__extract_data_section(result_keys, result_json)

        if self.__get_total_count(data) == 0:
            return

        yield from self.__extract_raw_data_into_list(data)

        while self.__has_next_page(data):
            params["cursor"] = self.__get_next_page_cursor(data)
            result_json = self.make_request_with_retries(query, params).json()
            data = self.__extract_data_section(result_keys, result_json)
            yield from self.__extract_raw_data_into_list(data)

    def execute_query(
        self,
        query: str,
        variables: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute a GraphQL query and return the response."""
        response = self.make_request_with_retries(query, variables)
        return response.json()

    def make_request(
        self,
        query: str,
        variables: Optional[Dict[str, Any]],
        timeout: int = 40
    ) -> httpx.Response:
        """Make a request to GitHub's GraphQL API."""
        with httpx.Client() as client:
            json_dict = {"query": query}
            if variables:
                json_dict["variables"] = variables

            response = client.post(
                url=URL,
                auth=self.key_manager,
                json=json_dict,
                timeout=timeout
            )
            response.raise_for_status()

            if not self.ignore_not_found_error:
                json_response = response.json()
                if (
                    "errors" in json_response
                    and len(json_response["errors"]) > 0
                ):
                    errors = json_response["errors"]
                    not_found_error = self.__find_first_error_of_type(
                        errors,
                        "NOT_FOUND"
                    )
                    if not_found_error:
                        message = not_found_error.get(
                            "message",
                            "Resource not found."
                        )
                        raise NotFoundException(
                            f"Could not find: {message}"
                        )
                    raise Exception(
                        f"Github Graphql Data Access Errors: {errors}"
                    )

            return response

    def make_request_with_retries(
        self,
        query: str,
        variables: Dict[str, Any],
        timeout: int = 100
    ) -> httpx.Response:
        """Make a request with retries to GitHub's GraphQL API."""
        try:
            return self.__make_request_with_retries(query, variables, timeout)
        except RetryError as e:
            raise e.last_attempt.exception()

    @retry(
        stop=stop_after_attempt(10),
        wait=wait_fixed(5),
        retry=retry_if_exception(
            lambda exc: not isinstance(exc, NotFoundException)
        ),
    )
    def __make_request_with_retries(
        self,
        query: str,
        variables: Dict[str, Any],
        timeout: int = 40
    ) -> httpx.Response:
        """Make a request with retries to GitHub's GraphQL API."""
        try:
            return self.make_request(query, variables, timeout)
        except RatelimitException as e:
            self.__handle_github_ratelimit_response(e.response)
            raise e

    def __handle_github_ratelimit_response(
        self,
        response: httpx.Response
    ) -> None:
        """Handle GitHub's rate limit response."""
        headers = response.headers

        if "Retry-After" in headers:
            retry_after = int(headers["Retry-After"])
            self.logger.info(
                "Sleeping for {} seconds due to secondary rate limit "
                "issue.".format(retry_after)
            )
            time.sleep(retry_after)
        elif (
            "X-RateLimit-Remaining" in headers
            and int(headers["X-RateLimit-Remaining"]) == 0
        ):
            current_epoch = int(time.time())
            epoch_when_key_resets = int(headers["X-RateLimit-Reset"])
            key_reset_time = epoch_when_key_resets - current_epoch

            if key_reset_time < 0:
                self.logger.error(
                    "Key reset time was less than 0 setting it to 0. "
                    "The current epoch is {} and the epoch that the key "
                    "resets at is {}".format(
                        current_epoch,
                        epoch_when_key_resets
                    )
                )
                key_reset_time = 0

            self.logger.info(
                "API rate limit exceeded. Sleeping until the key resets "
                "({} seconds)".format(key_reset_time)
            )
            time.sleep(key_reset_time)
        else:
            time.sleep(60)

    def __extract_data_section(
        self,
        keys: List[str],
        json_response: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Extract a section of data from the JSON response."""
        if not json_response:
            raise InvalidDataException("Empty data returned", json_response)

        if "data" not in json_response:
            raise InvalidDataException(
                "'data' key missing from response",
                json_response
            )

        core = json_response["data"]

        for value in keys:
            if core is None:
                raise InvalidDataException(
                    f"Data is None when trying to access {value}",
                    json_response
                )
            core = core[value]

        if core is None:
            return {"edges": [], "pageInfo": {"hasNextPage": False}}

        return core

    def __extract_raw_data_into_list(
        self,
        data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Extract raw data into a list from the response."""
        if "edges" not in data:
            raise InvalidDataException("'edges' key not present in data", data)

        data_list = []
        for edge in data["edges"]:
            if "node" not in edge:
                raise InvalidDataException("'node' key not present in data", data)
            data_list.append(edge["node"])

        return data_list

    def __has_next_page(self, data: Dict[str, Any]) -> bool:
        """Check if there is a next page of data."""
        if "pageInfo" not in data:
            raise InvalidDataException(
                "'pageInfo' key not present in data",
                data
            )

        if "hasNextPage" not in data["pageInfo"]:
            raise InvalidDataException(
                "'hasNextPage' key not present in data",
                data
            )

        if not isinstance(data["pageInfo"]["hasNextPage"], bool):
            raise InvalidDataException(
                "pageInfo.hasNextPage is not a bool",
                data
            )

        return data["pageInfo"]["hasNextPage"]

    def __get_next_page_cursor(self, data: Dict[str, Any]) -> str:
        """Get the cursor for the next page of data."""
        if "pageInfo" not in data:
            raise InvalidDataException(
                "'pageInfo' key not present in data",
                data
            )

        if "endCursor" not in data["pageInfo"]:
            raise InvalidDataException(
                "'endCursor' key not present in data",
                data
            )

        return data["pageInfo"]["endCursor"]

    def __get_total_count(self, data: Dict[str, Any]) -> int:
        """Get the total count of items in the response."""
        if "totalCount" not in data:
            raise InvalidDataException(
                "totalCount key not found in data",
                data
            )

        if data["totalCount"] is None:
            raise InvalidDataException(
                "totalCount is null",
                data
            )

        try:
            return int(data["totalCount"])
        except ValueError as exc:
            raise InvalidDataException(
                "totalCount is not an integer",
                data
            ) from exc

    def __find_first_error_of_type(
        self,
        errors: List[Dict[str, Any]],
        error_type: str
    ) -> Optional[Dict[str, Any]]:
        """Find the first error of a specific type from a list of errors."""
        return next(
            (error for error in errors if error.get('type') == error_type),
            None
        )


def get_pr_files_from_graphql(
    owner: str,
    repo: str,
    pr_number: int,
    client: 'GithubGraphQlDataAccess'
) -> List[Dict[str, Any]]:
    """Get pull request files using GraphQL API."""
    query = """
    query($owner: String!, $repo: String!, $prNumber: Int!) {
        repository(owner: $owner, name: $repo) {
            pullRequest(number: $prNumber) {
                files(first: 100) {
                    edges {
                        node {
                            path
                            additions
                            deletions
                            changeType
                        }
                    }
                }
            }
        }
    }
    """

    variables = {
        "owner": owner,
        "repo": repo,
        "prNumber": pr_number
    }

    try:
        result = client.execute_query(query, variables)
        if not result or "repository" not in result:
            return []

        pr = result["repository"]["pullRequest"]
        if not pr:
            return []

        return pr["files"]["edges"]
    except (GitHubAPIError, RateLimitError):
        raise
    except Exception as e:
        raise GitHubAPIError(f"Failed to get PR files: {str(e)}")
