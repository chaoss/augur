from augur.tasks.gitlab.merge_request_task import collect_gitlab_merge_requests

# Run the Celery task with your GitLab repo URL
collect_gitlab_merge_requests.delay("https://gitlab.com/gitlab-org/gitlab.git?dummy=1")
