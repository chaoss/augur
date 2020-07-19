import pytest
import requests
from time import sleep

from workers.gitlab_issues_worker.gitlab_issues_worker import GitLabIssuesWorker
from workers.worker_base import Worker
import sqlalchemy as s

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

    # connect to sqlalchemy models
    worker_config = gitlab_issues_worker.config
    database_connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(
            worker_config["user_database"], worker_config["password_database"],
            worker_config["host_database"], worker_config["port_database"], worker_config["name_database"]
        )

    csearch_path_options = 'augur_data'

    engine = s.create_engine(database_connection_string, poolclass=s.pool.NullPool,
        connect_args={'options': f'-csearch_path={csearch_path_options}'}, pool_pre_ping=True)

    conn = engine.connect()
    result = engine.execute("select * from augur_data.issues")
    for row in result:
        print(row)




    gitlab_issues_worker._queue.put(test_task)
    gitlab_issues_worker.collect()
    
    # data persistence test
    print('collection done')
    issues = requests.get('https://gitlab.com/api/v4/projects/6853087/issues', headers=gitlab_issues_worker.headers)
    issues_list = issues.json()
    id_list = [issue['id'] for issue in issues_list]

    

    assert 1==2

    
    