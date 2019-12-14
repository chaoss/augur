import datetime
import sqlalchemy as s
import pandas as pd
import requests
import json
from augur.util import logger, annotate, add_metrics

@annotate(tag='contributor-affiliation')
def contributor_affiliation(self, repo_group_id, repo_id=None, period='all', begin_date=None, end_date=None):
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
	        cntrb_id,
	        cntrb_company,
	        cntrb_created_at,
	        cntrb_location,
                gh_login,
                gh_html_url
            FROM
                augur_data.contributors
            WHERE
                cntrb_id in	(SELECT cntrb_id
                            FROM augur_data.issues
                            WHERE repo_id = :repo_id)
        """)

        results = pd.read_sql(contributorsSQL, self.database, params={'repo_id': repo_id, 'period': period,
                                                                'begin_date': begin_date, 'end_date': end_date})
    else:
        contributorsSQL = s.sql.text("""
            SELECT 
                cntrb_id,
	        cntrb_company,
	        cntrb_created_at,
	        cntrb_location,
                gh_login,
                gh_html_url
            FROM
                augur_data.contributors
            WHERE
                cntrb_id in	(SELECT cntrb_id
                            FROM augur_data.issues
                            WHERE repo_id in (SELECT repo_id
                                            FROM augur_data.repo
                                            WHERE repo_group_id = :repo_group_id))
        """)

        results = pd.read_sql(contributorsSQL, self.database, params={'repo_group_id': repo_group_id, 'period': period,
                                                                'begin_date': begin_date, 'end_date': end_date})
    
    url = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyA9F-7oBXz5ag8Ht5cskYr0Ci1lIkXYWbU&address='
    lat = []
    lng = []

    for _, row in results.iterrows():
        if row['cntrb_location']:
            r = requests.get(url + row['cntrb_location'])
            rjson = r.json()
            lat.append(rjson['results'][0]['geometry']['location']['lat'])
            lng.append(rjson['results'][0]['geometry']['location']['lng'])
        else:
            lat.append(None)
            lng.append(None)

    results['lat'] = lat
    results['lng'] = lng

    return results


def create_contributor_metrics(metrics):
    add_metrics(metrics, __name__)
