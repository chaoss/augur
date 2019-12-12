"""
Tests for new endpoints in commits folder
"""

def test_repo_timeline(metrics):
    assert metrics.repo_timeline(20, 21000).iloc[0].net > 0

def test_repo_group_timeline(metrics):
    assert metrics.repo_group_timeline(20).iloc[0].net > 0
