from flask import Flask, render_template, render_template_string, request, abort, jsonify, redirect, url_for, session, flash
from flask_login import current_user, login_required
from augur.util.repo_load_controller import parse_org_url, parse_repo_url
from .utils import *

def create_routes(server):
    @server.app.route('/cache/file/')
    @server.app.route('/cache/file/<path:file>')
    def cache(file=None):
        if file is None:
            return redirect(url_for('root', path=getSetting('caching')))
        return redirect(url_for('root', path=toCacheFilepath(file)))

    @server.app.route('/account/repos/add/<path:repo_url>')
    @server.app.route('/account/repos/add')
    @login_required
    def av_add_user_repo(url = None):
        # TODO finish UI and implement group adding
        if not url:
            flash("Repo or org URL must not be empty")
        elif result := parse_org_url(url):
            current_user.add_org()
            flash("Successfully added org")
        elif result := parse_repo_url(url):
            flash("Successfully added repo")
        else:
            flash("Could not add repo or org")
        
        return redirect(url_for("user_settings"))
    
    """ ----------------------------------------------------------------
    Locking request loop:
        This route will lock the current request until the
        report request completes. A json response is guaranteed.
        Assumes that the requested repo exists.
    """
    @server.app.route('/requests/report/wait/<id>')
    def wait_for_report_request(id):
        requestReports(id)
        return jsonify(report_requests[id])
