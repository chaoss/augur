import os
import pytest
import pandas as pd

@pytest.fixture(scope="module")
def metrics():
    import augur
    augur_app = augur.Application()
    return augur_app.metrics

def test_contributor_affiliation(metrics):
    assert metrics.contributor_affiliation(20,period='year').iloc[0].lat > 38
