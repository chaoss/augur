import flask
import json
from flask import jsonify, request
import psycopg2
from flask_cors import CORS
from datetime import datetime
import db
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
        cur.execute('''SELECT 
                            rg.repo_group_id, 
                            rg_name, 
                            rg_description, 
                            rg_website,
                            CAST(rg_last_modified AS DATE), rp.num_repos
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





    @app.route('/getrepos', methods=['POST'])
    def getRepos():
        repo_group_id=json.loads(request.data)
        #repo_group_id=22002
        conn=db.connectToDb()    # Create a cursor object
        cur = conn.cursor()

        
        cur.execute('''SELECT 
                        r.repo_id,
                        r.repo_name,
                        r.repo_git,
                        ri.issues_count,
                        ri.committers_count,
                        ri.commit_count,
                        rg.rg_name
                    FROM augur_data.repo r
                    LEFT JOIN augur_data.repo_info ri ON ri.repo_id=r.repo_id
                    LEFT JOIN augur_data.repo_groups rg ON rg.repo_group_id=r.repo_group_id
                    WHERE r.repo_group_id='''+str(repo_group_id))

        repos=cur.fetchall()

        cur.close()
        conn.close()

        data=[]
        for i in repos:
            data.append({
                "repo_id":str(i[0]),
                "repo_name":str(i[1]),
                "repo_git":str(i[2]),
                "issues_count":str(i[3]),
                "committers_count":str(i[4]),
                "commit_count":str(i[5]),
                "rg_name":str(i[6])
            })
            

        cur.close()
        conn.close()

        return jsonify(data)


    @app.route('/getcommits', methods=['POST'])
    def getCommits():
        repo_id=json.loads(request.data)
        #repo_group_id=22002
        conn=db.connectToDb()    # Create a cursor object
        cur = conn.cursor()

        
        cur.execute('''
                        SELECT 
                        CAST(cmt_committer_date AS DATE), 
                        COUNT(*) AS num_commit
                        FROM augur_data.commits
                        WHERE repo_id='''+str(repo_id)+''' GROUP BY CAST(cmt_committer_date AS DATE)
                        ORDER BY CAST(cmt_committer_date AS DATE) ASC''')

        commits=cur.fetchall()

        cur.close()
        conn.close()

        dates=[]
        num_commits=[]

        for i in commits:

            dates.append(str(i[0]))
            num_commits.append(str(i[1]))
            

        cur.close()
        conn.close()

        together=[dates,num_commits]

        print(together)
        return jsonify(together)




    return app
