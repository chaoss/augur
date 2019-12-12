"""
Test routes for new endpoints in the commits file
"""

def test_repo_timeline(metrics):
    response = requests.get('http://localhost:5000/api/unstable/repo-groups/20/repos/21000/repo-timeline')
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["net"] > 0

def test_repo_group_timeline(metrics):
    response = requests.get('http://localhost:5000/api/unstable/repo-groups/20/repo-group-timeline')
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["net"] > 0
