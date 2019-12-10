# Design Document Group 3 <br><br> Created by Graeson, Zachanry, Guangzu

### what is necessary for your use cases to lead into a solution

### Use Case:
1. https://github.com/computationalmystic/sengfs19-group3/blob/master/Sprint-1/Design-Document/use%20case%201.jpg
2. https://github.com/computationalmystic/sengfs19-group3/blob/master/Sprint-1/Design-Document/use%20case%202.jpg
3. https://github.com/computationalmystic/sengfs19-group3/blob/master/Sprint-1/Design-Document/use%20case%203.jpg

### Wireframes:
repo link:https://github.com/computationalmystic/sengfs19-group3/blob/master/Sprint-1/Design-Document/Repo-page.jpg <br>
repo group link:https://github.com/computationalmystic/sengfs19-group3/blob/master/Sprint-1/Design-Document/Repo-group-page.jpg<br>
info word version link:https://github.com/computationalmystic/sengfs19-group3/blob/master/Sprint-1/Design-Document/Info-page.jpg<br>

### Data source
  
    - Augur contributors data
    - Augur repo group data
    - Augur issues data 
    - Augur contributors data
    - Augur commits data

### Functions

    - Create contributors-by-company and messages-by-contributor API endpoints
    - Be able to display that data on a webpage using Angular
    - search data for specific repo groups and repos within those groups 
    - show the API endpoint's data display in a table 

### how the different software components communicate 
    List of the software component
    - Augur
    - Postgresql database
    - Angular Webpage
    - All of Augur's plugins
    - Data Access tables created in postgresql database from SQL queries implemented with metric functions
    - Python3.0+ 
    - Python virtual environment
    
    - User can see the list of the request they can do in application by different pages on website.
    - Data Access objects set up the data structure created from metric endpoints
    - User can choose the request from the list.
    - Models handle request and data processing.
    - Controller receive request to call metric function from metric route (Plugins).
    - Services save the data
    - Application can get data (data structure from data Access object) from serveice by calling Api 
    
    

### Document the reasons for your decision where you have choices in desgin
  
    - The information displayed in Augur's website is a little buggy.
    - The website will show different information from the endpoints created
    - Create a useful API endpoint that could be implemented in the form of a table.
    
### Links to Endpoints and Website
* [Link for Contributors by Company API Endpoint](http://129.114.104.142:5000/api/unstable/repo-groups/20/contributors-by-company)
* [Link for Messages by Contributor API Endpoint](http://129.114.104.142:5000/api/unstable/repo-groups/20/messages-by-contributor)
* [Link for Website Displaying Messages by Contributor API Endpoint](http://129.114.104.142:4250/messages/20)
* [Link for Website Displaying Contributors by Company API Endpoint](http://129.114.104.142:4250/contributors/20)
* [Link for Website Displaying the Number of Committers for each Repo](http://129.114.104.142:4250/repo)










