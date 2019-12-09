# Augur Repo Location Tool (ARLT)

## About ARLT

Augur is focused on prototyping open source software metrics.

Functionally, Augur is a prototyped implementation of the Linux Foundation's [CHAOSS Project](http://chaoss.community) on [open source software metrics](https://github.com/chaoss/metrics). Technically, Augur is a [Flask web application](http://augur.osshealth.io), [Python library](https://oss-augur.readthedocs.io/en/dev/library-documentation/python.html) and [REST server](http://augur.osshealth.io/static/api_docs/) that presents metrics on open source software development project health and sustainability.

The Augur Repo Location Tool utilizes Augurs basic functionalities in order to display where different contributors of a repository are located. 

## Installation and Deployment
These instructions are for mac, ubuntu, or other linux based systems.

***Clone Repository***
1. Clone this repository into your server's public html folder.

***Alter API calls***
2. Inside the repository, navigate to the sprint4 directory
3. Alter all API calls to a URL of the form 'http://129.114.104.67:5000/api/unstable/..." to reflect your DNS.

These API calls can be found in the following files:
  * repoNames.js
  * sprint3.js

***Install Augur***
4. Set up and activate your python virtual environment.
3. Run the following command inside the main repository to install Augur.
```
make install
```
4. During installation, set up the psql database using the provided sample data.
5. Create a new table in the augur_data schema called 'dummy_contributors' using the data provided in 'dummy_contributors.xlsx'. 

***Run Augur***

6. Run Augur with the following command:
```
nohup augur run >augur.log 2>augur.err &
```

note: Augur can be killed by running:
```
augur util kill
```

***View Front-end***

7. To view the front-end code, navigate to [your_domain]/sengfs19-group10/sprint4/login.html

Username is 'User'

Password is 'Pass'

note: This application currently only works for HTTP servers. 
