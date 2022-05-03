-- message_analysis
-- Author: Dr. Sean Goggins
SELECT
    --message_analysis.msg_id,
    AVG ( sentiment_score ) as average_sentiment,
    count(*),
    repo.repo_id,
    repo_name 
FROM
    message_analysis,
    repo,
    issue_message_ref 
WHERE
    repo.repo_id = issue_message_ref.repo_id 
    AND message_analysis.msg_id = issue_message_ref.msg_id 
GROUP BY
    --message_analysis.msg_id,
    repo.repo_id,
    repo_name
order by average_sentiment; 