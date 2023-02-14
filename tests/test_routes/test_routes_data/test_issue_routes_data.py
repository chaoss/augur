#SPDX-License-Identifier: MIT
import requests
import pytest
from tests import server_port


def test_issues_new_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/issues-new')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['issues'] > 0

def test_issues_new_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/issues-new')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['issues'] > 0

def test_issues_active_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/issues-active')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['issues'] > 0

def test_issues_active_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/issues-active')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['issues'] > 0

def test_issues_closed_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/issues-closed')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['issues'] > 0

def test_issues_closed_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/issues-closed')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['issues'] > 0

def test_issue_duration_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/issue-duration')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1

def test_issue_duration_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/issue-duration')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1

def test_issue_participants_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/issue-participants')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['participants'] > 0

def test_issue_participants_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/issue-participants')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['participants'] > 0

def test_issue_throughput_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/issue-throughput')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['throughput'] >= 0

def test_issue_throughput_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/issue-throughput')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['throughput'] >= 0

def test_issue_backlog_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/issue-backlog')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['issue_backlog'] > 0

def test_issue_backlog_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/issue-backlog')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['issue_backlog'] > 0

def test_issues_first_time_opened_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/issues-first-time-opened')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["count"] > 0

def test_issues_first_time_opened_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/issues-first-time-opened')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["count"] > 0

def test_issues_first_time_closed_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/20/issues-first-time-closed')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["count"] > 0

def test_issues_first_time_closed_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/20/repos/25430/issues-first-time-closed')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["count"] > 0

def test_open_issues_count_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/open-issues-count')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['open_count'] > 0

def test_open_issues_count_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/open-issues-count')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['open_count'] > 0

def test_closed_issues_count_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/closed-issues-count')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['closed_count'] > 0

def test_closed_issues_count_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/closed-issues-count')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]['closed_count'] > 0

def test_issues_open_age_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/issues-open-age/')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["open_date"] > 1

def test_issues_open_age_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/issues-open-age/')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["open_date"] > 1

def test_issues_closed_resolution_duration_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/issues-closed-resolution-duration/')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["diffdate"] >= 0


def test_issues_closed_resolution_duration_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/issues-closed-resolution-duration/')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["diffdate"] >= 0

def test_issues_maintainer_response_duration_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/issues-maintainer-response-duration/')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["average_days_comment"] >= 0

def test_issues_maintainer_response_duration_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/issues-maintainer-response-duration/')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["average_days_comment"] >= 0
    assert data[0]["average_days_comment"] >= 0

def test_average_issue_resolution_time_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/average-issue-resolution-time')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0

def test_average_issue_resolution_time_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/average-issue-resolution-time')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0

def test_issue_comments_mean_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/issue-comments-mean')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1

def test_issue_comments_mean_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/issue-comments-mean')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1

def test_issue_comments_mean_std_by_group_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/issue-comments-mean-std')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1

def test_issue_comments_mean_std_by_repo_api_data():
    response = requests.get(f'http://localhost:{server_port}/api/unstable/repo-groups/10/repos/25430/issue-comments-mean-std')
    assert response is not None
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
