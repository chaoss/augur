# Website Description
The first page will have a navbar at the top of the page that will include
a home button, as well as 3 separate tabs for augur information that is
different than the information for the repo groups and repos(additional augur
information). Below the navbar there will be a list of repo groups included
in augur. The list of repo groups will be incapsulated in a card, which states
information about that group, such as it's name, it's purpose, and the date it was
last modified. By clicking a specific repo group, the user will be redirected to 
a new page. 
  
This second page will show information specific to the repo group as well as a list
of repos that are included in that group. Once again the repo data will be 
on a card that gives the user information about the repo, to give them insight and 
help with a search if they are looking for something specific. From there the user can 
select a repo associated with that repo group. 
  
This will take them to a third page that displays a dropdown menu of 
information the user would like to see in that repo.
By choosing an information item from the dropdown menu, a graphic will appear
that visually shows the information the user picked from that repo. This 
information comes from specific API endpoints associated with augur that will
be parsed into Javascript objects then displayed graphically. Data could be 
displayed in different ways, depending on what kind of information the endpoint
contains. Some visualizations of the data selected may just be more cards to provide
a visualization of text that is easy to see and comprehend. Other data may need a more
graphical representation, such as a line or bar graph. This visual representation may 
vary based on the info selected. If an endpoint does not contain any data or is 
malfunctioning, an error message will be displayed to alert the user that the data
could not be found.

# We plan to use include this augur data if there is enough data in each:
1. Repo Groups
2. Repos
3. Sub Project Count
4. Abandoned Issues
5. Contributors
6. Pull Request Acceptance Rate
7. Active Issues
8. Commits Over Time
