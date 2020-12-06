import flask
import json
from flask import jsonify, request
import psycopg2
from flask_cors import CORS
from datetime import datetime
import db
import plotly.graph_objects as go
import plotly.io as pio
import matplotlib.pyplot as plt
import numpy as np

def create_app(test_config=None):
    ##Add comment for commit 
    
    app = flask.Flask(__name__)
    CORS(app)
    app.config["DEBUG"] = True





    ##HOME PAGE

    @app.route('/repogroups', methods=['GET'])
    def generalstats():
        conn=db.connectToDb()
        # Create a cursor object

        cur = conn.cursor()
        cur.execute('''SELECT repo_group_id, rg_name, rg_description, rg_website, rg_recache, rg_last_modified, rg_type, tool_source, tool_version, data_source, data_collection_date
	    FROM augur_data.repo_groups ''')
        test=cur.fetchall()

        return jsonify(test)






    return app