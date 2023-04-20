import time
import logging


from augur.tasks.init.celery_app import celery_app as celery
from augur.tasks.github.util.github_paginator import GithubPaginator, hit_api, retrieve_dict_from_endpoint
from augur.tasks.github.util.github_task_session import GithubTaskSession, GithubTaskManifest
from augur.tasks.github.util.util import get_owner_repo
from augur.tasks.util.worker_util import remove_duplicate_dicts
from augur.application.db.models import PullRequest, Message, PullRequestReview, PullRequestLabel, PullRequestReviewer, PullRequestEvent, PullRequestMeta, PullRequestAssignee, PullRequestReviewMessageRef, Issue, IssueEvent, IssueLabel, IssueAssignee, PullRequestMessageRef, IssueMessageRef, Contributor, Repo
from augur.tasks.github.facade_github.core import *
from augur.tasks.util.worker_util import create_grouped_task_load
from celery.result import allow_join_result
from augur.application.db.util import execute_session_query
from augur.tasks.git.util.facade_worker.facade_worker.facade00mainprogram import *
from sqlalchemy.orm.exc import NoResultFound


def process_commit_metadata(logger,db,auth,contributorQueue,repo_id,platform_id):

    for contributor in contributorQueue:
        # Get the email from the commit data
        email = contributor['email_raw'] if 'email_raw' in contributor else contributor['email']
    
        name = contributor['name']

        # check the email to see if it already exists in contributor_aliases
        
        # Look up email to see if resolved
        query = db.query(ContributorsAlias).filter_by(alias_email=email)
        alias_table_data = execute_session_query(query, 'all')
        if len(alias_table_data) >= 1:
            # Move on if email resolved
            logger.info(
                f"Email {email} has been resolved earlier.")

            continue
        
        #Check the unresolved_commits table to avoid hitting endpoints that we know don't have relevant data needlessly
        
            
        query = db.query(UnresolvedCommitEmail).filter_by(name=name)
        unresolved_query_result = execute_session_query(query, 'all')

        if len(unresolved_query_result) >= 1:

            logger.info(f"Commit data with email {email} has been unresolved in the past, skipping...")
            continue

        login = None
    
        #Check the contributors table for a login for the given name

        query = db.query(Contributor).filter_by(cntrb_full_name=name)
        contributors_with_matching_name = execute_session_query(query, 'first')

        if not contributors_with_matching_name:
            logger.debug("Failed local login lookup")
        else:
            login = contributors_with_matching_name.gh_login
        

        # Try to get the login from the commit sha
        if login == None or login == "":
            login = get_login_with_commit_hash(logger,db,auth,contributor, repo_id)
    
        if login == None or login == "":
            logger.info("Failed to get login from commit hash")
            # Try to get the login from supplemental data if not found with the commit hash
            login = get_login_with_supplemental_data(logger, db, auth,contributor)
    
        if login == None or login == "":
            logger.error("Failed to get login from supplemental data!")
            continue

        url = ("https://api.github.com/users/" + login)

        user_data, _ = retrieve_dict_from_endpoint(logger, auth, url)

        if user_data == None:
            logger.warning(
                f"user_data was unable to be reached. Skipping...")
            continue

        # Use the email found in the commit data if api data is NULL
        emailFromCommitData = contributor['email_raw'] if 'email_raw' in contributor else contributor['email']


        # Get name from commit if not found by GitHub
        name_field = contributor['commit_name'] if 'commit_name' in contributor else contributor['name']


        cntrb_id = GithubUUID()
        cntrb_id["user"] = int(user_data['id'])
        cntrb_id["platform"] = platform_id

        # try to add contributor to database
        cntrb = {
            "cntrb_id" : cntrb_id.to_UUID(),
            "cntrb_login": user_data['login'],
            "cntrb_created_at": user_data['created_at'],
            "cntrb_email": user_data['email'] if 'email' in user_data else None,
            "cntrb_company": user_data['company'] if 'company' in user_data else None,
            "cntrb_location": user_data['location'] if 'location' in user_data else None,
            # "cntrb_type": , dont have a use for this as of now ... let it default to null
            "cntrb_canonical": user_data['email'] if 'email' in user_data and user_data['email'] is not None else emailFromCommitData,
            "gh_user_id": user_data['id'],
            "gh_login": user_data['login'],
            "gh_url": user_data['url'],
            "gh_html_url": user_data['html_url'],
            "gh_node_id": user_data['node_id'],
            "gh_avatar_url": user_data['avatar_url'],
            "gh_gravatar_id": user_data['gravatar_id'],
            "gh_followers_url": user_data['followers_url'],
            "gh_following_url": user_data['following_url'],
            "gh_gists_url": user_data['gists_url'],
            "gh_starred_url": user_data['starred_url'],
            "gh_subscriptions_url": user_data['subscriptions_url'],
            "gh_organizations_url": user_data['organizations_url'],
            "gh_repos_url": user_data['repos_url'],
            "gh_events_url": user_data['events_url'],
            "gh_received_events_url": user_data['received_events_url'],
            "gh_type": user_data['type'],
            "gh_site_admin": user_data['site_admin'],
            "cntrb_last_used": None if 'updated_at' not in user_data else user_data['updated_at'],
            # Get name from commit if api doesn't get it.
            "cntrb_full_name": name_field if 'name' not in user_data or user_data['name'] is None else user_data['name'],
            #"tool_source": interface.tool_source,
            #"tool_version": interface.tool_version,
            #"data_source": interface.data_source
        }


        
        #Executes an upsert with sqlalchemy 
        cntrb_natural_keys = ['cntrb_login']
        
        db.insert_data(cntrb,Contributor,cntrb_natural_keys)


        try:
            # Update alias after insertion. Insertion needs to happen first so we can get the autoincrementkey
            insert_alias(logger, db,cntrb, emailFromCommitData)
        except LookupError as e:
            logger.info(
                ''.join(traceback.format_exception(None, e, e.__traceback__)))
            logger.info(
                f"Contributor id not able to be found in database despite the user_id existing. Something very wrong is happening. Error: {e}")
            return 
        

        #Replace each instance of a single or double quote with escape characters 
        #for postgres
        escapedEmail = email.replace('"',r'\"')
        escapedEmail = escapedEmail.replace("'",r'\'')
        # Resolve any unresolved emails if we get to this point.
        # They will get added to the alias table later
        # Do this last to absolutely make sure that the email was resolved before we remove it from the unresolved table.
        query = s.sql.text("""
            DELETE FROM unresolved_commit_emails
            WHERE email='{}'
        """.format(escapedEmail))

        logger.info(f"Updating now resolved email {email}")

        try:
            db.execute_sql(query)
        except Exception as e:
            logger.info(
                f"Deleting now resolved email failed with error: {e}")
            raise e
    
        
    return


def link_commits_to_contributor(session,contributorQueue):

    # # iterate through all the commits with emails that appear in contributors and give them the relevant cntrb_id.
    for cntrb in contributorQueue:
        session.logger.debug(
            f"These are the emails and cntrb_id's  returned: {cntrb}")

        query = s.sql.text("""
                UPDATE commits 
                SET cmt_ght_author_id=:cntrb_id
                WHERE 
                (cmt_author_raw_email=:cntrb_email
                OR cmt_author_email=:cntrb_email)
                AND cmt_ght_author_id is NULL
        """).bindparams(cntrb_id=cntrb["cntrb_id"],cntrb_email=cntrb["email"])

        #engine.execute(query, **data)
        session.insert_or_update_data(query)          
        
    
    return


# Update the contributors table from the data facade has gathered.
@celery.task
def insert_facade_contributors(repo_id):

    from augur.tasks.init.celery_app import engine

    logger = logging.getLogger(insert_facade_contributors.__name__)

    with GithubTaskManifest(logger) as manifest:
        

        # Get all of the commit data's emails and names from the commit table that do not appear
        # in the contributors table or the contributors_aliases table.

        manifest.logger.info(
        "Beginning process to insert contributors from facade commits for repo w entry info: {}\n".format(repo_id))
        new_contrib_sql = s.sql.text("""
                SELECT DISTINCT
                    commits.cmt_author_name AS NAME,
                    commits.cmt_commit_hash AS hash,
                    commits.cmt_author_raw_email AS email_raw,
                    'not_unresolved' as resolution_status
                FROM
                    commits
                WHERE
                    commits.repo_id = :repo_id
                    AND (NOT EXISTS ( SELECT contributors.cntrb_canonical FROM contributors WHERE contributors.cntrb_canonical = commits.cmt_author_raw_email )
                    or NOT EXISTS ( SELECT contributors_aliases.alias_email from contributors_aliases where contributors_aliases.alias_email = commits.cmt_author_raw_email)
                    AND ( commits.cmt_author_name ) IN ( SELECT C.cmt_author_name FROM commits AS C WHERE C.repo_id = :repo_id GROUP BY C.cmt_author_name ))
                GROUP BY
                    commits.cmt_author_name,
                    commits.cmt_commit_hash,
                    commits.cmt_author_raw_email
                UNION
                SELECT DISTINCT
                    commits.cmt_author_name AS NAME,--commits.cmt_id AS id,
                    commits.cmt_commit_hash AS hash,
                    commits.cmt_author_raw_email AS email_raw,
                    'unresolved' as resolution_status
                FROM
                    commits
                WHERE
                    commits.repo_id = :repo_id
                    AND EXISTS ( SELECT unresolved_commit_emails.email FROM unresolved_commit_emails WHERE unresolved_commit_emails.email = commits.cmt_author_raw_email )
                    AND ( commits.cmt_author_name ) IN ( SELECT C.cmt_author_name FROM commits AS C WHERE C.repo_id = :repo_id GROUP BY C.cmt_author_name )
                GROUP BY
                    commits.cmt_author_name,
                    commits.cmt_commit_hash,
                    commits.cmt_author_raw_email
                ORDER BY
                hash
        """).bindparams(repo_id=repo_id)

        #Execute statement with session.
        result = manifest.augur_db.execute_sql(new_contrib_sql).fetchall()
        new_contribs = [dict(zip(row.keys(), row)) for row in result]

        #print(new_contribs)

        #json.loads(pd.read_sql(new_contrib_sql, self.db, params={
        #             'repo_id': repo_id}).to_json(orient="records"))



        process_commit_metadata(manifest.logger,manifest.augur_db,manifest.key_auth,list(new_contribs),repo_id,manifest.platform_id)

        manifest.logger.debug("DEBUG: Got through the new_contribs")
    

    with FacadeSession(logger) as session:
        # sql query used to find corresponding cntrb_id's of emails found in the contributor's table
        # i.e., if a contributor already exists, we use it!
        resolve_email_to_cntrb_id_sql = s.sql.text("""
            SELECT DISTINCT
                cntrb_id,
                contributors.cntrb_login AS login,
                contributors.cntrb_canonical AS email,
                commits.cmt_author_raw_email
            FROM
                contributors,
                commits
            WHERE
                contributors.cntrb_canonical = commits.cmt_author_raw_email
                AND commits.repo_id = :repo_id
            UNION
            SELECT DISTINCT
                contributors_aliases.cntrb_id,
                                contributors.cntrb_login as login, 
                contributors_aliases.alias_email AS email,
                commits.cmt_author_raw_email
            FROM
                                contributors,
                contributors_aliases,
                commits
            WHERE
                contributors_aliases.alias_email = commits.cmt_author_raw_email
                                AND contributors.cntrb_id = contributors_aliases.cntrb_id
                AND commits.repo_id = :repo_id
        """).bindparams(repo_id=repo_id)

        #self.logger.info("DEBUG: got passed the sql statement declaration")
        # Get a list of dicts that contain the emails and cntrb_id's of commits that appear in the contributor's table.
        #existing_cntrb_emails = json.loads(pd.read_sql(resolve_email_to_cntrb_id_sql, self.db, params={
        #                                    'repo_id': repo_id}).to_json(orient="records"))

        result = session.execute_sql(resolve_email_to_cntrb_id_sql).fetchall()
        existing_cntrb_emails = [dict(zip(row.keys(), row)) for row in result]

        print(existing_cntrb_emails)
        link_commits_to_contributor(session,list(existing_cntrb_emails))

        session.logger.info("Done with inserting and updating facade contributors")
    return

