def test_committer_data(metrics):
    assert metrics.committer_data(20).iloc[6].gender == 'male'
    assert metrics.committer_data(20).iloc[6].cmt_author_name == 'Alberto Martín'
