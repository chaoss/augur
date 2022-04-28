BRUINS GITHUB AUGUR REPO SUBMISSION TOOL / SPRINT 3

SPRINT 3 updates are listed below the app steps to test section

GOGGINS / TA - STEPS TO RUN / TEST / VIEW / PROJECT

1 Install NodeJS and NPM from https://nodejs.org.

2 git clone https://github.com/k1nty/Bruins-augur.git

3 cd Bruins-augur/

4 git checkout sprint3

5 cd Sprint3ProjectSourceCode/

6* npm install

7** npm start

*) Install all required npm packages by running npm install or npm i from the command line in the project root folder (where the package.json is located).

**) Start the app by running npm start from the command line in the project root folder, this will compile the app and automatically launch it in the browser on the URL http://localhost:4200.

CREDIT - 

This frontend was modified from the below reference / repo
The code was originally cloned from the jasonwatmore repo, some modifications were made to make it better suit our project

APPLICATION - 

This frontend application uses a combination of HTML, CSS, JavaScript, TypeScript, Bootstrap, and Angular
As it is a Angular app there is no true backend database, the app runs entirely in the browser simulation a full stack app

angular-10-registration-login-example

Angular 10 - User Registration and Login Example

https://github.com/cornflourblue/angular-10-registration-login-example

https://jasonwatmore.com/post/2020/07/18/angular-10-user-registration-and-login-example-tutorial




Sprint 3 Updates:

This project’s goal is to give users a frontend platform to easily submit GitHub repos to be assessed by Augur. User’s will need to login to the frontend application with a username and password. Users can then submit a GitHub repo to be assessed by Augur

Requirements document updated /

Test document added

Source code for frontend added




AUGUR --

standard-readme compliant
branch 	status
main 	Build Status
dev 	Build Status

CII Best Practices
What is Augur?

Augur is a software suite for collecting and measuring structured data about free and open-source software (FOSS) communities.

We gather trace data for a group of repositories, normalize it into our data model, and provide a variety of metrics about said data. The structure of our data model enables us to synthesize data across various platforms to provide meaningful context for meaningful questions about the way these communities evolve.

We are a CHAOSS project, and many of our metrics are implementations of the metrics defined by our awesome community. You can find more information about how to get involved on the CHAOSS website.
Collecting Data

One of Augur's core tenets is a desire to openly gather data that people can trust, and then provide useful and well-defined metrics that help give important context to the larger stories being told by that data. We do this in a variety of ways, one of which is doing all our own data collection in house. We currently collect data from a few main sources:

    Raw Git commit logs (commits, contributors)
    GitHub's API (issues, pull requests, contributors, releases, repository metadata)
    The Linux Foundation's Core Infrastructure Initiative API (repository metadata)
    Succinct Code Counter, a blazingly fast Sloc, Cloc, and Code tool that also performs COCOMO calculations

This data is collected by dedicated data collection workers controlled by Augur, each of which is responsible for querying some subset of these data sources. We are also hard at work building workers for new data sources. If you have an idea for a new one, please tell us - we'd love your input!
Getting Started

If you're interested in collecting data with our tool, the Augur team has worked hard to develop a detailed guide to get started with our project which can be found in our documentation.

If you're looking to contribute to Augur's code, you can find installation instructions, development guides, architecture references (coming soon), best practices and more in our developer documentation. Please know that while it's still rather sparse right now, but we are actively adding to it all the time. If you get stuck, please feel free to ask for help!
Contributing

To contribute to Augur, please follow the guidelines found in our CONTRIBUTING.md and our Code of Conduct. Augur is a welcoming community that is open to all, regardless if you're working on your 1000th contribution to open source or your 1st. We strongly believe that much of what makes open source so great is the incredible communities it brings together, so we invite you to join us!
License, Copyright, and Funding

Copyright © 2022 University of Nebraska at Omaha, University of Missouri and the CHAOSS Project.

Augur is free software: you can redistribute it and/or modify it under the terms of the MIT License as published by the Open Source Initiative. See the LICENSE file for more details.

This work has been funded through the Alfred P. Sloan Foundation, Mozilla, The Reynolds Journalism Institute, contributions from VMWare, Red Hat Software, Grace Hopper's Open Source Day, GitHub, Microsoft, Twitter, Adobe, the Gluster Project, Open Source Summit (NA/Europe), and the Linux Foundation Compliance Summit. Significant design contributors include Kate Stewart, Dawn Foster, Duane O'Brien, Remy Decausemaker, others omitted due to the memory limitations of project maintainers, and 12 Google Summer of Code Students. 
