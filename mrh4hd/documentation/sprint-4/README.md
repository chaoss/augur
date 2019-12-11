# Software Engineering Group 5

Jacob Alongi, Matt Hudson, Tim Kuehner, Rebecca Parker

**Sprint 1** [here](./sprint-1)

**Sprint 2** [here](./sprint-2)

**Sprint 3** [here](./sprint-3)

**Sprint 4** is just ahead!

# Sprint 4 README

## Deployment Instructions
Our project is deployed on Matt's atmosphere server. Refer to [sprint 3's README](./sprint-3/README.md) for these links.

As far as deploying the project itself, it utlimately amounts to deploying augur itself - our project is an addition to
the API backend server, therefore it does not require any additional configuration. There are a few notes to doing this deployment that tripped us up in sprint 2, so here are the steps we took to deploy this:

- Clone this repository on a Linux server. 
- Install Augur's postgres database (install postgres too!). You can fill the database, or you can populate it with the sample data `make install` provides. You can also connect Augur to another database server by specifying the address/credentials in
`make install`.
- Create a python virtual environment with Python3. **Downgrade gunicorn to version 19.9.0.** Version 20.0 is incompatible with Augur and will prevent Augur from running properly, so you need to use `pip` to uninstall 20.0 and install 19.9.0 in its place.
- Make sure to get a GitHub API token, you'll need this for `make install`.
- Use `make install` to install Augur.
- Edit `augur.config.json`. Make sure that the `"Database"` object is set to the right database. If you're using the local
database, it should look something like this:

```json
"Database": {
        "connection_string": "sqlite:///:memory:",
        "database": "augur",
        "host": "localhost",
        "key": "<insert key here>",
        "password": "<insert user password here>",
        "port": 5432,
        "schema": "augur_data",
        "user": "augur"
    }
 ```

Then, make sure the Server object is configured correctly. For this, you need to set the IP address of the server you're running, and the port you're serving on. **Make sure to open the port in the firewall as well. Also, for our atmosphere servers, we had to set the IP address to the PRIVATE Class B address known to the server**. For example, `ip a` shows the following output:

```bash
2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc fq_codel state UP group default qlen 1000
    link/ether fa:16:3e:a0:77:9d brd ff:ff:ff:ff:ff:ff
    inet 172.21.45.11/24 brd 172.21.45.255 scope global dynamic ens3
       valid_lft 257sec preferred_lft 257sec
    inet6 fe80::f816:3eff:fea0:779d/64 scope link 
       valid_lft forever preferred_lft forever
```

Consequentally, this is the Server object in `augur.config.json`:
```json
"Server": {
        "cache_expire": "3600",
        "host": "172.21.45.11",
        "port": "5000",
        "workers": "4"
    },
```

- Lastly, use `make dev` or `augur run` to run the backend server. You can then access the endpoints using `http://<yourdomainnameorIP>:<yourport>/api/unstable/<route>/<goes>/<here>`

If that doesn't work, make sure the web server is working locally as well. Matt used `wget` to test this locally.

## Files/Code Modified
We modified the following files to add our three endpoints:<br>
(modified) [commit.py](./augur/metrics/commit/commit.py)<br>
Contains business logic for the first and second endpoints. These are the `repo_timeline` (line 201) and `repo_group_timeline` (line 215) methods, respectively.<br>
(modified) [contributors.py](./augur/metrics/contributor/contributor.py)<br>
contributors.py contains the business logic for the third endpoint. This is the `contributions` (line 571) method.<br>
(modified) [commit](./augur/metrics/commit/routes.py) and [contributor](./augur/metrics/contributor/routes.py) routes.py files <br>
Both routes.py files were updated to define the routes for all three endpoints. Routes in [commit](./augur/metrics/commit) are defined using the `server.addRepoMetric()` and `server.addRepoGroupMetric()` methods already present in Augur. The route in [contributor](./augur/metrics/contributor) is defined manually using the `@server.app.route()` annotation and defining the function `contributions` for this endpoint.<br>
(modified) test_contributor_functions.py<br>
test created to make sure the queries returned the correct values<br>
(modified) test_contributor_routes.py<br>
test created to make sure the routes correctly returned data<br>

## Completeness

Our project can use (and has used) the augur database running on the same server that runs Augur's backend server. It does not rely on endpoints outside the normal Augur environment. You could point Augur to augur's database if you want; it *should* work, because we did not edit anything regarding that configuration - we just added endpoints that access the database in the same way every other endpoint accesses the database.

## Testing

We modeled the tests for our 3 new endpoints after the existing Augur testing design for consistency. First, we created functional tests to ensure that the function will actually execute. We first mocked the metrics model and then called the new functions to test that some values were returned. 
```python
def test_repo_timeline(metrics):
    assert metrics.repo_timeline(20, 21000).iloc[0].net > 0
```

In addition, we tested the routes on the live development server to ensure that the function executes on the live server as well, returning non-empty data.
```python
def test_repo_timeline(metrics):
    response = requests.get('http://localhost:5000/api/unstable/repo-groups/20/repos/21000/repo-timeline')
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["net"] > 0
```
## Release

We created a release following the release convention. So, this release is one minor version ahead of the previous version. As is my (Matt's) understanding of this convention, it is `<major version>`.`<minor version>`.`<patch version>`, so this project is best described as a minor release.

## 16th Grade Science Fair (in-class demo)

For our demonstration, we demonstrated our endpoints running with various repos and repo groups. We used the augur repository and repogroup to demonstrate endpoints 1 and 2, and we used Dr. Goggins (s@goggins.com) as our example for Endpoint 3. We also went over some of our python code and how we got new endpoints to work, and the SQL queries we run to get that data. 

We also demonstrated the incredible power of the `sl` bash command. a.k.a if you mistype the `ls` command. It's less of a trainwreck than our finals next week.

![sl](https://www.cyberciti.biz/tips/wp-content/uploads/2011/05/sl_command_steam_locomotive-1.png)

## Feedback Incorporation

We found the endpoints to be satisfactory as they were presented in Sprints 2 and 3, as does Dr. Goggins (from Canvas):

> Good progress for sprint 2!

> Sean Goggins, Nov 30 at 6:45am

> Really great progress on the endpoints!

> Sean Goggins, Dec 1 at 2:15pm

:)

More seriously, we didn't find any feedback issues, so we focused on the demo and this README this week.

-------------------------------------
END OF SPRINT 4 README

Base Augur Readme Below (what was here before Sprint 4)

-------------------------------------
# Augur

branch | status
   --- | ---
master | [![Build Status](https://travis-ci.org/chaoss/augur.svg?branch=master)](https://travis-ci.org/chaoss/augur)
   dev | [![Build Status](https://travis-ci.org/chaoss/augur.svg?branch=dev)](https://travis-ci.org/chaoss/augur)

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2788/badge)](https://bestpractices.coreinfrastructure.org/projects/2788)

## About Augur

Augur is focused on prototyping open source software metrics.

Functionally, Augur is a prototyped implementation of the Linux Foundation's [CHAOSS Project](http://chaoss.community) on [open source software metrics](https://github.com/chaoss/metrics). Technically, Augur is a [Flask web application](http://augur.osshealth.io), [Python library](https://oss-augur.readthedocs.io/en/dev/library-documentation/python.html) and [REST server](http://augur.osshealth.io/static/api_docs/) that presents metrics on open source software development project health and sustainability.

## Getting Started

**Please follow the 'Getting Started' guide in our [documentation](https://oss-augur.readthedocs.io/en/master/getting-started/getting-started-toc.html).**

Note: we currently only support (most) UNIX systems. If you would like to use Augur but only have access to a non-Unix system, we recommend setting up an Ubuntu 18.04 VM if you can. 
If this is not feasible for you, please reach out to us at [p9j0r6s0m4a0t8v5@augurlabs.slack.com](mailto:p9j0r6s0m4a0t8v5@augurlabs.slack.com) and we will try to help you come up with a solution. In the meantime, if you have Windows and feel so inclined check out issue [#403](https://github.com/chaoss/augur/issues/403) as a starting point until we can finalize a Windows installation.

## Data Collection

Please [follow the instructions](https://oss-augur.readthedocs.io/en/master/getting-started/usage.html#db) for collecting data about specific repositories of interest. We are also currently working on putting together an easily distributable sample database to enable people to get going faster.

<!-- TODO: link to worker docs once they're done -->
<!-- If you are collecting data of your own, you must [start up the workers](./docs/setup/augur-get-workers-going.md). -->

If you have any issues, please feel free to request to email straight into our slack channel [p9j0r6s0m4a0t8v5@augurlabs.slack.com](mailto:p9j0r6s0m4a0t8v5@augurlabs.slack.com) for new developer support!!

## Contributing
----------------

To contribute to Augur, please follow the guidelines found in our [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md). Augur is a welcoming development community that is open to anyone and everyone of every skill level!

Check out our [documentation](https://oss-augur.readthedocs.io/en/documentation/) for information about our system.

Please note we require all commits to be signed off with a [Developer Certificate of Origin](https://developercertificate.org/) in accordance with the [CHAOSS Project Charter section 8.2.1](https://chaoss.community/about/charter/#user-content-8-intellectual-property-policy). This can be easily done by using the `-s` flag when using `git commit`, e.g. `git commit -s -m "Update README.md"`. **Any pull request containing commits that are not signed off will not be eligible for merge until all commits are signed off.** 

## License, Copyright, and Funding
----------------

Copyright © 2019 University of Nebraska at Omaha, University of Missouri and CHAOSS Project at the Linux Foundation

Augur is free software: you can redistribute it and/or modify it under the terms of the MIT License as published by the Open Source Initiative. See the [LICENSE](LICENSE) file for more details.

This work has been funded through the Alfred P. Sloan Foundation.
