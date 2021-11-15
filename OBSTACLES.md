Obstacles
-----------------------------------------------------------------------------------------------------------------------------------------
November 14 2021

When trying to deploy the augur fork onto an Ubunto instance, there were many issues that prevented the deployment.
The provided instructions as part of the class had many parts where the sequence wouldn't allow further pogression.
Using the quick settup, https://oss-augur.readthedocs.io/en/main/, as an example:

When creating a PostgreSQL database for Augur to use, there were issues with the commands. 
psql -h localhost -U postgres -p 5432 wouldn't work since the user postgres, being something that I hadn't touched before as this was a presented instruction,
required a password that I would need to provide. As I had nothign to do with the user postgres, I instead opted to use the command: psql -h localhost
This then lead to the system asking for the password to my user dvin.hackman. However, it would seem that none of the passwords for my own user worked.
It turned out that I had to log into PostgreSQL as a root user and set the password for postgres.

Yet after all of this, when I finally got throug and even enabled git, there came a problem when it was time to use the sudo apt make command.
Specifically the error "Invalid operation make." I know that this was an issue that wasbrought up in class, but as far as I can remember this 
was used as an example of other issues that arrized when people were trying to get Augur to work. The instructor said that there woul be a 
video posted that would explian how to install augur into a server and get it working, but that so far hasn't appeared. As such, our team has gotten stuck 
in terms of getting the a deployable instance.

In the near future I will work with the professor to get this instance deployed, but until then, its'g going to have to go unfulfilled.

-------------------------------------------------------------------------------------------------------------------------------------------

