-- clustering
-- Author: Dr. Sean Goggins
SELECT
    repo_cluster_messages.repo_id,
    repo.repo_name,
    repo_cluster_messages.cluster_content,
    MAX ( repo_cluster_messages.data_collection_date ) 
FROM
    repo_cluster_messages,
    repo 
WHERE
    repo_cluster_messages.repo_id = repo.repo_id 
GROUP BY
    repo_cluster_messages.repo_id,
    repo.repo_name,
    repo_cluster_messages.cluster_content