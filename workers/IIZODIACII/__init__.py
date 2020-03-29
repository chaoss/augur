from .models import db, Contributor
import os
import functools
import requests

from flask import Flask, request, Response, jsonify
from flask_migrate import Migrate


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://augur:root@localhost:5432/demo"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)

    @app.route('/', methods=['POST'])
    def index():
        id = request.get_json()['repo_id']
        response = requests.get(
            f"https://gitlab.com/api/v4/projects/{id}/repository/contributors")

        contributors = response.json()

        if len(contributors) == 0:
            return jsonify(message="No contributors on this repo yet")

        else:
            for contributor in contributors:
                contributor_data = Contributor(
                    repo_id=id, name=contributor['name'], email=contributor['email'],
                    commits=contributor['commits'], additions=contributor['additions'], deletions=contributor['deletions'])
                db.session.add(contributor_data)
                db.session.commit()

            return Response(response,
                            mimetype="application/json")
    return app
