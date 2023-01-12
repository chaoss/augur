#SPDX-License-Identifier: MIT
"""
Creates routes for user functionality
"""

import logging
import requests
import json
import os
import base64
import time
import secrets
import pandas as pd
from flask import request, Response, jsonify, session
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from augur.application.db.session import DatabaseSession
from augur.tasks.github.util.github_task_session import GithubTaskSession
from augur.util.repo_load_controller import RepoLoadController
from augur.api.util import get_bearer_token
from augur.api.util import get_client_token

from augur.application.db.models import User, UserRepo, UserGroup, UserSessionToken, ClientApplication, RefreshToken
from augur.application.config import get_development_flag
from augur.tasks.init.redis_connection import redis_connection as redis

logger = logging.getLogger(__name__)
development = get_development_flag()
from augur.application.db.engine import create_database_engine
Session = sessionmaker(bind=create_database_engine())

from augur.api.routes import AUGUR_API_VERSION

def api_key_required(fun):
    # TODO Optionally rate-limit non authenticated users instead of rejecting requests
    def wrapper(*args, **kwargs):

        client_token = get_client_token()
                    
        # If valid:
        if client_token:

            session = Session()
            try:
                kwargs["application"] = session.query(ClientApplication).filter(ClientApplication.api_key == client_token).one()
                return fun(*args, **kwargs)
            except NoResultFound:
                pass

        return {"status": "Unauthorized client"}
    
    wrapper.__name__ = fun.__name__
    return wrapper

# usage:
"""
@app.route("/path")
@api_key_required
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
        if user is None:
            return jsonify({"status": "Invalid username"})

        checkPassword = check_password_hash(user.login_hashword, password)
        if checkPassword == False:
            return jsonify({"status": "Invalid password"})

        login_user(user)

        return jsonify({"status": "Validated"})

    @server.app.route(f"/{AUGUR_API_VERSION}/user/logout", methods=['POST'])
    @login_required
    def logout_user_func():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        if logout_user():
            return jsonify({"status": "Logged out"})

        return jsonify({"status": "Error when logging out"})

    
    @server.app.route(f"/{AUGUR_API_VERSION}/user/authorize", methods=['POST', 'GET'])
    @login_required
    def user_authorize():
        code = secrets.token_hex()
        username = current_user.login_name

        redis.set(code, username, ex=30)

        return jsonify({"status": "Validated", "code": code})

    @server.app.route(f"/{AUGUR_API_VERSION}/user/session/generate", methods=['POST'])
    @api_key_required
    def generate_session(application):
        if not (code := request.args.get("code")):
            return jsonify({"status": "Invalid authorization code"})
        
        if request.args.get("grant_type") != "code":
            return jsonify({"status": "Invalid grant type"})

        username = redis.get(code)
        redis.delete(code)
        if not username:
            return jsonify({"status": "Invalid authorization code"})

        user = User.get_user(username)
        if not user:
            return jsonify({"status": "Invalid user"})

        user_session_token = secrets.token_hex()
        seconds_to_expire = 86400
        expiration = int(time.time()) + seconds_to_expire

        session = Session()
        user_session = UserSessionToken(token=user_session_token, user_id=user.user_id, application_id = application.id, expiration=expiration)

        refresh_token = RefreshToken.create(user_session_token)

        session.add(user_session)
        session.commit()
        session.close()

        response = jsonify({"status": "Validated", "username": username, "access_token": user_session_token, "refresh_token" : refresh_token.id, "token_type": "Bearer", "expires": seconds_to_expire})
        response.headers["Cache-Control"] = "no-store"

        return response
    
    @server.app.route(f"/{AUGUR_API_VERSION}/user/session/refresh")
    @api_key_required
    def refresh_session():
        refresh_token_str = request.args.get("refresh_token")

        if not refresh_token_str:
            return jsonify({"status": "Invalid refresh token"})
        
        if request.args.get("grant_type") != "refresh_token":
            return jsonify({"status": "Invalid grant type"})

        session = Session()
        refresh_token = session.query(RefreshToken).filter(RefreshToken.id == refresh_token_str).first()
        if not refresh_token:
            return jsonify({"status": "Invalid refresh token"})

        user_session = refresh_token.user_session
        user = user_session.user

        new_user_session = UserSessionToken.create(user.user_id, user_session.application.id)
        new_refresh_token = RefreshToken.create(new_user_session.token)
        
        if refresh_token.delete() != 1:
            return jsonify({"status": "Error deleting refresh token"})

        if user_session.delete() != 1:
            return jsonify({"status": "Error deleting user session"})

        return jsonify({"refresh_token": new_refresh_token.id, "session": new_user_session.token})

    
    @server.app.route(f"/{AUGUR_API_VERSION}/user/query", methods=['POST'])
    def query_user():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        username = request.args.get("username")
        if username is None:
            return jsonify({"status": "Missing argument"}), 400

        if not User.exists(username):
            return jsonify({"status": "Invalid username"})

        return jsonify({"status": True})

    @server.app.route(f"/{AUGUR_API_VERSION}/user/create", methods=['GET', 'POST'])
    def create_user():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        username = request.args.get("username")
        password = request.args.get("password")
        email = request.args.get("email")
        first_name = request.args.get("first_name")
        last_name = request.args.get("last_name")
        admin = request.args.get("create_admin") or False

        result = User.create_user(username, password, email, first_name, last_name, admin)

        return jsonify(result[1])

    
    @server.app.route(f"/{AUGUR_API_VERSION}/user/remove", methods=['POST', 'DELETE'])
    @login_required
    def delete_user():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        status = current_user.delete()
        return jsonify(status)


    @server.app.route(f"/{AUGUR_API_VERSION}/user/update", methods=['POST'])
    @login_required
    def update_user():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        email = request.args.get("email")
        new_login_name = request.args.get("new_username")
        new_password = request.args.get("new_password")

        if email is not None:
            existing_user = session.query(User).filter(User.email == email).one()
            if existing_user is not None:
                return jsonify({"status": "Already an account with this email"})

            current_user.email = email
            session.commit()
            return jsonify({"status": "Email Updated"})

        if new_password is not None:
            current_user.login_hashword = generate_password_hash(new_password)
            session.commit()
            return jsonify({"status": "Password Updated"})

        if new_login_name is not None:
            existing_user = session.query(User).filter(User.login_name == new_login_name).one()
            if existing_user is not None:
                return jsonify({"status": "Username already taken"})

            current_user.login_name = new_login_name
            session.commit()
            return jsonify({"status": "Username Updated"})

        return jsonify({"status": "Missing argument"}), 400


    @server.app.route(f"/{AUGUR_API_VERSION}/user/repo/add", methods=['GET', 'POST'])
    @login_required
    def add_user_repo():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        repo = request.args.get("repo_url")
        group_name = request.args.get("group_name")

        result = current_user.add_repo(group_name, repo)

        return jsonify(result[1])


    @server.app.route(f"/{AUGUR_API_VERSION}/user/group/add", methods=['GET', 'POST'])
    @login_required
    def add_user_group():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        group_name = request.args.get("group_name")

        result = current_user.add_group(group_name)

        return jsonify(result[1])

    @server.app.route(f"/{AUGUR_API_VERSION}/user/group/remove", methods=['GET', 'POST'])
    @login_required
    def remove_user_group():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        group_name = request.args.get("group_name")

        result = current_user.remove_group(group_name)

        return jsonify(result[1])


    @server.app.route(f"/{AUGUR_API_VERSION}/user/org/add", methods=['GET', 'POST'])
    @login_required
    def add_user_org():
        if not development and not request.is_secure:
            return generate_upgrade_request()

        org = request.args.get("org_url")
        group_name = request.args.get("group_name")

        result = current_user.add_org(group_name, org)

        return jsonify(result[1])


    @server.app.route(f"/{AUGUR_API_VERSION}/user/repo/remove", methods=['GET', 'POST'])
    @login_required
    def remove_user_repo():
        if not development and not request.is_secure:
            return generate_upgrade_request()


        group_name = request.args.get("group_name")

        try:
            repo_id = int(request.args.get("repo_id"))
        except TypeError:
            return {"status": "Repo id must be and integer"}

        result = current_user.remove_repo(group_name, repo_id)

        return jsonify(result[1])

    @server.app.route(f"/{AUGUR_API_VERSION}/user/group/repos/", methods=['GET', 'POST'])
    @login_required
    def group_repos():
        """Select repos from a user group by name

        Arguments
        ----------
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

        group_name = request.args.get("group_name")
        page = request.args.get("page") or 0
        page_size = request.args.get("page_size") or 25
        sort = request.args.get("sort") or "repo_id"
        direction = request.args.get("direction") or "ASC"

        result = current_user.get_group_repos(group_name, page, page_size, sort, direction)


        result_dict = result[1]
        if result[0] is not None:
            
            for repo in result[0]:
                repo["base64_url"] = str(repo["base64_url"].decode())

            result_dict.update({"repos": result[0]})        

        return jsonify(result_dict)

    @server.app.route(f"/{AUGUR_API_VERSION}/user/group/repos/count", methods=['GET', 'POST'])
    @login_required
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

        group_name = request.args.get("group_name")

        result = current_user.get_group_repo_count(group_name)

        result_dict = result[1]
        if result[0] is not None:
            result_dict.update({"repo_count": result[0]})

        return jsonify(result_dict)

    @server.app.route(f"/{AUGUR_API_VERSION}/user/groups/names", methods=['GET', 'POST'])
    @login_required
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

        result = current_user.get_group_names()

        return jsonify({"status": "success", "group_names": result[0]})

    @server.app.route(f"/{AUGUR_API_VERSION}/user/groups/repos/ids", methods=['GET', 'POST'])
    @login_required
    def get_user_groups_and_repos():
        """Get a list of user groups and their repos

        Returns
        -------
        list
            A list with this strucutre : [{"<group_name>": <list_of_repos}, ...]
        """

        if not development and not request.is_secure:
            return generate_upgrade_request()

        result = current_user.get_groups()
        if not result[0]:
            return result[1]

        groups = result[0]
        data = []
        for group in groups:

            repo_ids = [repo.repo_id for repo in group.repos]
            data.append({group.name : repo_ids})
        

        return jsonify({"status": "success", "data": data})

        