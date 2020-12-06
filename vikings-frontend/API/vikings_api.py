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
        cur.execute('''SELECT rg.repo_group_id, rg_name, rg_description, rg_website,CAST(rg_last_modified AS DATE), rp.num_repos
                        FROM augur_data.repo_groups rg
                        LEFT JOIN (SELECT repo_group_id, count(*) AS num_repos
                        FROM augur_data.repo
                        GROUP BY repo_group_id) rp ON rp.repo_group_id = rg.repo_group_id ''')
        results=cur.fetchall()

        data=[]
        for i in results:
            data.append({
                "repo_group_id":str(i[0]),
                "rg_name":str(i[1]),
                "rg_description":str(i[2]),
                "rg_website":str(i[3]),
                "rg_last_modified":str(i[4]),
                "num_repos":str(i[5])
            })
            

        cur.close()
        conn.close()

        return jsonify(data)






    return app