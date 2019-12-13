# Sprint 1

### Overall Goals:
#### Front-end:
1. Allow more user interaction with maps and search functions
2. Contributor location
  * Integrate Google Maps on website
  * Users will pick a repository group through a selection box or module which will then pin all contributors within that repository group on the map
  * Clicking on pins will return the contributor’s profile
3. Contributor occupation
  * These will be merged with the concept of contributor locations
  * The contributor’s profile will include their occupation, company, start date, and activity
4. Pictures will attempt to be added in profiles and to the database itself
  * Company logos will be used at the very least
#### Back-end:
1. Design and implement new metrics for determining code health for the Augur project.
  * Create a metric that evaluates the current test coverage of the code base within the repository.
  * Create a metric that predicts the gender and ethnic diversity of the committers to a repo using predictions based on the NamSor API.
2. Employ auxiliary APIs/tools to create more robust and cutting edge metrics.
3. Create endpoints for the Augur API for accessing the results of the new functions.
4. Write code that conforms to the existing stylistic and design standards of the Augur project.

### Use-Case Diagrams:
1. Contributor Occupation <br />
![Contributor Occupation](https://github.com/computationalmystic/sengfs19-group11/blob/master/sprint-1/customerOccupation.png)
2. Contributor Location <br />
![Contributor Location](https://github.com/computationalmystic/sengfs19-group11/blob/master/sprint-1/customerLocation.png)
3. Testing Coverage <br />
![Testing Coverage](https://github.com/computationalmystic/sengfs19-group11/blob/master/sprint-1/testCoverage.png)
4. Gender and Ethnic Diversity Among Committers <br />
![Gender and Ethnic Diversity Among Committers](https://github.com/computationalmystic/sengfs19-group11/blob/master/sprint-1/contributorDiversity.png)

### Augur Data Needed:
1. Contributor Occupation:
  * Augur_data.contributors: cntrb_company
  * Augur_data.contributor_affiliations: ca_affiliation
  * Augur_data.contributor_affiliations: ca_start_date
2. Contributor Location:
  * Augur_data.contributors: contrb_long
  * Augur_data.contributors: contrib_lat
3. Testing Coverage:
  * Augur_data.repo_test_coverage: file_subroutine_count
  * Augur_data.repo_test_coverage: file_subroutines_tested
  * Augur_data.repo_test_coverage: file_statement_count
  * Augur_data.repo_test_coverage: file_statements_tested
  * Augur_data.repo_test_coverage: testing_tool
4. Gender and Ethic Diversity Among Committers 
  * Augur_data.commits: cmt_author_name
  * Augur_data.commits: cmt_ght_committer_id
  * Augur_data.commits: repo_id

### Languages Needed:
* Python
* SQL
* HTML
* CSS
* Javascript

On our team, for each language, there is at least one member who has experience with it.  For those who don’t, beyond asking for help from the other team members, examples of how to use these languages can be found on several sites.  For the front end, [Twitter’s Year In Review](https://github.com/twitter/twitter.github.io) site demonstrates an easy to decipher and dynamic web design.  For the backend, Augur provides a [detailed tutorial](https://oss-augur.readthedocs.io/en/master/getting-started/create-a-metric/create-a-metric-toc.html) on how to create a new metric and endpoint for their API.  Live examples of this can be found on the [Augur repo](https://github.com/chaoss/augur/tree/master/augur/metrics).  By imitating these examples, we will be able to understand and use these languages to contribute to the project.

### Design Document:
[Github link](https://github.com/computationalmystic/sengfs19-group11/blob/master/Group%2011%20Design%20Doc.pdf)

