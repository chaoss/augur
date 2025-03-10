from flask import request, jsonify, redirect, url_for, flash, current_app
import re
from flask_login import current_user, login_required
from augur.application.db.models import Repo, RepoGroup, UserGroup, UserRepo, WorkerOauth
from augur.tasks.frontend import add_github_orgs_and_repos, parse_org_and_repo_name, parse_org_name, add_gitlab_repos
from .utils import *
from ..server import app
from augur.application.db.session import DatabaseSession
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

@app.route('/cache/file/')
@app.route('/cache/file/<path:file>')
def cache(file=None):
    if file is None:
        return redirect(url_for('static', filename="cache"))
    return redirect(url_for('static', filename="cache/" + toCacheFilename(file, False)))

    
def add_existing_org_to_group(session, user_id, group_name, rg_id):

    logger.info("Adding existing org to group")

    group_id = UserGroup.convert_group_name_to_id(session, user_id, group_name)
    if group_id is None:
        return False
    
    repos = session.query(Repo).filter(Repo.repo_group_id == rg_id).all()
    logger.info("Length of repos in org: " + str(len(repos)))
    for repo in repos:
        result = UserRepo.insert(session, repo.repo_id, group_id)
        if not result:
            logger.info("Failed to add repo to group")
    


@app.route('/account/repos/add', methods = ['POST'])
@login_required
def av_add_user_repo():

    print("Adding user repos")

    urls = request.form.get('urls')
    group = request.form.get("group_name")

    if not urls:
        flash("No URLs provided")
        return redirect(url_for("user_settings") + "?section=tracker")
    
    # split on commas, carriage returns, and whitespace
    urls = re.split(r'[,\r\s]+', urls)

    # Remove duplicates and empty strings
    # passing None to fitler removes any 
    # values that don't evaluate to true
    urls = list(filter(None, set(urls)))

    if group == "None":
        group = current_user.login_name + "_default"

    invalid_urls = []

    orgs = []
    repo_urls = []
    gitlab_repo_urls = []
    for url in urls:  

        # matches https://github.com/{org}/ or htts://github.com/{org}
        if (org_name := Repo.parse_github_org_url(url)):
            orgs.append(org_name)

        # matches https://github.com/{org}/{repo}/ or htts://github.com/{org}/{repo}
        elif Repo.parse_github_repo_url(url)[0]:
            repo_urls.append(url)

        # matches /{org}/{repo}/ or /{org}/{repo} or {org}/{repo}/ or {org}/{repo}
        elif (match := parse_org_and_repo_name(url)):
            org, repo = match.groups()
            repo_git = f"https://github.com/{org}/{repo}"
            repo_urls.append(repo_git)
        
        # matches /{org}/ or /{org} or {org}/ or {org}
        elif (match := parse_org_name(url)):
            org_name = match.group(1)
            orgs.append(org_name)

        # matches https://gitlab.com/{org}/{repo}/ or http://gitlab.com/{org}/{repo}
        elif Repo.parse_gitlab_repo_url(url)[0]:

            org_name, repo_name = Repo.parse_gitlab_repo_url(url)
            repo_git = f"https://gitlab.com/{org_name}/{repo_name}"
            
            gitlab_repo_urls.append(repo_git)
        else:
            invalid_urls.append(url)

    

    if orgs or repo_urls:
        repo_urls = [url.lower() for url in repo_urls]
        orgs = [url.lower() for url in orgs]
        flash(f"Adding repos: {repo_urls}")
        flash(f"Adding orgs: {orgs}")
        add_github_orgs_and_repos.si(current_user.user_id, group, orgs, repo_urls).apply_async()

    if gitlab_repo_urls:
        add_gitlab_repos(current_user.user_id, group, gitlab_repo_urls)

    flash("Adding repos and orgs in the background")
            
    return redirect(url_for("user_settings") + "?section=tracker")

@app.route('/account/update', methods = ['POST'])
@login_required
def user_update_password():
    old_password = request.form.get("password")
    new_password = request.form.get("new_password")

    if current_user.update_password(old_password, new_password):
        flash(f"Account {current_user.login_name} successfully updated")
    else:
        flash("An error occurred updating the account")
    
    return redirect(url_for("user_settings"))

@app.route('/account/group/add', methods = ['POST'])
@login_required
def user_add_group():
    group = request.form.get("group_name")

    if not group:
        flash("No group name provided")
    elif current_user.add_group(group):
        flash(f"Successfully added group {group}")
    else:
        flash("An error occurred adding group")
    
    return redirect(url_for("user_settings") + "?section=tracker")

@app.route('/account/group/remove')
@login_required
def user_remove_group():
    group = request.args.get("group_name")

    if not group:
        flash("No group name provided")
    elif current_user.remove_group(group):
        flash(f"Successfully removed group {group}")
    else:
        flash("An error occurred removing group")
    
    return redirect(url_for("user_settings") + "?section=tracker")

@app.route('/account/repo/remove')
@login_required
def user_remove_repo():
    group = request.args.get("group_name")
    repo = request.args.get("repo_id")

    if not repo:
        flash("No repo id provided")
    if not group:
        flash("No group name provided")

    repo = int(repo)

    result = current_user.remove_repo(group, repo)[0]

    if result:
        flash(f"Successfully removed repo {repo} from group {group}")
    else:
        flash("An error occurred removing repo from group")
    
    return redirect(url_for("user_group_view") + f"?group={group}")

@app.route('/account/application/deauthorize')
@login_required
def user_app_deauthorize():
    token = request.args.get("token")

    if not token:
        flash("No application provided")
    elif current_user.invalidate_session(token):
        flash("Successfully deauthorized application")
    else:
        flash("Invalid application token")
    
    return redirect(url_for("user_settings") + "?section=application")

@app.route('/account/application/create', methods = ['POST'])
@login_required
def user_app_create():
    name = request.form.get("app_name")
    url = request.form.get("app_url")

    if not name or not url:
        flash("Must provide app name and redirect URL")
    elif current_user.add_app(name, url):
        flash("Successfully created app")
    else:
        flash("Could not create app")
    
    return redirect(url_for("user_settings") + "?section=application")


""" ----------------------------------------------------------------
Locking request loop:
    This route will lock the current request until the
    report request completes. A json response is guaranteed.
    Assumes that the requested repo exists.
"""
@app.route('/requests/report/wait/<id>')
def wait_for_report_request(id):
    requestReports(id)
    return jsonify(report_requests[id])


@app.route('/admin/worker-oauth-keys')
@login_required
def list_worker_oauth_keys():
    """List all worker OAuth keys.
    
    Returns a JSON response with all worker OAuth keys for external APIs.
    These keys are used by collection workers to interface with external platforms.
    """
    try:
        with DatabaseSession() as session:
            oauth_keys = session.query(WorkerOauth).all()
            keys = [{
                'id': key.oauth_id,
                'name': key.name,
                'platform': key.platform,
                'access_token': key.access_token
            } for key in oauth_keys]
            
            return jsonify({'success': True, 'keys': keys})
    except Exception as e:
        logger.error(f"Error getting worker OAuth keys: {str(e)}")
        return jsonify({'success': False, 'message': str(e)})


@app.route('/admin/worker-oauth-keys', methods=['POST'])
@login_required
def add_worker_oauth_key():
    """Add a new worker OAuth key.
    
    Creates a new worker OAuth key for external APIs like GitHub and GitLab.
    These keys are used by collection workers to fetch data from external platforms.
    """
    try:
        platform = request.form.get('platform', 'github')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        name = request.form.get('name', f"{platform} API Key - {timestamp}")
        access_token = request.form.get('access_token')
        
        if not access_token:
            return jsonify({'success': False, 'message': 'Access token is required'})
        
        new_key = WorkerOauth(
            name=name,
            consumer_key='0',
            consumer_secret='0',
            access_token=access_token,
            access_token_secret='0',
            platform=platform
        )
        
        with DatabaseSession() as session:
            session.add(new_key)
            session.commit()
            key_id = new_key.oauth_id
        
        return jsonify({'success': True, 'key_id': key_id})
    except Exception as e:
        logger.error(f"Error adding worker OAuth key: {str(e)}")
        return jsonify({'success': False, 'message': str(e)})


@app.route('/admin/worker-oauth-keys/<int:key_id>', methods=['DELETE'])
@login_required
def delete_worker_oauth_key(key_id):
    """Delete a worker OAuth key.
    
    Removes a worker OAuth key used for external APIs.
    This endpoint requires the user to be authenticated.
    """
    try:
        with DatabaseSession() as session:
            key = session.query(WorkerOauth).filter(WorkerOauth.oauth_id == key_id).first()
            
            if not key:
                return jsonify({'success': False, 'message': 'OAuth key not found'})
            
            session.delete(key)
            session.commit()
        
        return jsonify({'success': True})
    except Exception as e:
        logger.error(f"Error deleting worker OAuth key: {str(e)}")
        return jsonify({'success': False, 'message': str(e)})
