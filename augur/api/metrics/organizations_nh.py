import datetime
import sqlalchemy as s
import pandas as pd
from augur.util import register_metric

from augur.application.db.engine import create_database_engine
engine = create_database_engine()

@register_metric()
def contributor_affiliations()
  """
  Add comments here
  """
  
  
  if repo_id:
    cntrb_affiliationsSQL = s.sql.text("""
      SELECT trim(BOTH from cntrb_company) as cntrb_company, 
      COUNT(*) AS organization_cntrb 
      FROM augur_data.contributors INNER JOIN 
	      (SELECT pr_augur_contributor_id 
	      FROM augur_data.pull_requests 
	      WHERE repo_id = 26285) AS pr_cntrb_id 
	      ON contributors.cntrb_id=pr_cntrb_id.pr_augur_contributor_id 
	      Group by trim(BOTH from cntrb_company)
      """)
    
    results = pd.read_sql(cntrb_affiliationsSQL, engine, params={'repo_id': repo_id, 'period': period,
                                                                'begin_date': begin_date, 'end_date': end_date})
  else:
    cntrb_affiliationsSQL = s.sql.text("""
      SELECT trim(BOTH from cntrb_company) as cntrb_company, 
      COUNT(*) AS organization_cntrb 
      FROM augur_data.contributors INNER JOIN 
	      (SELECT pr_augur_contributor_id 
	      FROM augur_data.pull_requests 
	      WHERE repo_id = 26285) AS pr_cntrb_id 
	      ON contributors.cntrb_id=pr_cntrb_id.pr_augur_contributor_id 
	      Group by trim(BOTH from cntrb_company)
      """)
          
    results = pd.read_sql(contributorsSQL, engine, params={'repo_group_id': repo_group_id, 'period': period,
                                                                'begin_date': begin_date, 'end_date': end_date}) 

  return results
