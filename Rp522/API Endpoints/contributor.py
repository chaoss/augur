"""
Endpoint from metrics file
"""

@annotate(tag='contributions')
def contributions(self, contributor_email):
    contributionsSQL = s.sql.text("""
    SELECT repo.repo_id, COUNT(commits) as contributions
    FROM repo, commits
    WHERE commits.repo_id = repo.repo_id
    AND commits.cmt_committer_email = :contributor_email
    GROUP BY repo.repo_id
    ORDER BY repo.repo_id asc
    """)

    results = pd.read_sql(contributionsSQL, self.database, params={'contributor_email': contributor_email})
    return results
