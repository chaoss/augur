import inspect
import sys
import types
import datetime
import sqlalchemy as s
import pandas as pd
import requests
import json
from augur.util import logger, annotate, add_metrics

@annotate(tag='committer-data')
def committer_data(self, repo_group_id, repo_id=None, period='all', begin_date=None, end_date=None):
    """
    Returns a timeseries of all the contributions to a project.
    DataFrame has these columns:
    date
    commits
    :param repo_id: The repository's id
    :param repo_group_id: The repository's group id
  -----  :param period: To set the periodicity to 'all', day', 'week', 'month' or 'year', defaults to 'all'
  -----  :param begin_date: Specifies the begin date, defaults to '1970-1-1 00:00:00'
  -----  :param end_date: Specifies the end date, defaults to datetime.now()
    :return: DataFrame of persons/period
    """

    if not begin_date:
        begin_date = '1970-1-1 00:00:01'
    if not end_date:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if repo_id:
        contributorsSQL = s.sql.text("""
            SELECT 
	            DISTINCT cmt_author_name,
	            cmt_author_affiliation,
                repo_id
            FROM
                augur_data.commits
            WHERE
                repo_id = :repo_id
        """)

        results = pd.read_sql(contributorsSQL, self.database, params={'repo_id': repo_id, 'period': period,
                                                                'begin_date': begin_date, 'end_date': end_date})
    else:
        contributorsSQL = s.sql.text("""
            SELECT 
	            DISTINCT cmt_author_name,
	            cmt_author_affiliation,
                repo_id
            FROM
                augur_data.commits
            WHERE repo_id in (SELECT repo_id
                            FROM augur_data.repo
                            WHERE repo_group_id = :repo_group_id)
        """)

        results = pd.read_sql(contributorsSQL, self.database, params={'repo_group_id': repo_group_id, 'period': period,
                                                                'begin_date': begin_date, 'end_date': end_date})
    
    headers = {
        'X-API-KEY': 'a978daf0d0bae32c8377c1613db4a22b'
    }
    genderURL = "https://v2.namsor.com/NamSorAPIv2/api2/json/genderFull/"
    ethURL = "https://v2.namsor.com/NamSorAPIv2/api2/json/usRaceEthnicity/"
    gender = []
    genderProb = []
    eth = []
    ethProb = []

    for _, row in results.iterrows():
        name = row['cmt_author_name']
        dividedName = name.split(" ")

        if len(dividedName) == 2:
            r = requests.get(genderURL + name, headers=headers)
            rjson = r.json()
            gender.append(rjson['likelyGender'])
            genderProb.append(rjson['genderScale'])

            r = requests.get(ethURL + dividedName[0] + "/" + dividedName[1], headers=headers)
            rjson = r.json()
            eth.append(rjson['raceEthnicity'])
            ethProb.append(rjson['probabilityCalibrated'])

        else:
            gender.append('null')
            genderProb.append(0)
            eth.append('null')
            ethProb.append(0)

    results['gender'] = gender
    results['genderProb'] = genderProb
    results['eth'] = eth
    results['ethProb'] = ethProb
        
    return results

def create_commit_metrics(metrics):
    add_metrics(metrics, __name__)
