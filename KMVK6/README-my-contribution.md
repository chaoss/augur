# Kyle Malisos contributions to group 4 project.

## Design Document Additions.

I added the metric functionality and description of the Entrance Difficulty metric. This also included creating a use case diagram for the metric. This metric was unfortunately replaced by another metric due to a lack of database data the metric required so it is not in our current design document.

I also was responsible in part for making additions to the Design document as we updated the document with a new metric and changes to our old metrics.

## Augur Contributions.

1. During sprint two I added the required routes in the routes.py file for all metrics except the one we had to have working.

2. In sprint three I worked in conjunction with Max Balk to create the issue-response-time metric which made an average of the time to respond to an issue for all issues within a metric. The main work we had to do in creating this metric was to create an SQL query that would select and average the appropriate data from the database. Then we used this query to implement the metric into the issues.py folder using the same format as the other metrics.

3. Also during sprint three I created all of the tests for the issue-response-time metric within the test_issue_functions.py that made sure the metric will return data and that it is correct. I also added the testing for the metric route within the test_issue_routes.py for this metric as well.

4. During sprint four I worked with other members of our group to create the README.md file for the sprint that discussed our additions to augur. I also created the deployment instructions of how to download and run our project and how to use the endpoints we created in the README.md document. I was also responsible for making the release of our project on GitHub.