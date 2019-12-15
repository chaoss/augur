def test_contributor_affiliation(metrics):
    response = requests.get('http://localhost:5000/api/unstable/repo-groups/20/contributor-affiliation')
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
