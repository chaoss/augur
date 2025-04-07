import time
import random
import logging
import sqlalchemy as s
from sqlalchemy import func 
from sqlalchemy.exc import DataError
from sqlalchemy.dialects import postgresql
from sqlalchemy.exc import OperationalError
from psycopg2.errors import DeadlockDetected
from typing import List, Any, Optional, Union

from augur.application.db.models import Config, Repo, Commit, WorkerOauth, Issue, PullRequest, PullRequestReview, ContributorsAlias,UnresolvedCommitEmail, Contributor, CollectionStatus, UserGroup, RepoGroup
from augur.tasks.util.collection_state import CollectionState
from augur.application.db import get_session, get_engine
from augur.application.db.util import execute_session_query
from augur.application.db.session import remove_duplicates_by_uniques, remove_null_characters_from_list_of_dicts
from .bulk_operations import BulkOperationHandler

logger = logging.getLogger("db_lib")

def convert_type_of_value(config_dict, logger=None):
        
        
    data_type = config_dict["type"]

    if data_type == "str" or data_type is None:
        return config_dict

    if data_type == "int":
        config_dict["value"] = int(config_dict["value"])

    elif data_type == "bool":
        value = config_dict["value"]
        
        if value.lower() == "false":
            config_dict["value"] = False
        else:
            config_dict["value"] = True

    elif data_type == "float":
        config_dict["value"] = float(config_dict["value"])

    else:
        if logger:
            logger.error(f"Need to add support for {data_type} types to config") 
        else:
            print(f"Need to add support for {data_type} types to config")

    return config_dict


def get_section(section_name) -> dict:
    """Get a section of data from the config.

    Args:
        section_name: The name of the section being retrieved

    Returns:
        The section data as a dict
    """
    with get_session() as session:

        query = session.query(Config).filter_by(section_name=section_name)
        section_data = execute_session_query(query, 'all')
        
        section_dict = {}
        for setting in section_data:
            setting_dict = setting.__dict__

            setting_dict = convert_type_of_value(setting_dict, logger)

            setting_name = setting_dict["setting_name"]
            setting_value = setting_dict["value"]

            section_dict[setting_name] = setting_value

        return section_dict


def get_value(section_name: str, setting_name: str) -> Optional[Any]:
    """Get the value of a setting from the config.

    Args:
        section_name: The name of the section that the setting belongs to 
        setting_name: The name of the setting

    Returns:
        The value from config if found, and None otherwise
    """

    with get_session() as session:


        # TODO temporary until added to the DB schema
        if section_name == "frontend" and setting_name == "pagination_offset":
            return 25

        try:
            query = session.query(Config).filter(Config.section_name == section_name, Config.setting_name == setting_name)
            config_setting = execute_session_query(query, 'one')
        except s.orm.exc.NoResultFound:
            return None

        setting_dict = config_setting.__dict__

        setting_dict = convert_type_of_value(setting_dict, logger)

        return setting_dict["value"]
    
    
def execute_sql(sql_text):

    engine = get_engine()

    with engine.begin() as connection:

        return_data = connection.execute(sql_text)  

    return return_data

def fetchall_data_from_sql_text(sql_text):

    engine = get_engine()

    with engine.begin() as connection:

        result = connection.execute(sql_text)
    return [dict(row) for row in result.mappings()]

def get_repo_by_repo_git(repo_git: str):

    with get_session() as session:

        query = session.query(Repo).filter(Repo.repo_git == repo_git)
        repo = execute_session_query(query, 'one')

        return repo
    
def get_repo_by_repo_id(repo_id):

    with get_session() as session:

        query = session.query(Repo).filter(Repo.repo_id == repo_id)
        repo = execute_session_query(query, 'one')

        return repo
    
def get_github_repo_by_src_id(src_id):
    
    with get_session() as session:

        query = session.query(Repo).filter(Repo.repo_src_id == src_id, Repo.repo_git.ilike(f'%https://github.com%'))
        repo = execute_session_query(query, 'first')

        return repo
    
def get_gitlab_repo_by_src_id(src_id):
    
    with get_session() as session:

        query = session.query(Repo).filter(Repo.repo_src_id == src_id, Repo.repo_git.ilike(f'%https://gitlab.com%'))
        repo = execute_session_query(query, 'first')

        return repo
        
    
def remove_working_commits_by_repo_id_and_hashes(repo_id, commit_hashes):

    remove_working_commits = s.sql.text("""DELETE FROM working_commits 
        WHERE repos_id = :repo_id AND working_commit IN :hashes
        """).bindparams(repo_id=repo_id,hashes=tuple(commit_hashes))
    
    execute_sql(remove_working_commits)  

def remove_working_commits_by_repo_id(repo_id):

    remove_working_commits = s.sql.text("""DELETE FROM working_commits WHERE repos_id=:repo_id""").bindparams(repo_id=repo_id)
    execute_sql(remove_working_commits)

def remove_commits_by_repo_id_and_hashes(repo_id, commit_hashes):

    remove_commit = s.sql.text("""DELETE FROM commits
        WHERE repo_id=:repo_id
        AND cmt_commit_hash IN :hashes""").bindparams(repo_id=repo_id,hashes=tuple(commit_hashes))
    execute_sql(remove_commit)


def remove_commits_by_repo_id(repo_id):

    remove_commits = s.sql.text("""DELETE FROM commits WHERE repo_id=:repo_id""").bindparams(repo_id=repo_id)
    execute_sql(remove_commits) 

def get_working_commits_by_repo_id(repo_id):

    query = s.sql.text("""SELECT working_commit FROM working_commits WHERE repos_id=:repo_id
    """).bindparams(repo_id=repo_id)

    try:
        working_commits = fetchall_data_from_sql_text(query)
    except:
        working_commits = []

    return working_commits

def get_missing_commit_message_hashes(repo_id):

    fetch_missing_hashes_sql = s.sql.text("""
    SELECT DISTINCT cmt_commit_hash FROM commits
    WHERE repo_id=:repo_id 
    AND cmt_commit_hash NOT IN 
    (SELECT DISTINCT cmt_hash FROM commit_messages WHERE repo_id=:repo_id);
    """).bindparams(repo_id=repo_id)

    try:
        missing_commit_hashes = fetchall_data_from_sql_text(fetch_missing_hashes_sql)
    except:
        missing_commit_hashes = []
    
    return missing_commit_hashes

def get_worker_oauth_keys(platform: str):

    with get_session() as session:

        results = session.query(WorkerOauth).filter(WorkerOauth.platform == platform).order_by(func.random()).all()

        return [row.access_token for row in results]
    
def get_active_repo_count(collection_type):

    with get_session() as session:
    
        return session.query(CollectionStatus).filter(getattr(CollectionStatus,f"{collection_type}_status" ) == CollectionState.COLLECTING.value).count()


def facade_bulk_insert_commits(logger, records):

    with get_session() as session:

        try:
            session.execute(
                    s.insert(Commit),
                    records,
                )
            session.commit()
        except Exception as e:
            
            if len(records) > 1:
                logger.error(f"Ran into issue when trying to insert commits \n Error: {e}")

                #split list into halves and retry insert until we isolate offending record
                firsthalfRecords = records[:len(records)//2]
                secondhalfRecords = records[len(records)//2:]

                facade_bulk_insert_commits(logger, firsthalfRecords)
                facade_bulk_insert_commits(logger, secondhalfRecords)
            elif len(records) == 1 and isinstance(e,DataError) and "time zone displacement" in f"{e}":
                commit_record = records[0]
                #replace incomprehensible dates with epoch.
                #2021-10-11 11:57:46 -0500
                placeholder_date = "1970-01-01 00:00:15 -0500"

                #Check for improper utc timezone offset
                #UTC timezone offset should be between -14:00 and +14:00

                commit_record['author_timestamp'] = placeholder_date
                commit_record['committer_timestamp'] = placeholder_date

                session.execute(
                    s.insert(Commit),
                    [commit_record],
                )
                session.commit()
            else:
                raise e
            

def bulk_insert_dicts(logger, data: Union[List[dict], dict], table, natural_keys: List[str], 
                     return_columns: Optional[List[str]] = None, 
                     string_fields: Optional[List[str]] = None, 
                     on_conflict_update:bool = True) -> Optional[List[dict]]:
    """
    Improved bulk insert operation using BulkOperationHandler.
    
    Args:
        logger: Logger instance
        data: Data to insert
        table: SQLAlchemy table
        natural_keys: List of natural key columns
        return_columns: Columns to return after insert
        string_fields: String fields that need special handling
        on_conflict_update: Whether to update on conflict
        
    Returns:
        Optional[List[dict]]: Returned data if return_columns specified
    """
    handler = BulkOperationHandler(logger)
    return handler.bulk_insert(
        data, table, natural_keys,
        return_columns, string_fields,
        on_conflict_update
    )



def get_issues_by_repo_id(repo_id):

    with get_session() as session:

        return session.query(Issue).filter(Issue.repo_id == repo_id).all()
    
def get_pull_requests_by_repo_id(repo_id):

    with get_session() as session:

        return session.query(PullRequest).filter(PullRequest.repo_id == repo_id).all()
    
def get_pull_request_reviews_by_repo_id(repo_id):

    with get_session() as session:

        return session.query(PullRequestReview).filter(PullRequestReview.repo_id == repo_id).all()
    
def get_contributor_aliases_by_email(email):

    with get_session() as session:

        return session.query(ContributorsAlias).filter_by(alias_email=email).all()
    
def get_unresolved_commit_emails_by_name(name):

    with get_session() as session:

        return session.query(UnresolvedCommitEmail).filter_by(name=name).all()
 
def get_contributors_by_full_name(full_name):

    with get_session() as session:

        return session.query(Contributor).filter_by(cntrb_full_name=full_name).all()
    
def get_contributors_by_github_user_id(id):

    with get_session() as session:

        # Look into this, where it was used was doing .all() but this query should really only return one
        return session.query(Contributor).filter_by(gh_user_id=id).all()

def update_issue_closed_cntrbs_by_repo_id(repo_id):

    engine = get_engine()

    get_ranked_issues = s.text(f"""
        WITH RankedIssues AS (
            SELECT repo_id, issue_id, cntrb_id, 
                ROW_NUMBER() OVER(PARTITION BY issue_id ORDER BY created_at DESC) AS rn
            FROM issue_events 
            WHERE "action" = 'closed'
        )
                                            
        SELECT issue_id, cntrb_id from RankedIssues where rn=1 and repo_id={repo_id} and cntrb_id is not NULL
    """)

    with engine.connect() as conn:
        result = conn.execute(get_ranked_issues).fetchall()

    update_data = []
    for row in result:
        update_data.append(
            {
            'issue_id': row[0], 
            'cntrb_id': row[1], 
            'repo_id': repo_id
            }
        )

    if update_data:
        with engine.connect() as connection:
            update_stmt = s.text("""
                UPDATE issues
                SET cntrb_id = :cntrb_id
                WHERE issue_id = :issue_id
                AND repo_id = :repo_id
            """)
            connection.execute(update_stmt, update_data)

def get_core_data_last_collected(repo_id):
    
    with get_session() as session:
        try:
           return session.query(CollectionStatus).filter(CollectionStatus.repo_id == repo_id).one().core_data_last_collected 
        except s.orm.exc.NoResultFound:
            return None

def get_secondary_data_last_collected(repo_id):
    
    with get_session() as session:
        try:
           return session.query(CollectionStatus).filter(CollectionStatus.repo_id == repo_id).one().secondary_data_last_collected 
        except s.orm.exc.NoResultFound:
            return None
        
def get_updated_prs(repo_id, since):
    
    with get_session() as session:
        return session.query(PullRequest).filter(PullRequest.repo_id == repo_id, PullRequest.pr_updated_at >= since).order_by(PullRequest.pr_src_number).all()
    
def get_updated_issues(repo_id, since):

    with get_session() as session:
        return session.query(Issue).filter(Issue.repo_id == repo_id, Issue.updated_at >= since).order_by(Issue.gh_issue_number).all()
            


def get_group_by_name(user_id, group_name):


    with get_session() as session:
        
        try:
            user_group = session.query(UserGroup).filter(UserGroup.user_id == user_id, UserGroup.name == group_name).one()
        except s.orm.exc.NoResultFound:
            return None

        return user_group
    
def get_repo_group_by_name(name):


    with get_session() as session:
        
        return  session.query(RepoGroup).filter(RepoGroup.rg_name == name).first()
        