import pytest
import requests
from time import sleep

from workers.gitlab_issues_worker.gitlab_issues_worker import GitLabIssuesWorker

@pytest.fixture
def test_task():
    return {
        "given": {
            "git_url": "https://gitlab.com/NickBusey/HomelabOS"
        },
        "models": ["issues"],
        "job_type": "MAINTAIN",
        "display_name": "issues model for url: https://gitlab.com/NickBusey/HomelabOS",
        "focused_task": 1
    }

@pytest.fixture
def gitlab_issues_worker():
    config = {
        "offline_mode": True,
        "quiet": True
    }

    gitlab_issues_worker = GitLabIssuesWorker(config=config)
    return gitlab_issues_worker

def test_gitlab_issues_worker(gitlab_issues_worker, test_task):
    gitlab_issues_worker.gitlab_issues_model(test_task, 6853087)
    # data persistence test
    issues = requests.get('https://gitlab.com/api/v4/projects/6853087/issues', headers=gitlab_issues_worker.headers)
    print(issues)
    assert 1==2

    
    