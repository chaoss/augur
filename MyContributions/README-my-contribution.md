# My Contributions to our Project

### My Contributor Code Contribution
1. In the contributor.py file, I added a metric function contributors-by-company
>   
        @annotate(tag='contributors-by-company')
        def contributors_by_company(self, repo_group_id, repo_id=None):
        """
        Returns the number of contributors categorized by each company.
        :param repo_group_id: The repositories group_id
        :param repo_id: The repositories ID defaults to None
        :return: DataFrame of Contributors by company
        """
        numOfContribsByCompany_SQL = ''
            if repo_id:
                numOfContribsByCompany_SQL = s.sql.text("""
                    SELECT cntrb_company, count(*) AS counter FROM 
                    (
                    SELECT DISTINCT 
                        cntrb_company, repo.repo_id, contributors.cntrb_id,
                        COUNT ( * ) AS counter 
                    FROM
                        contributors,
                        repo,
                        issues 
                    WHERE
                        repo.repo_id = issues.repo_id 
                    AND issues.cntrb_id = contributors.cntrb_id
                    AND repo.repo_id = :repo_id
                    GROUP BY
                        cntrb_company, repo.repo_id, contributors.cntrb_id
                    UNION
                    SELECT
                        cntrb_company, repo.repo_id, contributors.cntrb_id, 
                        COUNT ( * ) AS counter 
                    FROM
                        contributors,
                        repo,
                        commits 
                    WHERE
                        repo.repo_id = commits.repo_id 
                        AND ( commits.cmt_author_email = contributors.cntrb_canonical OR commits.cmt_committer_email = contributors.cntrb_canonical ) 
                        AND repo.repo_id = :repo_id
                    GROUP BY
                        cntrb_company, repo.repo_id, contributors.cntrb_id) L
                    WHERE cntrb_company IS NOT NULL
                    GROUP BY L.cntrb_company
                    ORDER BY counter DESC; 
                    """)
            results = pd.read_sql(numOfContribsByCompany_SQL, self.database, params={'repo_id': repo_id})
            return results
        else:
            numOfContribsByCompany_SQL = s.sql.text("""
                SELECT cntrb_company, count(*) AS counter FROM 
                    (
                    SELECT DISTINCT 
                        cntrb_company, repo.repo_id, contributors.cntrb_id,
                        COUNT ( * ) AS counter 
                    FROM
                        contributors,
                        repo,
                        issues 
                    WHERE
                        repo.repo_id = issues.repo_id 
                    AND issues.cntrb_id = contributors.cntrb_id
                    AND repo.repo_group_id = :repo_group_id
                    GROUP BY
                        cntrb_company, repo.repo_id, contributors.cntrb_id
                    UNION
                    SELECT
                        cntrb_company, repo.repo_id, contributors.cntrb_id, 
                        COUNT ( * ) AS counter 
                    FROM
                        contributors,
                        repo,
                        commits 
                    WHERE
                        repo.repo_id = commits.repo_id 
                        AND ( commits.cmt_author_email = contributors.cntrb_canonical OR commits.cmt_committer_email = contributors.cntrb_canonical ) 
                        AND repo.repo_group_id = :repo_group_id
                    GROUP BY
                        cntrb_company, repo.repo_id, contributors.cntrb_id) L
                    WHERE cntrb_company IS NOT NULL
                    GROUP BY L.cntrb_company
                    ORDER BY counter DESC;
                """)
            results = pd.read_sql(numOfContribsByCompany_SQL, self.database, params={'repo_group_id': repo_group_id})
        return results
2. Then, I created a metric route in the routes.py file inside of the contributor directory in augur.
>       server.addRepoMetric(metrics.contributors_by_company,'contributors-by-company')
        """
        @api {get} /repo-groups/:repo_group_id/repos/:repo_id/contributors-by-company Contributors By Company (Repo)
        @apiName contributors-by-company
        @apiGroup Contributors
        @apiDescription Returns a list of contributors by each company that contributes
        @apiParam {string} repo_group_id Repository Group ID
        @apiParam {string} repo_id Repository ID.
        @apiSuccessExample
                    [
                        {
                            "cntrb_company": "Microsoft"
                            "counter": 14
                            }
                    }
        """
        server.addRepoGroupMetric(metrics.contributors_by_company,'contributors-by-company')
        """
        @api {get} /repo-groups/:repo_group_id/repos/:repo_id/contributors-by-company Contributors By Company (Repo)
        @apiName contributors-by-company
        @apiGroup Contributors
        @apiDescription Returns a list of contributors by each company that contributes
        @apiParam {string} repo_group_id Repository Group ID
        @apiSuccessExample
                    [
                        {
                            "cntrb_company": "Microsoft"
                            "counter": 14
                            }
                    }
    """
3. Then I created pytest functions for the respective metric function and metric routes
>       # Metric function test
          def test_contributors_by_companys(metrics):
    
            #repo_group_id
            assert metrics.contributors_by_company(20).iloc[0]['counter'] > 0
            
            #repo_id
            assert metrics.contributors_by_company(20, repo_id=25432).iloc[0]['counter'] > 0
        # metric route repo tests
        def test_contributors_by_company_repo(metrics):
            response = requests.get('http://localhost:5000/api/unstable/repo-groups/20/repos/25432/contributors-by-company')
            data = response.json()
            assert response.status_code == 200
            assert len(data) >= 1
        # metric route group test
        def test_contributors_by_company_group(metrics):
            response = requests.get('http://localhost:5000/api/unstable/repo-groups/20/contributors-by-company')
            data = response.json()
            assert response.status_code == 200
            assert len(data) >= 1




