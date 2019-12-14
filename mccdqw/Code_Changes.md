## Group 11 - Final Project

For our project, we created three new API endpoints: [contributor-affiliation](http://129.114.16.76:5000/api/unstable/repo-groups/20/contributor-affiliation), [committer-data](http://129.114.16.76:5000/api/unstable/repo-groups/20/committer-data), and [testing-coverage](http://129.114.16.76:5000/api/unstable/repo-groups/20/testing-data).  We also created a website to view these new metrics, at http://129.114.16.76:8080/home.html .

### Installation 
1. Clone this repository into a local directory using `git clone https://github.com/computationalmystic/sengfs19-group11.git`
2. Follow the 'Getting Started' guide in the Augur [documentation](https://oss-augur.readthedocs.io/en/master/getting-started/getting-started-toc.html) to set up out Augur version, stopping before `make install`.
3. Ensure your virtual environment has been activated and uses python 3.
4. Run `pip uninstall gunicorn`, then run `pip install gunicorn==19.9.0`.
5. Run `make install`, opting to install the database schema, load the sample data, and not install front-end dependencies.
6. Using the database created following Augur's installation guide, enter into the database using `psql`, and add new data into the database using the commands `insert into augur_data.repo_test_coverage(repo_id, file_subroutines_tested, file_subroutine_count, file_statements_tested, file_statement_count) values (25430, 124, 154, 254, 304)` and `insert into augur_data.repo_test_coverage(repo_id, file_subroutines_tested, file_subroutine_count, file_statements_tested, file_statement_count) values (25432, 354, 354, 463, 602)`
7. Run `make install` again
8. To start the API server, run `augur run --no-enable-housekeeper`

You may now access your API endpoints on your localhost at port 5000, for instance using http://localhost:5000/api/unstable/repo-groups/20/committer-data 

1. In a separate terminal windown, naviage into /sengfs19-group11/website
2. Ensure your virtual environment is activated.
3. run `python3 server.py`

You may now access your website at http://localhost:8080/home.html

### Changed/Added Files
1. created `/website` directory to house the code for our front end, which contains `home.html`, `one.html`, `two.html`, `ethnicities.html`, `navbar.html`, `augur.css`, `testData.js`, `contributorData.js`, `committerData.js`, and `server.py`
2. changed `commit.py`, `routes.py`, `test_commit_functions.py`, and `test_commit_routes.py` in `/augur/metrics/commit` directory to add the committer-data API endpoint
3. changed `contributor.py`, `routes.py`, `test_contributor_functions.py`, and `test_contributor_routes.py` in `/augur/metrics/contributor` directory to add the contributor-affiliation API endpoint
4. changed `insight.py`, `routes.py`, `test_insight_functions.py`, and `test_insight_routes.py` in `/augur/metrics/insight` directory to add the testing-coverage API endpoint
5. created `sprint-1`, `sprint-2`, `sprint-3`, and `sprint-4`directories to contain all class materials
6. created `Group 11 Design Doc.pdf` 

### Testing
#### Back End
Function and route tests were written for all three new metrics.  To verify your functions are working correctly:
1. Activate your virtual environment (ex: `source augur_env/bin/activate`)
2. Run `pip install pytest-timeout`
3. Navigate into the `sengfs19-group11` directory
4. Run the tests for your desired metric:
- committer-data: 
1. `pytest augur/metrics/commit/test_commit_functions.py::test_committer_data`
2. `pytest augur/metrics/commit/test_commit_routes.py::test_committer_data --timeout=300`
- contributor-affiliation:
1. `pytest augur/metrics/contributor/test_contributor_functions.py::test_contributor_affiliation`
2. `pytest augur/metrics/contributor/test_contributor_routes.py::test_contributor_affiliation`
- testing-coverage
1. `pytest augur/metrics/insight/test_insight_functions.py::test_testing_coverage`
2. `pytest augur/metrics/insight/test_insight_routes.py::test_testing_coverage`

#### Front End
1. The maps should populate with pins at contributor locations when opening the home page. Locations can be confirmed by viewing the contributors' city in the location API.
2. The pie charts and table in each repo group will appear after a load time. This can again be confirmed by comparing the diversity API against the table.
3. The testing coverage meters are easily checked with doing a percentage calculation from the API.

