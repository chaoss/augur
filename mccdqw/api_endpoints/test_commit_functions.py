import os
import pytest
import pandas as pd

def test_committer_data(metrics):
    assert metrics.committer_data(20).iloc[0].gender == 'male'
