CS4320 Software Engineering
Group 1: Ashton Hess,

Fetching Data by Email: Endpoints

Description:
The use case for adding these endpoints to Augur is to give the user the ability to search certain metrics by email. By adding these endpoints to query the database by, this addition expands the user’s flexibility in selecting search terms to query information about a specific user. Expanding the database’s ability to handle searching information on specific users also provides more information that could be displayed on the frontend or extrapolated to provide the user more specific information. 

Triggers:
When a user wants to pull specific information from the database pertaining to a specific email.
Could be used at program startup to populate information that is displayed to the user. This could be charts, graphs, lists, etc. 

Actors:

Preconditions:
The database must have information stored in the tables pertaining to the searches and the user’s emails. 

Main Success Scenario (goals):
Produce useful data for the user about certain emails and comments given by that specific email.

Alternate Success Scenarios:


Failed End Condition (“crashes” is not a failed end condition. “User is unable to discern the difference between two projects because they are similar on the available indicators” might be).: 
Users share privacy concerns related to their accounts email. If users are uncomfortable with their account emails being used this way, this would cause a failed end condition. 

Extensions:

Steps of Execution (Requirements):

A Use Case Diagram (following the UML Standard for expressing use cases):

Dependent Use Cases:
One use case that could depend on these data endpoints is a UI element or anything on the front end that shows statistics pertaining to a user’s email. 
Another use case that could depend on these data endpoints is if Augur was used to monitor the work done by specific users on a project, the project manager could search users by email to see specific information about that user. 
