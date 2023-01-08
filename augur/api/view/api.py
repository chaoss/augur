from flask import Flask, render_template, render_template_string, request, abort, jsonify, redirect, url_for, session, flash
from flask_login import current_user, login_required
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
    def av_add_user_repo(repo_url = None):
        if not repo_url:
            flash("Repo or org URL must not be empty")
        elif current_user.try_add_url(repo_url):
            flash("Successfully added repo or org")
        else:
            flash("Could not add repo or org")
        
        return redirect(url_for("user_settings"))

    """ ----------------------------------------------------------------
    """
    @server.app.route('/requests/make/<path:request_endpoint>')
    def make_api_request(request_endpoint):
        do_cache = True
        if request.headers.get("nocache") or request.args.get("nocache"):
            do_cache = False

        data = requestJson(request_endpoint, do_cache)
        if type(data) == tuple:
            return jsonify({"request_error": data[1]}), 400
        return jsonify(data)

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
