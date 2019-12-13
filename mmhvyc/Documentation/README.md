# Sprint 3

- To view the website work completed for sprint 3, you can go to http://129.114.16.76:8080/home.html .  This code is located in the "website" directory in this repo.

- To view the api endpoints completed for sprint 3, you can go to http://129.114.16.76:5000/api/unstable/repo-groups/10/contributor-affiliation , http://129.114.16.76:5000/api/unstable/repo-groups/20/committer-data , and http://129.114.16.76:5000/api/unstable/repo-groups/20/testing-coverage ("20" within these links can be substitued for 10, the other sample repo group in the sample data).  This code is located in the "augur/metrics" directory in this repo.


## Michelle
- Originally had plans for repo groups in augur, but the data had other plans... We discovered that only sample data for three repo groups were available. Therefore, our options were to create a large amount of fake data or implement the three repo groups with existing APIs
- Before the turn of events, I tranferred previous code to a bootstrap template, gathered logos for the repo groups, and created a layout for the data visualizations to be displayed.
- Not many changes had to be made design wise at the last minute, just concepts
- Next steps will be to display repo group and repository information, pinning multiple markers, and changing the meter gauge to a circular format
- We have the data for these displays but the visualizations took precedence 

## Samantha
For this sprint, I produced two working API endpoints: committer-data and contributor-affiliations.  I also create function and route tests for each new metric.  This code can be found in the the "augur/metrics/contributor" and "augur/metrics/commit" folders.
### committer-data:
This metric mainly returns the unique full names of all the contributors in a repo group, including a prediction of the person's gender.  This prediction is created by iterating through the SQL response and calling the NamSor API on each name.  This new data is appended to the response and then supplied to the endpoint.  This will be used to illustrate the possible gender distribution of the committers to a repository group.  [Try it out here.](http://129.114.16.76:5000/api/unstable/repo-groups/20/committer-data)
### contributor-affiliation:
This metric returns information on the contributors to a repo group, including their github username, profile url, company affiliation, and location.  Using the location information and the Google Geocoding API, latitude and longitude corrdinates for the user are generated for use with the map visualization.  These results are appended to the SQL response and then supplied to the endpoint.  This will be used to give descriptions on the contributors to a repository group.  [Try it out here.](http://129.114.16.76:5000/api/unstable/repo-groups/20/contributor-affiliation)

## Matthew
For this sprint I created my testing coverage metric. It can be found in the augur/metrics/insight folder. When I got the json response, there was no data being displayed without any errors, so we will probably need to manually put in data into the augur sample database. I also wrote tests for the function the routes, but I am not sure how effective these tests are because I did not have any previous examples to draw from from the insight folder in augur. 
