from flask import render_template, redirect, url_for, session, request, jsonify
from flask_login import LoginManager
from io import StringIO
from .utils import *
from .init import logger
from .url_converters import *

# from .server import User
from ..server import app, db_session
from augur.application.db.models import User, UserSessionToken
from augur.api.routes import AUGUR_API_VERSION
from augur.api.util import get_bearer_token

import time, traceback

login_manager = LoginManager()

login_manager.init_app(app)

app.secret_key = getSetting("session_key")

app.url_map.converters['list'] = ListConverter
app.url_map.converters['bool'] = BoolConverter
app.url_map.converters['json'] = JSONConverter

# Code 404 response page, for pages not found
@app.errorhandler(404)
def page_not_found(error):
    if AUGUR_API_VERSION in str(request.path):
        return jsonify({"status": "Not Found"}), 404

    return render_template('index.j2', title='404'), 404

@app.errorhandler(405)
def unsupported_method(error):
    if AUGUR_API_VERSION in str(request.path):
        return jsonify({"status": "Unsupported method"}), 405
    
    return render_message("405 - Method not supported", "The resource you are trying to access does not support the request method used"), 405

@app.errorhandler(500)
def internal_server_error(error):
    if AUGUR_API_VERSION in str(request.path):
        return jsonify({"status": error.original_exception}), 500
    error = error.original_exception
    try:
        errout = StringIO()
        traceback.print_tb(error.__traceback__, file=errout)
        # traceback.print_exception(error, file=errout)
        stacktrace = errout.getvalue()
        errout.close()
    except Exception as e:
        logger.error(e)
    
    return render_message("500 - Internal Server Error", "An error occurred while trying to service your request. Please try again, and if the issue persists, please file a GitHub issue with the below error message:", error=stacktrace), 500

@login_manager.unauthorized_handler
def unauthorized():
    if AUGUR_API_VERSION in str(request.path):
        token_str = get_bearer_token()
        print(token_str)
        token = db_session.query(UserSessionToken).filter(UserSessionToken.token == token_str).first()
        if not token:
            return jsonify({"status": "Session expired"})

        return jsonify({"status": "Login required"})

    session["login_next"] = url_for(request.endpoint, **request.args)
    return redirect(url_for('user_login'))

@login_manager.user_loader
def load_user(user_id):

    user = User.get_user(db_session, user_id)
    if not user:
        return None

    groups = user.groups
    tokens = user.tokens
    applications = user.applications
    for application in applications:
        sessions = application.sessions
    for group in groups:
        repos = group.repos
    for token in tokens:
        application = token.application
    db_session.expunge(user)


    # The flask_login library sets a unique session["_id"]
    # when login_user() is called successfully
    if session.get("_id") is not None:
    
        user._is_authenticated = True
        user._is_active = True

    return user

@login_manager.request_loader
def load_user_request(request):
    token = get_bearer_token()

    current_time = int(time.time())
    token = db_session.query(UserSessionToken).filter(UserSessionToken.token == token, UserSessionToken.expiration >= current_time).first()
    if token:

        print("Valid user")

        user = token.user
        user._is_authenticated = True
        user._is_active = True

        return user
        
    return None

@app.template_filter('as_datetime')
def as_datetime(seconds):
    time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(seconds))