import datetime
import sqlalchemy as s
import pandas as pd
from augur.api.util import register_metric

from augur.application.db.engine import create_database_engine
engine = create_database_engine(repo_group_id, repo_id=None, period='day', begin_date=None, end_date=None)

@register_metric()
def contributor_affiliations():
  """
  Add comments here
  """
  
  
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
