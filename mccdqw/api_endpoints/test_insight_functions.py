def test_testing_coverage(metrics):
    assert metrics.testing_coverage(20).iloc[0].file_statement_count > 0
