import datetime
import sqlalchemy as s
import pandas as pd
from augur.api.util import register_metric

from augur.application.db.engine import create_database_engine
engine = create_database_engine()

@register_metric()
def contributor_affiliations(repo_group_id, repo_id=None, period='day', begin_date=None, end_date=None):
  """
  Add comments here
  """
  
  if not begin_date:
    begin_date = '1970-1-1 00:00:01'
  if not end_date:
    end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  
  if repo_id:
    cntrb_affiliationsSQL = s.sql.text("""
      SELECT 'Organizations' as null_state, COUNT(*)
      FROM augur_data.pull_requests
      inner join augur_data.contributors on pull_requests.pr_augur_contributor_id = contributors.cntrb_id
      WHERE repo_id = :repo_id
        AND cntrb_company is not null
      union
      SELECT 'Volunteers' as null_state, COUNT(*)
      FROM augur_data.pull_requests
      inner join augur_data.contributors on pull_requests.pr_augur_contributor_id = contributors.cntrb_id
      WHERE repo_id = :repo_id
        AND cntrb_company is null;
      """)
    
    results = pd.read_sql(cntrb_affiliationsSQL, engine, params={'repo_id': repo_id, 'period': period,
                                                                'begin_date': begin_date, 'end_date': end_date})
  else:
    cntrb_affiliationsSQL = s.sql.text("""
           SELECT 'Organizations' as null_state, COUNT(*)
      FROM augur_data.pull_requests
      inner join augur_data.contributors on pull_requests.pr_augur_contributor_id = contributors.cntrb_id
      WHERE repo_id = :repo_id
        AND cntrb_company is not null
      union
      SELECT 'Volunteers' as null_state, COUNT(*)
      FROM augur_data.pull_requests
      inner join augur_data.contributors on pull_requests.pr_augur_contributor_id = contributors.cntrb_id
      WHERE repo_id = :repo_id
        AND cntrb_company is null;
      """)
          
    results = pd.read_sql(contributorsSQL, engine, params={'repo_group_id': repo_group_id, 'period': period,
                                                                'begin_date': begin_date, 'end_date': end_date}) 

  return results
