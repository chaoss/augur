"""
Metrics that provide data about with insight detection and reporting
"""

import datetime
import sqlalchemy as s
import pandas as pd
from augur.util import logger, annotate, add_metrics


@annotate(tag='top-insights')
def top_insights(self, repo_group_id, num_repos=6):
    """
    Timeseries of pull request acceptance rate (expressed as the ratio of pull requests merged on a date to the count of pull requests opened on a date)

    :return: DataFrame with top insights across all repos
    """

    topInsightsSQL = s.sql.text("""
        SELECT rg_name, repo.repo_group_id, repo_insights.repo_id, repo_git, ri_metric, ri_field, ri_value AS value,
            ri_date AS date, ri_fresh AS discovered
        FROM repo_insights JOIN repo ON repo.repo_id = repo_insights.repo_id JOIN repo_groups ON repo.repo_group_id = repo_groups.repo_group_id
        WHERE repo_insights.repo_id IN (
            SELECT repo_id
            FROM repo
            WHERE repo_group_id = :repo_group_id
            AND repo_id IN (SELECT repo_id FROM repo_insights GROUP BY repo_id, ri_id HAVING 304 > count(repo_insights.repo_id) ORDER BY ri_id desc)
            LIMIT :num_repos
        )
    """)
    results = pd.read_sql(topInsightsSQL, self.database, params={'repo_group_id': repo_group_id, 'num_repos': num_repos})
    return results

@annotate(tag='testing-coverage')
def testing_coverage(self, repo_group_id, repo_id=None, period='day', begin_date=None, end_date=None):
	"""
	<the metric analzyes how much a repository is tested>
	:parameter repo_group_id: The repository’s group id
	:return: Dataframe of <testing-coverage for a repository>
	"""

	if not begin_date:
		begin_date = '1970-1-1 00:00:00'

	if not end_date:
		end_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

							    
	if not repo_id:
		testing_coverage_SQL = s.sql.text("""
		SELECT
			repo_test_coverage.repo_id,
			repo_test_coverage.file_subroutines_tested,
			repo_test_coverage.file_subroutine_count,
			repo_test_coverage.file_statements_tested,
			repo_test_coverage.file_statement_count
		FROM augur_data.repo_test_coverage JOIN augur_data.repo on repo_test_coverage.repo_id in (SELECT repo_id
													  	FROM augur_data.repo
														WHERE repo_group_id = :repo_group_id)
		GROUP BY repo_test_coverage.repo_id
	
		
		""")
							    
		results = pd.read_sql(testing_coverage_SQL, self.database, params={'repo_group_id': repo_group_id, 'period': period, 'begin_date': begin_date, 'end_date': end_date})
		# output the testing coverage as percentages, one for subroutines tested and one for statements tested
		return results

	else:
		testing_coverage_SQL = s.sql.text("""
		SELECT
			augur_data.repo_test_coverage.file_subroutines_tested,
			augur_data.repo_test_coverage.file_subroutine_count,
			augur_data.repo_test_coverage.file_statements_tested,
			augur_data.repo_test_coverage.file_statement_count
		FROM augur_data.repo_test_coverage JOIN augur_data.repo on repo_test_coverage.repo_id in (SELECT repo_id
													  	FROM augur_data.repo
														WHERE repo_group_id = :repo_group_id) 
		GROUP BY augur_data.repo_test_coverage.repo_id
		""")
		results = pd.read_sql(testing_coverage_SQL, self.database, params={'repo_id': repo_id, 'period': period, 'begin_date': begin_date, 'end_date': end_date})
		# same as above for outputting percentages
		return results


def create_insight_metrics(metrics):
    add_metrics(metrics, __name__)
