#SPDX-License-Identifier: MIT
"""
Utility functions for handling contributor data across different forge platforms.

Provides helpers to map contributor data to correct forge-specific database columns
(gh_* for GitHub, gl_* for GitLab) to prevent cross-contamination (issue #3469).

Key functions:
- get_contributor_column_mapping(): Get column mappings for a forge type
- map_contributor_data(): Map API data to database columns
- validate_contributor_data(): Ensure correct column usage
"""

import logging
from typing import Dict, Optional, List


class UnsupportedForgeError(Exception):
    """Raised when an unsupported forge type is specified."""
    pass


def get_contributor_column_mapping(forge_type: str) -> Dict[str, str]:
    """
    Get mapping of generic fields to forge-specific database columns.
    
    Args:
        forge_type: 'github' or 'gitlab'
            
    Returns:
        Dict mapping generic names (e.g., 'user_id') to column names (e.g., 'gh_user_id' or 'gl_id')
            
    Raises:
        UnsupportedForgeError: If forge_type is not supported
    """
    
    # Normalize forge type to lowercase for case-insensitive comparison
    forge_type_lower = forge_type.lower().strip()
    
    # GitHub column mapping
    if forge_type_lower == "github":
        return {
            # Primary identifiers
            'user_id': 'gh_user_id',
            'login': 'gh_login',
            
            # URLs and profile information
            'url': 'gh_url',
            'html_url': 'gh_html_url',
            'avatar_url': 'gh_avatar_url',
            'web_url': 'gh_url',  # Alias for consistency
            
            # Additional GitHub-specific fields
            'node_id': 'gh_node_id',
            'gravatar_id': 'gh_gravatar_id',
            'followers_url': 'gh_followers_url',
            'following_url': 'gh_following_url',
            'gists_url': 'gh_gists_url',
            'starred_url': 'gh_starred_url',
            'subscriptions_url': 'gh_subscriptions_url',
            'organizations_url': 'gh_organizations_url',
            'repos_url': 'gh_repos_url',
            'events_url': 'gh_events_url',
            'received_events_url': 'gh_received_events_url',
            'type': 'gh_type',
            'site_admin': 'gh_site_admin',
            
            # GitLab columns should be None for GitHub data
            'state': None,  # GitLab-specific
            'username': 'gh_login',  # Map to login for consistency
        }
    
    # GitLab column mapping
    elif forge_type_lower == "gitlab":
        return {
            # Primary identifiers
            'user_id': 'gl_id',
            'id': 'gl_id',
            'login': 'gl_username',
            'username': 'gl_username',
            
            # URLs and profile information
            'url': 'gl_web_url',
            'web_url': 'gl_web_url',
            'avatar_url': 'gl_avatar_url',
            
            # GitLab-specific fields
            'state': 'gl_state',
            'full_name': 'gl_full_name',
            'name': 'gl_full_name',
            
            # GitHub columns should be None for GitLab data
            'html_url': None,  # GitHub-specific
            'node_id': None,  # GitHub-specific
            'gravatar_id': None,  # GitHub-specific
            'followers_url': None,  # GitHub-specific
            'following_url': None,  # GitHub-specific
            'gists_url': None,  # GitHub-specific
            'starred_url': None,  # GitHub-specific
            'subscriptions_url': None,  # GitHub-specific
            'organizations_url': None,  # GitHub-specific
            'repos_url': None,  # GitHub-specific
            'events_url': None,  # GitHub-specific
            'received_events_url': None,  # GitHub-specific
            'type': None,  # GitHub-specific
            'site_admin': None,  # GitHub-specific
        }
    
    # Unsupported forge type
    else:
        supported_forges = ["github", "gitlab"]
        raise UnsupportedForgeError(
            f"Unsupported forge type: '{forge_type}'. "
            f"Supported forge types are: {', '.join(supported_forges)}"
        )


def get_null_columns_for_other_forges(forge_type: str) -> Dict[str, None]:
    """
    Get columns that should be NULL for other platforms.
    
    Args:
        forge_type: 'github' or 'gitlab'
        
    Returns:
        Dict with other platform's columns set to None
    """
    
    forge_type_lower = forge_type.lower().strip()
    
    if forge_type_lower == "github":
        # Return all GitLab columns as None
        return {
            'gl_id': None,
            'gl_username': None,
            'gl_web_url': None,
            'gl_avatar_url': None,
            'gl_state': None,
            'gl_full_name': None,
        }
    
    elif forge_type_lower == "gitlab":
        # Return all GitHub columns as None
        return {
            'gh_user_id': None,
            'gh_login': None,
            'gh_url': None,
            'gh_html_url': None,
            'gh_node_id': None,
            'gh_avatar_url': None,
            'gh_gravatar_id': None,
            'gh_followers_url': None,
            'gh_following_url': None,
            'gh_gists_url': None,
            'gh_starred_url': None,
            'gh_subscriptions_url': None,
            'gh_organizations_url': None,
            'gh_repos_url': None,
            'gh_events_url': None,
            'gh_received_events_url': None,
            'gh_type': None,
            'gh_site_admin': None,
        }
    
    else:
        supported_forges = ["github", "gitlab"]
        raise UnsupportedForgeError(
            f"Unsupported forge type: '{forge_type}'. "
            f"Supported forge types are: {', '.join(supported_forges)}"
        )


def map_contributor_data(contributor_data: Dict, forge_type: str) -> Dict:
    """
    Map contributor data from API response to database columns based on forge type.
    
    This is a convenience function that automatically applies the correct column mapping
    and sets other forge columns to None.
    
    Args:
        contributor_data (Dict): Raw contributor data from API response
        forge_type (str): The type of forge platform ("github", "gitlab", etc.)
        
    Returns:
        Dict: Mapped contributor data ready for database insertion
        
    Raises:
        UnsupportedForgeError: If the forge_type is not recognized or supported.
        
    Example:
        >>> gitlab_data = {'id': 123, 'username': 'john', 'avatar_url': 'http://...'}
        >>> mapped = map_contributor_data(gitlab_data, "gitlab")
        >>> print(mapped['gl_id'])
        123
        >>> print(mapped['gl_username'])
        'john'
        >>> print(mapped['gh_user_id'])  # Should be None
        None
    """
    
    mapping = get_contributor_column_mapping(forge_type)
    null_columns = get_null_columns_for_other_forges(forge_type)
    
    result = {}
    
    # Apply the mapping
    for api_field, db_column in mapping.items():
        if db_column is not None and api_field in contributor_data:
            result[db_column] = contributor_data[api_field]
    
    # Add null columns for other forges
    result.update(null_columns)
    
    return result


def get_supported_forge_types() -> list:
    """
    Get a list of all supported forge types.
    
    Returns:
        list: List of supported forge type strings
        
    Example:
        >>> forges = get_supported_forge_types()
        >>> print(forges)
        ['github', 'gitlab']
    """
    return ["github", "gitlab"]


def validate_forge_type(forge_type: str) -> bool:
    """
    Validate if a forge type is supported.
    
    Args:
        forge_type (str): The forge type to validate
        
    Returns:
        bool: True if supported, False otherwise
        
    Example:
        >>> validate_forge_type("github")
        True
        >>> validate_forge_type("bitbucket")
        False
    """
    return forge_type.lower().strip() in get_supported_forge_types()


def validate_contributor_data(contributor_dict: Dict, forge_type: str, logger: Optional[logging.Logger] = None) -> None:
    """
    Validate that contributor data uses the correct forge-specific columns.
    
    This function prevents cross-contamination by ensuring that:
    - GitHub data only populates gh_* columns (gl_* columns should be None)
    - GitLab data only populates gl_* columns (gh_* columns should be None)
    
    This validation helps catch bugs like issue #3469 where GitLab data was
    incorrectly stored in GitHub columns.
    
    Args:
        contributor_dict (Dict): Contributor data dictionary to validate
        forge_type (str): The forge type ('github' or 'gitlab')
        logger (Optional[logging.Logger]): Logger for warnings (creates default if None)
        
    Raises:
        ValueError: If validation fails (wrong columns populated for forge type)
        UnsupportedForgeError: If forge_type is not supported
        
    Example:
        >>> # This should pass
        >>> gitlab_data = {'gl_id': 123, 'gl_username': 'john', 'gh_user_id': None}
        >>> validate_contributor_data(gitlab_data, 'gitlab')
        
        >>> # This should raise ValueError
        >>> bad_data = {'gh_user_id': 123, 'gl_id': None}  # GitHub ID for GitLab data
        >>> validate_contributor_data(bad_data, 'gitlab')  # Raises ValueError!
        
    Note:
        This function is strict - ANY non-None value in the wrong platform's
        columns will trigger a validation error. This is intentional to catch
        subtle bugs early.
    """
    
    # Create logger if not provided
    if logger is None:
        logger = logging.getLogger(__name__)
    
    # Normalize and validate forge type
    forge_type_lower = forge_type.lower().strip()
    if not validate_forge_type(forge_type_lower):
        raise UnsupportedForgeError(
            f"Cannot validate contributor data for unsupported forge type: '{forge_type}'. "
            f"Supported types: {', '.join(get_supported_forge_types())}"
        )
    
    # Define all GitHub and GitLab column names
    github_columns = [
        'gh_user_id', 'gh_login', 'gh_url', 'gh_html_url', 'gh_node_id',
        'gh_avatar_url', 'gh_gravatar_id', 'gh_followers_url', 'gh_following_url',
        'gh_gists_url', 'gh_starred_url', 'gh_subscriptions_url',
        'gh_organizations_url', 'gh_repos_url', 'gh_events_url',
        'gh_received_events_url', 'gh_type', 'gh_site_admin'
    ]
    
    gitlab_columns = [
        'gl_id', 'gl_username', 'gl_web_url', 'gl_avatar_url',
        'gl_state', 'gl_full_name'
    ]
    
    errors: List[str] = []
    warnings: List[str] = []
    
    # Validate based on forge type
    if forge_type_lower == "github":
        # For GitHub data: gh_* columns should be populated, gl_* should be None
        
        # Check that GitLab columns are None or not present
        for col in gitlab_columns:
            if col in contributor_dict and contributor_dict[col] is not None:
                errors.append(
                    f"GitLab column '{col}' is populated (value: {contributor_dict[col]!r}) "
                    f"but forge_type is 'github'. GitLab columns should be None for GitHub data."
                )
        
        # Check that at least some GitHub columns are populated
        github_populated = [col for col in github_columns if col in contributor_dict and contributor_dict[col] is not None]
        if not github_populated:
            warnings.append(
                "No GitHub columns (gh_*) are populated for GitHub data. "
                "This may indicate the data wasn't properly extracted from the API."
            )
        
        # Check for critical GitHub fields
        critical_gh_fields = ['gh_user_id', 'gh_login']
        missing_critical = [f for f in critical_gh_fields if f not in contributor_dict or contributor_dict[f] is None]
        if missing_critical:
            warnings.append(
                f"Critical GitHub fields are missing or None: {', '.join(missing_critical)}. "
                f"GitHub contributors should have at least 'gh_user_id' and 'gh_login' populated."
            )
    
    elif forge_type_lower == "gitlab":
        # For GitLab data: gl_* columns should be populated, gh_* should be None
        
        # Check that GitHub columns are None or not present
        for col in github_columns:
            if col in contributor_dict and contributor_dict[col] is not None:
                errors.append(
                    f"GitHub column '{col}' is populated (value: {contributor_dict[col]!r}) "
                    f"but forge_type is 'gitlab'. GitHub columns should be None for GitLab data. "
                    f"This is the cross-contamination bug from issue #3469!"
                )
        
        # Check that at least some GitLab columns are populated
        gitlab_populated = [col for col in gitlab_columns if col in contributor_dict and contributor_dict[col] is not None]
        if not gitlab_populated:
            warnings.append(
                "No GitLab columns (gl_*) are populated for GitLab data. "
                "This may indicate the data wasn't properly extracted from the API."
            )
        
        # Check for critical GitLab fields
        critical_gl_fields = ['gl_id', 'gl_username']
        missing_critical = [f for f in critical_gl_fields if f not in contributor_dict or contributor_dict[f] is None]
        if missing_critical:
            warnings.append(
                f"Critical GitLab fields are missing or None: {', '.join(missing_critical)}. "
                f"GitLab contributors should have at least 'gl_id' and 'gl_username' populated."
            )
    
    # Check cntrb_login is populated (should be for both platforms)
    if 'cntrb_login' in contributor_dict:
        if contributor_dict['cntrb_login'] is None or contributor_dict['cntrb_login'] == '':
            warnings.append(
                "'cntrb_login' is None or empty. Per schema design, this should be "
                "populated with the platform username for both GitHub and GitLab."
            )
    else:
        warnings.append("'cntrb_login' field is missing from contributor data.")
    
    # Log warnings
    for warning in warnings:
        logger.warning(f"Contributor validation warning: {warning}")
    
    # If we have errors, raise ValueError with all error messages
    if errors:
        error_msg = (
            f"Contributor data validation failed for forge_type='{forge_type}':\n" +
            "\n".join(f"  - {err}" for err in errors) +
            "\n\nThis indicates cross-contamination between GitHub and GitLab columns. "
            "Please ensure the correct column mapping is used for the specified forge type."
        )
        raise ValueError(error_msg)
    
    # Log success if no errors or warnings
    if not warnings:
        logger.debug(
            f"Contributor data validation passed for forge_type='{forge_type}'. "
            f"Columns are correctly segregated."
        )


def validate_contributor_batch(contributors: List[Dict], forge_type: str, logger: Optional[logging.Logger] = None) -> None:
    """
    Validate a batch of contributor data dictionaries.
    
    This is a convenience function to validate multiple contributors at once.
    It will continue checking all contributors even if some fail, then report
    all failures together.
    
    Args:
        contributors (List[Dict]): List of contributor data dictionaries
        forge_type (str): The forge type ('github' or 'gitlab')
        logger (Optional[logging.Logger]): Logger for warnings
        
    Raises:
        ValueError: If any contributor fails validation (reports all failures)
        
    Example:
        >>> contributors = [
        ...     {'gl_id': 1, 'gl_username': 'alice', 'gh_user_id': None},
        ...     {'gl_id': 2, 'gl_username': 'bob', 'gh_user_id': None}
        ... ]
        >>> validate_contributor_batch(contributors, 'gitlab')
    """
    
    if logger is None:
        logger = logging.getLogger(__name__)
    
    failures = []
    
    for i, contributor in enumerate(contributors):
        try:
            validate_contributor_data(contributor, forge_type, logger)
        except ValueError as e:
            failures.append(f"Contributor #{i}: {str(e)}")
        except UnsupportedForgeError:
            # Re-raise immediately for unsupported forge types
            raise
    
    if failures:
        error_msg = (
            f"Batch validation failed for {len(failures)} out of {len(contributors)} contributors:\n" +
            "\n".join(failures)
        )
        raise ValueError(error_msg)
    
    logger.info(
        f"Batch validation passed: All {len(contributors)} contributors have correct "
        f"column usage for forge_type='{forge_type}'"
    )
