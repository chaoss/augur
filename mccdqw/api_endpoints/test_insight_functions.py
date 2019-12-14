import os
import pytest
import pandas as pd

@pytest.fixture(scope="module")
def metrics():
    import augur
    augur_app = augur.Application()
    return augur_app.metrics

def test_commit_test_coverage(metrics):
    assert metrics.commit_test_coverage(20).iloc[0].file_statement_count > 0
