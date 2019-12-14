# Final Sprint

In this sprint, we got three API endpoints working, wrote tests for the endpoints (all in the contributor directory test files), connected the front-end to these apis, and added and modified functionality to the front-end.

### Endpoints
For the endpoints, we completed the repo and repo_group API endpoints for committers-locations, issue-locations, and pull-request-locations. Each endpoint gives the contributor id, latitude, longitude, city, and state of anyone who made a commit, issue, or pull-request on a given repo. Because location data was sparse, to make these endpoints we created a new table 'dummy_contributor' with the cntrb_id and cntrb_email using 99 records from the real contributors table. Then, we filled this table with random latitude and longitudes using the random() function. Lastly, we manually found the city and state for each latitude and longitude in the table.

To write the endpoint tests, we added to test_contributor_function.py and test_contributor_routes.py by copying the basic pattern of each test for each of the endpoints. Values and attributes were modified to fit the specific endpoints. 

### Front-End
For the front-end, the page opens to a Login Page. The user should login as Username: "User" and Password: "Pass". After login, the user is directed to an Interactive Map home page. 

In the leftmost Selection Section, the user can select a state and the map will zoom to the selected state and display its contributor locations.

The Map loads with a display of the contributor locations found at the API endpoints.

The Search Bars on the righthand-side are completely functional. The city search and zip code search will zoom to wherever on the map you search if it exists and if it doesn't then the API handles the error checking for us by returning a code or giving its' best guess as to what you are searching for.

The Statistics Section is completed. It returns information about the contributor pinpoints on the map.

The Repo Return button returns a list of all contributors, by their ID. 

The Regional Contributor Pie Chart is partially functional. The display is correct, but information needs to be pulled correctly from the API to display accurate information on the contributor's locations.

There are clickable markeres on the map that should tell you unique things about each of the markers.
