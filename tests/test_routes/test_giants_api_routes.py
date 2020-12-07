#SPDX-License-Identifier: MIT
import requests
import pytest

def test_giants_api_repos(metrics):
    response = requests.get('http://localhost:5113/api/unstable/giants-project/repos')
    assert response.status_code == 200
    data = response.json()
    for item in data:
        item['repo_id']

def test_giants_api_status(metrics):
    response = requests.get('http://localhost:5113/api/unstable/giants-project/repos')
    assert response.status_code == 200
    data = response.json()
    for item in data:
        item['repo_id']
    repo_id = data[0]['repo_id']
    response = requests.get('http://localhost:5113/api/unstable/giants-project/status/' + repo_id)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]

def test_giants_api_tracked(metrics):
    response = requests.get('http://localhost:5113/api/unstable/giants-project/new-key')
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    key = data[0]
    response = requests.get('http://localhost:5113/api/unstable/giants-project/tracked/' + key + '/api/unstable/giants-project/repos')
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]['added'] >= 0
    assert data[0]['removed'] >= 0
    response = requests.get('http://localhost:5113/api/unstable/giants-project/history/' + key)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0] == "api/unstable/giants-project/repos"

