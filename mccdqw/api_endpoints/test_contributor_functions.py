def test_contributor_affiliation(metrics):
    assert metrics.contributor_affiliation(20,period='year').iloc[0].lat > 38
