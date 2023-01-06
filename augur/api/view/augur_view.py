from flask import Flask, render_template, redirect, url_for, session, request
from flask_login import LoginManager
from .utils import *
from .url_converters import *
# from .server import User
from augur.application.db.models import User
from augur.application.db.session import DatabaseSession

login_manager = LoginManager()

def create_routes(server):
    login_manager.init_app(server.app)

    server.app.secret_key = getSetting("session_key")

    server.app.url_map.converters['list'] = ListConverter
    server.app.url_map.converters['bool'] = BoolConverter
    server.app.url_map.converters['json'] = JSONConverter

    # Code 404 response page, for pages not found
    @server.app.errorhandler(404)
    def page_not_found(error):
        return render_template('index.html', title='404', api_url=getSetting('serving')), 404

    @server.app.errorhandler(405)
    def unsupported_method(error):
        return renderMessage("405 - Method not supported", "The resource you are trying to access does not support the request method used"), 405

    @login_manager.unauthorized_handler
    def unauthorized():
        session["login_next"] = url_for(request.endpoint, **request.args)
        return redirect(url_for('user_login'))

    @login_manager.user_loader
    def load_user(user_id):

        user = User.get_user(user_id)

        if not user:
            return None

        # The flask_login library sets a unique session["_id"]
        # when login_user() is called successfully
        if session.get("_id") is not None:

            # TODO: Add these as properties
            user._is_authenticated = True
            user._is_active = True

        return user

