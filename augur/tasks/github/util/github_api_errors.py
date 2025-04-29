class GitHubAPIError(Exception):
    """Base exception for GitHub API errors"""
    pass

class RateLimitError(GitHubAPIError):
    """Exception raised when GitHub API rate limit is exceeded"""
    def __init__(self, reset_time: int):
        self.reset_time = reset_time
        super().__init__(f"GitHub API rate limit exceeded. Reset at {reset_time}")

class AuthenticationError(GitHubAPIError):
    """Exception raised when GitHub API authentication fails"""
    pass 