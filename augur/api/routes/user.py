#SPDX-License-Identifier: MIT
"""
Creates routes for user login functionality
"""

import logging
import requests
import json
import os
import base64
import pandas as pd
from flask import request, Response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from augur.application.db.session import DatabaseSession
from augur.tasks.github.util.github_task_session import GithubTaskSession
from augur.util.repo_load_controller import RepoLoadController


from augur.application.db.models import User, UserRepo, UserGroup
from augur.application.config import get_development_flag
logger = logging.getLogger(__name__)
development = get_development_flag()
from augur.application.db.engine import create_database_engine
Session = sessionmaker(bind=create_database_engine())

AUGUR_API_VERSION = 'api/unstable'

""" 
    Extract Bearer token from request header,
    using the standard oauth2 format
"""
def get_bearer_token(request):
    token = request.headers.get("Authorization")

    if token and " " in token:
        token = token.split(" ")
        if len(token) == 2:
            return token[1]

        for substr in token:
            if substr and "Bearer" not in substr:
                return substr
    
    return token

def user_login_required(fun):
    def wrapper(*args, **kwargs):
        # TODO check that user session token is valid

        # We still need to decide on the format for this

        # If valid:
        return fun(*args, **kwargs)

        # else: return error JSON
    
    return wrapper

def api_key_required(fun):
    def wrapper(*args, **kwargs):
        # TODO check that API key is valid

        # If valid:
        return fun(*args, **kwargs)

        # else: return error JSON
    
    return wrapper

# usage:
"""
@app.route("/path")
@api_key_required
@user_login_required
def priviledged_function():
    stuff
"""

# TODO This should probably be available to all endpoints
def generate_upgrade_request():
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/426
    response = jsonify({"status": "SSL Required"})
    response.headers["Upgrade"] = "TLS"
    response.headers["Connection"] = "Upgrade"

    return response, 426

def create_routes(server):
    # TODO This functionality isn't specific to the User endpoints, and should be moved
    @server.app.errorhandler(405)
    def unsupported_method(error):
        return jsonify({"status": "Unsupported method"}), 405

    @server.app.route(f"/{AUGUR_API_VERSION}/user/validate", methods=['POST'])
    def validate_user():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        session = Session()
        username = request.args.get("username")
        password = request.args.get("password")
        if username is None or password is None:
            # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400
            return jsonify({"status": "Missing argument"}), 400

        user = session.query(User).filter(User.login_name == username).first()
        checkPassword = check_password_hash(user.login_hashword, password)
        if user is None:
            return jsonify({"status": "Invalid username"})
        if checkPassword == False:
            return jsonify({"status": "Invalid password"})
        
        # TODO Generate user session token to be stored in client browser

        token = "USER SESSION TOKEN"

        return jsonify({"status": "Validated", "session": token})
    
    @server.app.route(f"/{AUGUR_API_VERSION}/user/oauth", methods=['POST'])
    def oauth_validate():
        # Check if user has an active session
        current_session = request.args.get("session")

        if current_session:
            # TODO validate session token
            # If invalid, set current_session to None to force validation
            pass

        if not current_session:
            return jsonify({"status": "Invalid session"})
        
        # TODO generate oauth token and store in temporary table
        # Ideally should be valid for ~1 minute
        # oauth entry: (token: str, generated: date)

        token = "TEMPORARY VALUE"

        return jsonify({"status": "Validated", "oauth_token": token})

    @server.app.route(f"/{AUGUR_API_VERSION}/user/generate_session", methods=['POST'])
    def generate_session():
        # TODO Validate oauth token
        oauth = request.args.get("oauth_token")

        # If invalid, return error JSON:
        # return jsonify({"status": "Invalid oauth token"})

        # If valid, pop oauth token from temporary table
        # Generate user session token to be stored in client browser

        token = "USER SESSION TOKEN"
        user = "USERNAME"

        return jsonify({"status": "Validated", "username": user, "session": token})
    
    @server.app.route(f"/{AUGUR_API_VERSION}/user/query", methods=['POST'])
    def query_user():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        session = Session()
        username = request.args.get("username")
        if username is None:
            # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400
            return jsonify({"status": "Missing argument"}), 400
        user = session.query(User).filter(User.login_name == username).first()
        
        if user is None:
            return jsonify({"status": "Invalid username"})

        return jsonify({"status": True})

    @server.app.route(f"/{AUGUR_API_VERSION}/user/create", methods=['POST'])
    def create_user():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        session = Session()
        username = request.args.get("username")
        password = request.args.get("password")
        email = request.args.get("email")
        first_name = request.args.get("first_name")
        last_name = request.args.get("last_name")
        admin = request.args.get("create_admin") or False

        if username is None or password is None or email is None:
            # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400
            return jsonify({"status": "Missing argument"}), 400
        user = session.query(User).filter(User.login_name == username).first()
        if user is not None:
            return jsonify({"status": "User already exists"})
        emailCheck = session.query(User).filter(User.email == email).first()
        if emailCheck is not None:
            return jsonify({"status": "Email already exists"})
        try:
            user = User(login_name = username, login_hashword = generate_password_hash(password), email = email, first_name = first_name, last_name = last_name, tool_source="User API", tool_version=None, data_source="API", admin=False)
            session.add(user)
            session.commit()
            return jsonify({"status": "User created"})
        except AssertionError as exception_message: 
            return jsonify(msg='Error: {}. '.format(exception_message)), 400
    
    @server.app.route(f"/{AUGUR_API_VERSION}/user/remove", methods=['POST', 'DELETE'])
    def delete_user():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        session = Session()
        username = request.args.get("username")
        if username is None:
            return jsonify({"status": "Missing argument"}), 400

        user = session.query(User).filter(User.login_name == username).first()
       
        if user is None:
            return jsonify({"status": "User does not exist"})

        for group in user.groups:
            user_repos_list = group.repos

            for user_repo_entry in user_repos_list:
                session.delete(user_repo_entry)

            session.delete(group)

        session.delete(user)
        session.commit()
        return jsonify({"status": "User deleted"}), 200

    @server.app.route(f"/{AUGUR_API_VERSION}/user/update", methods=['POST'])
    def update_user():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        session = Session()
        username = request.args.get("username")
        password = request.args.get("password")
        email = request.args.get("email")
        new_login_name = request.args.get("new_username")
        new_password = request.args.get("new_password")

        if username is None or password is None:
            return jsonify({"status": "Missing argument"}), 400

        user = session.query(User).filter(User.login_name == username).first()
        if user is None:
            return jsonify({"status": "User does not exist"})

        checkPassword = check_password_hash(user.login_hashword, password)
        if checkPassword == False:
            return jsonify({"status": "Invalid password"}) 

        if email is not None:
            existing_user = session.query(User).filter(User.email == email).one()
            if existing_user is not None:
                return jsonify({"status": "Already an account with this email"})

            user.email = email
            session.commit()
            return jsonify({"status": "Email Updated"})

        if new_password is not None:
            user.login_hashword = generate_password_hash(new_password)
            session.commit()
            return jsonify({"status": "Password Updated"})

        if new_login_name is not None:
            existing_user = session.query(User).filter(User.login_name == new_login_name).one()
            if existing_user is not None:
                return jsonify({"status": "Username already taken"})

            user.login_name = new_login_name
            session.commit()
            return jsonify({"status": "Username Updated"})

        return jsonify({"status": "Missing argument"}), 400


    @server.app.route(f"/{AUGUR_API_VERSION}/user/add_repo", methods=['GET', 'POST'])
    def add_user_repo():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        username = request.args.get("username")
        repo = request.args.get("repo_url")
        group_name = request.args.get("group_name")

        with GithubTaskSession(logger) as session:

            if username is None or repo is None or group_name is None:
                return jsonify({"status": "Missing argument"}), 400
            user = session.query(User).filter(
                User.login_name == username).first()
            if user is None:
                return jsonify({"status": "User does not exist"})

            repo_load_controller = RepoLoadController(gh_session=session)

            result = repo_load_controller.add_frontend_repo(repo, user.user_id, group_name)

            return jsonify(result)


    @server.app.route(f"/{AUGUR_API_VERSION}/user/add_group", methods=['GET', 'POST'])
    def add_user_group():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        username = request.args.get("username")
        group_name = request.args.get("group_name")

        if group_name == "default":
            return jsonify({"status": "Reserved Group Name"})
            
        with GithubTaskSession(logger) as session:

            if username is None or group_name is None:
                return jsonify({"status": "Missing argument"}), 400

            user = session.query(User).filter(User.login_name == username).first()
            if user is None:
                return jsonify({"status": "User does not exist"})

            repo_load_controller = RepoLoadController(gh_session=session)

            result = repo_load_controller.add_user_group(user.user_id, group_name)

            return jsonify(result)

    @server.app.route(f"/{AUGUR_API_VERSION}/user/remove_group", methods=['GET', 'POST'])
    def remove_user_group():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        username = request.args.get("username")
        group_name = request.args.get("group_name")
            
        with GithubTaskSession(logger) as session:

            if username is None or group_name is None:
                return jsonify({"status": "Missing argument"}), 400

            user = session.query(User).filter(User.login_name == username).first()
            if user is None:
                return jsonify({"status": "User does not exist"})

            repo_load_controller = RepoLoadController(gh_session=session)

            result = repo_load_controller.remove_user_group(user.user_id, group_name)

            return jsonify(result)

    


    @server.app.route(f"/{AUGUR_API_VERSION}/user/add_org", methods=['GET', 'POST'])
    def add_user_org():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        username = request.args.get("username")
        org = request.args.get("org_url")
        group_name = request.args.get("group_name")

        with GithubTaskSession(logger) as session:

            if username is None or org is None or group_name is None:
                return jsonify({"status": "Missing argument"}), 400

            user = session.query(User).filter(
                User.login_name == username).first()
            if user is None:
                return jsonify({"status": "User does not exist"})

            repo_load_controller = RepoLoadController(gh_session=session)

            result = repo_load_controller.add_frontend_org(org, user.user_id, group_name)

            return jsonify(result)


    @server.app.route(f"/{AUGUR_API_VERSION}/user/remove_repo", methods=['GET', 'POST'])
    def remove_user_repo():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        username = request.args.get("username")
        repo_id = request.args.get("repo_id")
        group_name = request.args.get("group_name")

        with GithubTaskSession(logger) as session:

            if username is None or repo_id is None or group_name is None:
                return jsonify({"status": "Missing argument"}), 400
            user = session.query(User).filter(
                User.login_name == username).first()
            if user is None:
                return jsonify({"status": "User does not exist"})

            repo_load_controller = RepoLoadController(gh_session=session)

            result = repo_load_controller.remove_frontend_repo(repo_id, user.user_id, group_name)

            return jsonify(result)



    @server.app.route(f"/{AUGUR_API_VERSION}/user/group_repos", methods=['GET', 'POST'])
    def group_repos():
        """Select repos from a user group by name

        Arguments
        ----------
        username : str
            The username of the user making the request
        group_name : str
            The name of the group to select
        page : int = 0 -> [>= 0]
            The page offset to use for pagination (optional)
        page_size : int = 25 -> [> 0]
            The number of result per page (optional)
        sort : str
            The name of the column to sort the data by (optional)
        direction : str = "ASC" -> ["ASC" | "DESC"]
            The direction to be used for sorting (optional)

        Returns
        -------
        list
            A list of dictionaries containing repos which match the given arguments
        """

        if not development and not request.is_secure:
            return generate_upgrade_request()

        username = request.args.get("username")
        group_name = request.args.get("group_name")

        # Set default values for ancillary arguments
        page = request.args.get("page") or 0
        page_size = request.args.get("page_size") or 25
        sort = request.args.get("sort")
        direction = request.args.get("direction") or ("ASC" if sort else None)



        if (not username) or (not group_name):
            return jsonify({"status": "Missing argument"}), 400

        if direction and direction != "ASC" and direction != "DESC":
            return jsonify({"status": "Invalid direction"}), 400

        try:
            page = int(page)
            page_size = int(page_size)
        except ValueError:
            return jsonify({"status": "Page size and page should be integers"}), 400

        if page < 0 or page_size < 0:
            return jsonify({"status": "Page size and page should be postive"}), 400


        with DatabaseSession(logger) as session:

            controller = RepoLoadController(session)

            user = session.query(User).filter(User.login_name == username).first()
    
            group_id = controller.convert_group_name_to_id(user.user_id, group_name)
            if group_id is None:
                return jsonify({"status": "Group does not exist"}), 400
            
           
        order_by = sort if sort else "repo_id"
        order_direction = direction if direction else "ASC"

        get_page_of_repos_sql = text(f"""
            SELECT
                    augur_data.repo.repo_id,
                    augur_data.repo.repo_name,
                    augur_data.repo.description,
                    augur_data.repo.repo_git AS url,
                    augur_data.repo.repo_status,
                    a.commits_all_time,
                    b.issues_all_time,
                    rg_name,
                    augur_data.repo.repo_group_id
            FROM
                    augur_data.repo
                    LEFT OUTER JOIN augur_data.api_get_all_repos_commits a ON augur_data.repo.repo_id = a.repo_id
                    LEFT OUTER JOIN augur_data.api_get_all_repos_issues b ON augur_data.repo.repo_id = b.repo_id
                    JOIN augur_operations.user_repos ON augur_data.repo.repo_id = augur_operations.user_repos.repo_id
                    JOIN augur_data.repo_groups ON augur_data.repo.repo_group_id = augur_data.repo_groups.repo_group_id
            WHERE augur_operations.user_repos.group_id = {group_id}
            ORDER BY {order_by} {order_direction}
            LIMIT {page_size}
            OFFSET {page*page_size};
        """)

        results = pd.read_sql(get_page_of_repos_sql, create_database_engine())
        results['url'] = results['url'].apply(lambda datum: datum.split('//')[1])

        b64_urls = []
        for i in results.index:
            b64_urls.append(base64.b64encode((results.at[i, 'url']).encode()))
        results['base64_url'] = b64_urls

        data = results.to_json(orient="records", date_format='iso', date_unit='ms')
        return Response(response=data,
                        status=200,
                        mimetype="application/json")



    @server.app.route(f"/{AUGUR_API_VERSION}/user/group_repo_count", methods=['GET', 'POST'])
    def group_repo_count():
        """Count repos from a user group by name

        Arguments
        ----------
        username : str
            The username of the user making the request
        group_name : str
            The name of the group to select

        Returns
        -------
        int
            A count of the repos in the given user group
        """

        if not development and not request.is_secure:
            return generate_upgrade_request()

        username = request.args.get("username")
        group_name = request.args.get("group_name")

        if (not username) or (not group_name):
            return jsonify({"status": "Missing argument"}), 400

        with DatabaseSession(logger) as session:

            controller = RepoLoadController(session)

            user = session.query(User).filter(User.login_name == username).first()
    
            group_id = controller.convert_group_name_to_id(user.user_id, group_name)
            if group_id is None:
                return jsonify({"status": "Group does not exist"}), 400

            get_page_of_repos_sql = text(f"""
                SELECT
                    count(*)
                FROM
                        augur_data.repo
                        LEFT OUTER JOIN augur_data.api_get_all_repos_commits a ON augur_data.repo.repo_id = a.repo_id
                        LEFT OUTER JOIN augur_data.api_get_all_repos_issues b ON augur_data.repo.repo_id = b.repo_id
                        JOIN augur_operations.user_repos ON augur_data.repo.repo_id = augur_operations.user_repos.repo_id
                        JOIN augur_data.repo_groups ON augur_data.repo.repo_group_id = augur_data.repo_groups.repo_group_id
                WHERE augur_operations.user_repos.group_id = {group_id}
            """)

            result = session.fetchall_data_from_sql_text(get_page_of_repos_sql)
            
            return jsonify({"repos": result[0]["count"]}), 200


    @server.app.route(f"/{AUGUR_API_VERSION}/user/groups", methods=['GET', 'POST'])
    def get_user_groups():
        """Get a list of user groups by username

        Arguments
        ----------
        username : str
            The username of the user making the request

        Returns
        -------
        list
            A list of group names associated with the given username
        """

        if not development and not request.is_secure:
            return generate_upgrade_request()

        username = request.args.get("username")

        if not username:
            return jsonify({"status": "Missing argument"}), 400

        with DatabaseSession(logger) as session:

            controller = RepoLoadController(session)

            user = session.query(User).filter(User.login_name == username).first()
    
            user_groups = controller.get_user_groups(user.user_id)

            group_names = [group.name for group in user_groups]

            return jsonify({"group_names": group_names}), 200

