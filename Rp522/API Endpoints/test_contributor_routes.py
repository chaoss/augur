"""
Test for route for new contributor endpoint
"""

def test_contributors(metrics):
    response = request.get('http://localhost:5000/api/unstable/contributors/s@goggins.com/contributions')
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
