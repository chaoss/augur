"""
Centralized GitHub API base URL management for GitHub Enterprise support.

This module provides functions to get the GitHub API base URL that works with
both the public GitHub API (api.github.com) and GitHub Enterprise instances.

The base URL can be configured via the 'github_api_base_url' setting in the
'Keys' section of the Augur config.

Example Enterprise URL: https://api.mycompany.ghe.com
"""
from augur.application.db.lib import get_value

# Default GitHub API URL
DEFAULT_GITHUB_API_URL = "https://api.github.com"


def get_github_api_base_url() -> str:
    """Get the configured GitHub API base URL.
    
    Returns:
        The GitHub API base URL from config, or the default public API URL.
    """
    base_url = get_value("Keys", "github_api_base_url")
    if base_url:
        # Remove trailing slash if present
        return base_url.rstrip("/")
    return DEFAULT_GITHUB_API_URL
