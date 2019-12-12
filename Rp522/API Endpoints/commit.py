"""
Two endpoints added to the commit.py file in the metrics folder
"""

@annotate(tag='repo-timeline')
def repo_timeline(self, repo_group_id, repo_id):
    timelineSQL = s.sql.text("""
        SELECT commits.cmt_committer_date as date, COUNT(*) as commits
        FROM repo, commits
        WHERE repo.repo_id = commits.repo_id
        AND repo.repo_id = :repo_id
        GROUP BY commits.cmt_committer_date
        ORDER BY commits.cmt_committer_date asc
    """)
    
    results = pd.read_sql(timelineSQL, self.database, params={ "repo_group_id": repo_group_id, "repo_id": repo_id})
    return results
@annotate(tag='repo-group-timeline')
def repo_group_timeline(self, repo_group_id): 
    repoSQL = s.sql.text("""
    SELECT DISTINCT repo.repo_id
    FROM repo
    WHERE repo.repo_group_id = :repo_group_id
    ORDER BY repo.repo_id asc
    """)
    timelineSQL = s.sql.text("""
    SELECT commits.cmt_committer_date as dates, COUNT(*) as commits
    FROM repo, commits
    WHERE repo.repo_id = commits.repo_id
    AND repo.repo_id = :repo_id
    GROUP BY commits.cmt_committer_date
    ORDER BY commits.cmt_committer_date asc
    """)
    results = []
    repos = pd.read_sql(repoSQL, self.database, params={ "repo_group_id": repo_group_id })
    for idx, repo in repos.items():
        for item in repo.iteritems():
            repo_id = item[1]
            timeline = pd.read_sql(timelineSQL, self.database, params={ "repo_id": repo_id})
            results.append({
                "repo_id": item[1],
                "timeline": timeline.to_dict()
                })
    return results
