import logging
from flask import Flask, render_template, render_template_string, request, abort, jsonify, redirect, url_for, session, flash
from sqlalchemy.orm.exc import NoResultFound
from .utils import *
from flask_login import login_user, logout_user, current_user, login_required
# from .server import User
from augur.application.db.models import User
from .server import LoginException
from augur.application.db.session import DatabaseSession

logger = logging.getLogger(__name__)


# ROUTES -----------------------------------------------------------------------

def create_routes(server):
    """ ----------------------------------------------------------------
    root:
        This route returns a redirect to the application root, appended
        by the provided path, if any.
    """
    @server.app.route('/root/')
    @server.app.route('/root/<path:path>')
    def root(path=""):
        return redirect(getSetting("approot") + path)

    """ ----------------------------------------------------------------
    logo:
        this route returns a redirect to the application logo associated
        with the provided brand, otherwise the inverted Augur logo if no
        brand is provided.
    """
    @server.app.route('/logo/')
    @server.app.route('/logo/<string:brand>')
    def logo(brand=None):
        if brand is None:
            return redirect(url_for('static', filename='img/augur_logo.png'))
        elif "augur" in brand:
            return logo(None)
        elif "chaoss" in brand:
            return redirect(url_for('static', filename='img/Chaoss_Logo_white.png'))
        return ""

    """ ----------------------------------------------------------------
    default:
    table:
        This route returns the default view of the application, which
        is currently defined as the repository table view
    """
    @server.app.route('/')
    @server.app.route('/repos/views/table')
    def repo_table_view():
        query = request.args.get('q')
        page = request.args.get('p')
        sorting = request.args.get('s')
        rev = request.args.get('r')
        if rev is not None:
            if rev == "False":
                rev = False
            elif rev == "True":
                rev = True
        else:
            rev = False
        
        if current_user.is_authenticated:
            data = requestJson("repos", cached = False)
            user_repo_ids = current_user.query_repos()
            user_repos = []
            for repo in data:
                if repo["repo_id"] in user_repo_ids:
                    user_repos.append(repo)
            
            data = user_repos or None
        else:
            data = requestJson("repos")

        #if not cacheFileExists("repos.json"):
        #    return renderLoading("repos/views/table", query, "repos.json")

        return renderRepos("table", query, data, sorting, rev, page, True)

    """ ----------------------------------------------------------------
    card:
        This route returns the repository card view
    """
    @server.app.route('/repos/views/card')
    def repo_card_view():
        query = request.args.get('q')
        return renderRepos("card", query, requestJson("repos"), filter = True)

    """ ----------------------------------------------------------------
    groups:
        This route returns the groups table view, listing all the current
        groups in the backend
    """
    @server.app.route('/groups')
    @server.app.route('/groups/<group>')
    def repo_groups_view(group=None):
        query = request.args.get('q')
        page = request.args.get('p')

        if(group is not None):
            query = group

        if(query is not None):
            buffer = []
            data = requestJson("repos")
            for repo in data:
                if query == str(repo["repo_group_id"]) or query in repo["rg_name"]:
                    buffer.append(repo)
            return renderRepos("table", query, buffer, page = page, pageSource = "repo_groups_view")
        else:
            groups = requestJson("repo-groups")
            return render_template('index.html', body="groups-table", title="Groups", groups=groups, query_key=query, api_url=getSetting('serving'))

    """ ----------------------------------------------------------------
    status:
        This route returns the status view, which displays information
        about the current status of collection in the backend
    """
    @server.app.route('/status')
    def status_view():
        return render_module("status", title="Status")

    """ ----------------------------------------------------------------
    login:
        Under development
    """
    @server.app.route('/account/login', methods=['GET', 'POST'])
    def user_login():
        if request.method == 'POST':
            try:
                username = request.form.get('username')
                remember = request.form.get('remember') is not None
                password = request.form.get('password')

                if username is None:
                    raise LoginException("A login issue occurred")

                # test if the user does not exist then the login is invalid
                user = User.get_user(username)
                if not user and request.form.get('register'):
                    raise LoginException("Invalid login credentials")

                # register a user
                if request.form.get('register') is not None:
                    print("Register user")
                    if user:
                        print(f"User already exists: {user.__dict__}")
                        raise LoginException("User already exists")
                    
                    email = request.form.get('email')
                    first_name = request.form.get('first_name')
                    last_name = request.form.get('last_name')
                    admin = request.form.get('admin') or False

                    result = User.create_user(username, password, email, first_name, last_name, admin)
                    if "Error" in result.keys():
                        raise LoginException("An error occurred registering your account")
                    else:
                        user = User.get_user(username)
                        flash(result["status"])

                # Log the user in if the password is valid
                if user.validate(password):

                    result = login_user(user, remember = remember)
                    print(result)
                    flash(f"Welcome, {username}!")
                    if "login_next" in session:
                        return redirect(session.pop("login_next"))
                    return redirect(url_for('root'))
                else:
                    print("Invalid login")
                    raise LoginException("Invalid login credentials")
            except LoginException as e:
                flash(str(e))
        return render_module('login', title="Login")

    """ ----------------------------------------------------------------
    logout:
        Under development
    """
    @server.app.route('/account/logout')
    @login_required
    def user_logout():
        logout_user()
        flash("You have been logged out")
        return redirect(url_for('root'))

    @server.app.route('/account/delete')
    @login_required
    def user_delete():
        if current_user.delete():
            flash(f"Account {current_user.id} successfully removed")
            logout_user()
        else:
            flash("An error occurred removing the account")

        return redirect(url_for("root"))

    @server.app.route('/account/update')
    @login_required
    def user_update_password():
        if current_user.update_password(request):
            flash(f"Account {current_user.id} successfully updated")
        else:
            flash("An error occurred updating the account")
        
        return redirect(url_for("user_settings"))

    """ ----------------------------------------------------------------
    settings:
        Under development
    """
    @server.app.route('/account/settings')
    @login_required
    def user_settings():
        return render_module("settings", title="Settings")

    """ ----------------------------------------------------------------
    report page:
        This route returns a report view of the requested repo (by ID).
    """
    @server.app.route('/repos/views/repo/<id>')
    def repo_repo_view(id):
        # For some reason, there is no reports definition (shouldn't be possible)
        if reports is None:
            return renderMessage("Report Definitions Missing", "You requested a report for a repo on this instance, but a definition for the report layout was not found.")
        data = requestJson("repos")
        repo = {}
        # Need to convert the repo id parameter to int so it's comparable
        try:
            id = int(id)
        except:
            pass
        # Finding the report object in the data so the name is accessible on the page
        for item in data:
            if item['repo_id'] == id:
                repo = item
                break

        return render_module("repo-info", reports=reports.keys(), images=reports, title="Repo", repo=repo, repo_id=id)

    """ ----------------------------------------------------------------
    default:
    table:
        This route returns the default view of the application, which
        is currently defined as the repository table view
    """
    @server.app.route('/user/group/<group>')
    def user_group_view(group):
        params = {}

        # NOT IMPLEMENTED
        # query = request.args.get('q')

        try:
            params["page"] = int(request.args.get('p'))
        except:
            pass

        if sort := request.args.get('s'):
            params["sort"] = sort

        rev = request.args.get('r')
        if rev is not None:
            if rev == "False":
                params["direction"] = "ASC"
            elif rev == "True":
                params["direction"] = "DESC"
        
        if current_user.is_authenticated:
            data = current_user.select_group(group, **params)

            if not data:
                return renderMessage("Error Loading Group", "Either the group you requestion does not exist, or an unspecified error occurred.")
        else:
            return renderMessage("Authentication Required", "You must be logged in to view this page.")

        #if not cacheFileExists("repos.json"):
        #    return renderLoading("repos/views/table", query, "repos.json")

        return renderRepos("table", None, data, sort, rev, params.get("page"), True)

    """ ----------------------------------------------------------------
    Admin dashboard:
        View the admin dashboard.
    """
    @server.app.route('/dashboard')
    def dashboard_view():
        empty = [
            { "title": "Placeholder", "settings": [
                { "id": "empty",
                    "display_name": "Empty Entry",
                    "value": "NULL",
                    "description": "There's nothing here 👻"
                }
            ]}
        ]

        backend_config = requestJson("config/get", False)

        return render_template('admin-dashboard.html', sections = empty, config = backend_config)
