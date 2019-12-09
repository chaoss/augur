# Sprint 2: Beginning Deployment

### Deployment server link: [http://129.114.104.224/](http://129.114.104.224/)

For this sprint, we created the first basic components of our Augur Informatics application UI. 
So far we have generated an Angular application that can read two of the most important Augur API endpoints, 
repository groups and specific repositories. It displays the data retrieved using Boostrap UI elements, to 
create a simple and easy understand design for the user. Clicking on those data elements will navigate you 
through the different pages of the application. We have a third page set up, in which we will add and
display the more detailed information about a selected repository, but this will be added in the near future. 
For now a banner is displayed to let the user know that they have reached that page, and more details will be coming
soon.

The UI code was then deployed on a Ruby on Rails backend server, which
hosts the application. By clicking on the link provided, you can view our
frontend application in it's current state. In the future, we hope to use the 
ruby on rails backend capabilities to read the api endpoints and cache the data
received, so the application does not have to fetch all that information
each time the page is loaded. This will add to the efficiency and speed
of our design. 

We have included a description of our UI design in the markdown document
above. This document describes in detail how our application will look and 
function. Design elements that have already been added to the application as
well as elements that will soon be implemented are described there.
  
Frontend and Ruby on Rails code/setup are included on the master branch under
the group-frontend and RubyOnRails folders




