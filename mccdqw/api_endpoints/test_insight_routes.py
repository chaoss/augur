import requests
import pytest

@pytest.fixture(scope="session")
def metrics():
    pass

def test_commit_test_coverage(metrics):
    response = requests.get('http://localhost:5000/api/unstable/repo-groups/20/commit-test-coverage')
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
