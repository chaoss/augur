-- clustering-v2
-- Author: Dr. Sean Goggins
SELECT
    repo_cluster_messages.repo_id,
    repo.repo_name,
    repo_cluster_messages.cluster_content,
    MAX ( repo_cluster_messages.data_collection_date ) 
FROM
    augur_data.repo_cluster_messages,
    augur_data.repo 
WHERE
    repo_cluster_messages.repo_id = repo.repo_id 
GROUP BY
    repo_cluster_messages.repo_id,
    repo.repo_name,
    repo_cluster_messages.cluster_content