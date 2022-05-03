-- discourse_insights
-- Author: Dr. Sean Goggins
SELECT
    discourse_act,
    COUNT ( * ) AS discourse_type_count,
    repo.repo_id,
    repo_name 
FROM
    discourse_insights,
    repo,
    issue_message_ref 
WHERE
    repo.repo_id = issue_message_ref.repo_id 
    AND discourse_insights.msg_id = issue_message_ref.msg_id 
GROUP BY
    discourse_act,
    repo.repo_id 
ORDER BY
    repo_name;