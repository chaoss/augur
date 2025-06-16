vacuumdb -h localhost -p 5434 -U augur -j 4 -z -v augur; 
psql -U augur -h localhost -p 5434 -d augur -c 'REFRESH MATERIALIZED VIEW concurrently augur_data.explorer_commits_and_committers_daily_count with data;'
psql -U augur -h localhost -p 5434 -d augur -c 'REFRESH MATERIALIZED VIEW concurrently augur_data.explorer_contributor_actions with data;'
psql -U augur -h localhost -p 5434 -d augur -c 'REFRESH MATERIALIZED VIEW concurrently augur_data.explorer_new_contributors with data;'
psql -U augur -h localhost -p 5434 -d augur -c 'REFRESH MATERIALIZED VIEW concurrently augur_data.explorer_user_repos with data;'
psql -U augur -h localhost -p 5434 -d augur -c 'REFRESH MATERIALIZED VIEW concurrently augur_data.explorer_pr_metrics with data;'
