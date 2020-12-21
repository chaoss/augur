#SPDX-License-Identifier: MIT
import requests
import pytest

def test_giants_api_repos(metrics):
    response = requests.get('http://localhost:5113/api/unstable/giants-project/repos')
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1

def test_giants_api_status(metrics):
    response = requests.get('http://localhost:5113/api/unstable/giants-project/repos')
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    repo_id = data[0]['repo_id']
    response = requests.get('http://localhost:5113/api/unstable/giants-project/status/' + str(repo_id))
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]
