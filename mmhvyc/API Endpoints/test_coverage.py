import datetime
import sqlalchemy as s
import pandas as pd
from augur.util. import logger, annotate, add_metrics

""" SQL Query
SELECT
	augur_data.repo_test_coverage.repo_id,
	augur_data.repo_test_coverage.file_subroutines_tested,
	augur_data.repo_test_coverage.file_subroutine_count,
	augur_data.repo_test_coverage.file_statements_tested,
	augur_data.repo_test_coverage.file_statement_count
FROM augur_data.repo_test_coverage JOIN augur_data.repo on repo_test_coverage.repo_id = repo.repo_id
GROUP BY augur_data.repo_test_coverage.repo_id
"""
@annotate(tag='testing-coverage')
def testing_coverage(self, repo_group_id, repo_id = 'None', period='day', begin_date=None, end_date=None):
	"""
	<the metric analzyes how much a repository is tested>
	:parameter repo_group_id: The repository’s group id
	:return: Dataframe of <testing-coverage for a repository>
	"""

	if not begin_date:
		begin_date = '1970-1-1 00:00:00'

	if not end_date:
		end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M)

	testing_coverage_SQL = ' '
							    
	if not repo_id:
		testing_coverage_SQL = s.sql.text("""
		SELECT
			augur_data.repo_test_coverage.repo_id,
			augur_data.repo_test_coverage.file_subroutines_tested,
			augur_data.repo_test_coverage.file_subroutine_count,
			augur_data.repo_test_coverage.file_statements_tested,
			augur_data.repo_test_coverage.file_statement_count
		FROM augur_data.repo_test_coverage JOIN augur_data.repo on repo_test_coverage.repo_id = repo.repo_id
		GROUP BY augur_data.repo_test_coverage.repo_id
	
		
	""")
							    
	results = pd.read_sql(testing_coverage_SQL, self.database, params = {‘repo_group_id’: repo_group_id})
	# output the testing coverage as percentages, one for subroutines tested and one for statements tested
	return results

	else:
		testing_coverage_SQL> = s.sql.text("""
		SELECT
			augur_data.repo_test_coverage.file_subroutines_tested,
			augur_data.repo_test_coverage.file_subroutine_count,
			augur_data.repo_test_coverage.file_statements_tested,
			augur_data.repo_test_coverage.file_statement_count
		FROM augur_data.repo_test_coverage JOIN augur_data.repo on repo_test_coverage.repo_id = repo.repo_id
		GROUP BY augur_data.repo_test_coverage.repo_id
	""")
	results = pd.read_sql(testing_coverage_SQL, self.database, params={‘repo_id’: repo_id})
	# same as above for outputting percentages
	return results
