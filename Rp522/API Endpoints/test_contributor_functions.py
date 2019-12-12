"""
Test for new contributor endpoint
"""

def test_contributions(metrics):
    assert metrics.contributions("s@goggins.com").iloc[0]['count'] > 0
