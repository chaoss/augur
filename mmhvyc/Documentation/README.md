# Sprint 2


#### Sam
For this sprint, I focused on creating a new working API call which will eventually be used to provide the latitude and longitude of contributors to a repo/repo group.  To achieve this, I followed the metric creation guide in the augur documentation, using their provided SQL query for practice.  I ended up with two files, a contributor-location.py file which defines the new metric, and a routes.py file, which creates the endpoint.  I also used my server to create and deploy my own instance of augur.  Althouh I was able to follow all the instructions successfully, the web app will not load when you try to access it.  I assume this is because of the issues we're facing right now with the servers.

#### Michelle
I created a menu layout including all the repo groups in augur and a brief description of the projects. The future function of this is for the user to click on the repo group and the map will display the locations of the contributors in that repo group. It's still TBD if each repo group will have their own tab/page. I pinned Columbia, MO on the map to demonstrate the understanding of the Google Maps function.

#### Matthew
I am working on a metric that analyzes test coverage for repositories. The goal is to build a visual for the user to be able to clearly see how much each repo has been tested. I have written out the SQL query and python code but have not fully tested yet.

#### Sweta
The user selects the project it wants to see the metric: organizational diversity through a drop-down box that populates all the project groups from the Augur server(from index.html).The user sees the organizational diversity that is Ratio of contributors from a single company over all contributors, also described as: Maintainers from different companies,Diversity of contributor affiliation.I plan to show the data in form of dough-nut chart using Google charts.For now I have used small raw data on my own.
Understanding the Visualization:
A pie chart is rendered within the browser using SVG or VML,displays tooltips when hovering over slices.
master
