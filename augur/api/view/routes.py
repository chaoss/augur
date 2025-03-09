"""
Defines the api routes for the augur views
"""
import logging
import math
from datetime import datetime
import secrets
from flask import render_template, request, redirect, url_for, session, flash, jsonify
from .utils import *
from .utils import getSetting, render_module, render_message, renderRepos
from .init import reports
from flask_login import login_user, logout_user, current_user, login_required

from augur.application.db.models import User, Repo, ClientApplication
from .server import LoginException
from augur.application.util import *
from augur.application.db.lib import get_value
from ..server import app, db_session

logger = logging.getLogger(__name__)

# Placeholder functions if not imported
def get_all_repos(session, group=None, batch=None, offset=None):
    """Placeholder for get_all_repos function."""
    return []

def get_all_repos_count(session, group=None):
    """Placeholder for get_all_repos_count function."""
    return 0

# ROUTES -----------------------------------------------------------------------

""" ----------------------------------------------------------------
root:
    This route returns a redirect to the application root, appended
    by the provided path, if any.
"""
@app.route('/root/')
@app.route('/root/<path:path>')
def root(path=""):
    return redirect(getSetting("approot") + path)

""" ----------------------------------------------------------------
logo:
    this route returns a redirect to the application logo associated
    with the provided brand, otherwise the inverted Augur logo if no
    brand is provided.
"""
@app.route('/logo/')
@app.route('/logo/<string:brand>')
def logo(brand=None):
    if brand is None:
        return redirect(url_for('static', filename='img/augur_logo.png'))
    if "augur" in brand:
        return logo(None)
    if "chaoss" in brand:
        return redirect(url_for('static', filename='img/Chaoss_Logo_white.png'))
    return ""

""" ----------------------------------------------------------------
default:
table:
    This is the default landing route, which displays a table view
    of the Augur repositories.
"""
@app.route('/')
@app.route('/repos/views/table')
def repo_table_view():
    try:
        # page is the offset index for pagination
        page = int(request.args.get('page', 1))
        filter = request.args.get('filter', False)
        sort = request.args.get('sort', None)
        group = request.args.get('group', None)
        rev = False
        sort2 = sort
        if sort is not None and sort.startswith("-"):
            sort2 = sort[1:]
            rev = True
        
        repos_count = get_all_repos_count(db_session, group)
        all_repos = get_all_repos(db_session, group, 25, (page - 1) * 25)
        
        return render_module("repos-table", all_repos=all_repos, total=repos_count, filter=filter, page=page)
    except (ValueError, AttributeError, RuntimeError) as e:
        logger.error(f"Error in repo_table_view: {e}")
        return render_template("error.j2", error=str(e))

""" ----------------------------------------------------------------
    This is a card view of the Augur repositories.
"""
@app.route('/repos/views/card')
def repo_card_view():
    try:
        # page is the offset index for pagination
        page = int(request.args.get('page', 1))
        
        repos_count = get_all_repos_count(db_session)
        all_repos = get_all_repos(db_session, None, 25, (page - 1) * 25)
        
        return renderRepos('card', {}, {"all_repos": all_repos, "total": repos_count}, page=page, pageSource="repo_card_view")
    except (ValueError, AttributeError, RuntimeError) as e:
        logger.error(f"Error in repo_card_view: {e}")
        return render_template("error.j2", error=str(e))

""" ----------------------------------------------------------------
    This renders a status/loading page.
"""
@app.route('/collection/status')
def status_view():
    return render_module("status")

""" ----------------------------------------------------------------
    This route performs user authentication.
"""
@app.route('/account/login', methods=['GET', 'POST'])
def user_login():
    # redirect users who are already logged in
    if current_user.is_authenticated:
        return redirect(request.args.get('next', url_for('user_settings')))
    
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        
        if not username or not password:
            flash("Please provide both a username and password.", "error")
            return render_template("login.j2")
        
        try:
            user = User.get_by_login(db_session, username)
            if not user:
                raise LoginException("Invalid username or password")
            
            if not user.check_password(password):
                raise LoginException("Invalid username or password")
            
            login_user(user)
            flash("Login successful", "success")
            return redirect(request.args.get('next', url_for('user_settings')))
        except LoginException as e:
            flash(str(e), "error")
            return render_template("login.j2")
        
    return render_template("login.j2")

""" ----------------------------------------------------------------
    This route ends a user's session.
"""
@app.route('/account/logout')
@login_required
def user_logout():
    logout_user()
    flash("You have been logged out", "success")
    return redirect(url_for('repo_table_view'))

""" ----------------------------------------------------------------
    This route authorizes a 3rd party application to access a
    user's account via the API.
"""
@app.route('/user/authorize')
@login_required
def authorize_user():
    client_id = request.args.get('client_id')
    redirect_uri = request.args.get('redirect_uri')
    
    return render_module("authorization", client_id=client_id, redirect_uri=redirect_uri)

""" ----------------------------------------------------------------
    This route allows a user to delete their account.
"""
@app.route('/account/delete')
@login_required
def user_delete():
    try:
        current_user.delete(db_session)
        logout_user()
        flash("Your account has been deleted", "success")
        return redirect(url_for('repo_table_view'))
    except (ValueError, AttributeError, RuntimeError) as e:
        flash(f"Error deleting account: {e}", "error")
        return redirect(url_for('user_settings'))

""" ----------------------------------------------------------------
settings:
    Under development
"""
@app.route('/account/settings')
@login_required
def user_settings():
    return render_template('settings.j2')


@app.route('/account/api-keys')
@login_required
def api_keys_list():
    """
    Get a list of API keys for the current user.
    """
    try:
        # Query the client applications for the current user to get their API keys
        applications = db_session.query(ClientApplication).filter(
            ClientApplication.user_id == current_user.user_id
        ).all()
        
        keys = []
        for app in applications:
            keys.append({
                'id': app.id,
                'api_key': app.api_key,
                'name': app.name,
                'created_at': app.redirect_url  # Using redirect_url as created_at for demonstration
            })
        
        return jsonify({'success': True, 'keys': keys})
    except (ValueError, AttributeError, RuntimeError) as e:
        logger.error(f"Error getting API keys: {str(e)}")
        return jsonify({'success': False, 'message': str(e)})


@app.route('/account/generate-api-key', methods=['POST'])
@login_required
def generate_api_key():
    """
    Generate a new API key for the current user.
    """
    try:
        # Generate a new API key
        new_key = secrets.token_hex(16)
        
        # Create a new client application with the generated API key
        new_app = ClientApplication(
            id=secrets.token_hex(16),
            api_key=new_key,
            name=f"API Key - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            redirect_url=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            user_id=current_user.user_id
        )
        
        # Add the new application to the database
        db_session.add(new_app)
        db_session.commit()
        
        return jsonify({'success': True, 'api_key': new_key})
    except (ValueError, AttributeError, RuntimeError) as e:
        db_session.rollback()
        logger.error(f"Error generating API key: {str(e)}")
        return jsonify({'success': False, 'message': str(e)})


@app.route('/account/delete-api-key', methods=['POST'])
@login_required
def delete_api_key():
    """
    Delete an API key for the current user.
    """
    try:
        key_id = request.form.get('key_id')
        if not key_id:
            return jsonify({'success': False, 'message': 'No key ID provided'})
        
        # Find the application with the given ID and ensure it belongs to the current user
        app = db_session.query(ClientApplication).filter(
            ClientApplication.id == key_id,
            ClientApplication.user_id == current_user.user_id
        ).first()
        
        if not app:
            return jsonify({'success': False, 'message': 'API key not found or not authorized'})
        
        # Delete the application
        db_session.delete(app)
        db_session.commit()
        
        return jsonify({'success': True})
    except (ValueError, AttributeError, RuntimeError) as e:
        db_session.rollback()
        logger.error(f"Error deleting API key: {str(e)}")
        return jsonify({'success': False, 'message': str(e)})

""" ----------------------------------------------------------------
report page:
    This route returns a report view of the requested repo (by ID).
"""
@app.route('/repos/views/repo/<id>')
def repo_repo_view(id):
    # For some reason, there is no reports definition (shouldn't be possible)
    if reports is None:
        return render_message("Reports are not available", "Augur is unable to obtain report data at this time.")
    
    # Get the repository
    repo = db_session.query(Repo).filter(Repo.repo_id == id).first()
    if repo:
        return render_module("repo-info", repo=repo, reports=reports["pull_request_reports"], issue_reports=reports["issue_reports"])
    
    # Cannot find the repo
    return render_message("Repository not found", f"Augur was unable to locate repository with ID: {id}")

""" ----------------------------------------------------------------
group page:
    This route returns a list of repositories associated with the
    currently logged in user.
"""
@app.route('/user/groups/')
@login_required
def user_groups_view():
    try:
        groups, favorites = current_user.get_groups()
        
        for g in favorites:
            if g in groups:
                groups.remove(g)
        
        # Get the repo counts for all the groups and favorites
        repoGroups = []
        for g in groups:
            repoGroups.append({
                "name": g.name,
                "repos": current_user.get_group_repos(db_session, g.name),
                "favorited": False
            })
        
        favGroups = []
        for g in favorites:
            favGroups.append({
                "name": g.name,
                "repos": current_user.get_group_repos(db_session, g.name),
                "favorited": True
            })
        
        # Sort the groups by name
        repoGroups.sort(key=lambda x: x["name"])
        favGroups.sort(key=lambda x: x["name"])
        
        # Return the page
        return render_module("groups-table", groups=repoGroups, favorites=favGroups)
    except (ValueError, AttributeError, RuntimeError) as e:
        return render_message("Error retrieving groups", str(e))

""" ----------------------------------------------------------------
    This route returns a list of repositories associated with the
    currently logged in user, filtered by group.
"""
@app.route('/user/group/<group>')
@login_required
def user_group_view(group = None):
    try:
        if group is None:
            return redirect(url_for('user_groups_view'))
        
        # page is the offset index for pagination
        page = int(request.args.get('page', 1))
        
        # Get the repos by group
        group_repos = current_user.get_group_repos(db_session, group)
        
        return render_module("user-group-repos-table", repos=group_repos, group=group, page=page)
    except (ValueError, AttributeError, RuntimeError) as e:
        return render_message("Error retrieving repositories", str(e))

""" ----------------------------------------------------------------
    This route immediately throws an Exception (for testing)
"""
@app.route('/error')
def throw_exception():
    import sys
    raise Exception(f"Requested test exception (Python{sys.version})")

""" ----------------------------------------------------------------
    This route displays a dashboard for analyzing the current state
    of the Augur application.
"""
@app.route('/dashboard')
def dashboard_view():
    # If we don't have admin privileges, deny the request
    if not current_user.is_authenticated or not current_user.admin:
        return render_message("Access Denied", "You need to be an administrator in order to access the application dashboard.")
    
    requestData = request.json
    if requestData:
        # request format: {"command": "...", args:{...}}
        pass
    
    return render_module("admin-dashboard")
