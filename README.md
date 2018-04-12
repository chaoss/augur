# GHData

branch | status
   --- | ---
master | [![Build Status](https://travis-ci.org/OSSHealth/ghdata.svg?branch=master)](https://travis-ci.org/OSSHealth/ghdata)
   dev | [![Build Status](https://travis-ci.org/OSSHealth/ghdata.svg?branch=dev)](https://travis-ci.org/OSSHealth/ghdata)

GHData is a Python library and REST server that provides data related to GitHub repositories. Hosting the GHData project requires a copy of the [GHTorrent database](http://ghtorrent.org/downloads.html).

GHData is under heavy development; expect frequent backwards-incompatible changes until a 1.x.x release!



Roadmap
-------
This project is a software prototype implementation of CHAOSS Metrics. The process for defining new metrics is located here: https://github.com/chaoss/metrics 

Our technical, outreach, and academic goals [roadmap](https://github.com/OSSHealth/ghdata/wiki/Release-Schedule).



Installation with Docker (easy to get up and running)
------------------------
Before we begin, make sure you have everything you need installed: [Git](https://git-scm.com/downloads), [Docker](https://www.docker.com/community-edition), [Docker Compose](https://docs.docker.com/compose/install/), and a MySQL server with [GHTorrent](https://github.com/gousiosg/github-mirror/tree/master/sql) loaded.

Now, to install:

1.  Clone the repo and enter its directory:

    ```bash
    git clone https://github.com/OSSHealth/ghdata
    cd ghdata
      ```


2.  Set the following variables in your environment:

    ```bash
    # Most likely required
    GHDATA_DB_USER
    GHDATA_DB_PASS
    GHDATA_DB_HOST
    GHDATA_DB_PORT
    GHDATA_DB_NAME

    # Optional
    GHDATA_HOST
    GHDATA_PORT
    GHDATA_PUBLIC_WWW_API_KEY
    GHDATA_GITHUB_API_KEY
    GHDATA_LIBRARIESIO_API_KEY
    GHDATA_DEBUG
    GHDATA_GHTORRENT_PLUS_USER
    GHDATA_GHTORRENT_PLUS_PASS
    GHDATA_GHTORRENT_PLUS_HOST
    GHDATA_GHTORRENT_PLUS_PORT
    GHDATA_GHTORRENT_PLUS_NAME
    ```

    docker-compose will automatically pass the relevant variables from the local environment to the container.


3.  Build the container with `docker-compose build`
4.  Launch the container with `docker-compose up`



Installation without Docker (recommended for developers)
---------------------------
### Dependencies
- Python 3.4.x/Python 2.7.x and `pip`
- Static web server such as nginx or Apache
- a MySQL 5.x database or later with the [GHTorrent database](http://ghtorrent.org/)
  - You can use the [MSR14 dataset](http://ghtorrent.org/msr14.html) for testing
  - Our Development team has a public read only database you can request access to
  - If you want to install your own copy of the MSR14 dataset [Installation instructions](https://github.com/gousiosg/github-mirror/tree/master/sql)
- a MySQL 5.x database with write access

After restoring GHTorrent (or msr14) to MySQL, it is recommended you create a user for GHData. GHData only needs `SELECT` privileges.

Once the database is set up, clone GHData
```bash
git clone https://github.com/OSSHealth/ghdata/
cd ghdata && pip install -U .
```
Copy the files in [ghdata repo]/frontend/public to your webserver:

Run `ghdata` to create the configuration file (ghdata.cfg). Edit the file to reflect your database credentials.

Run `ghdata` to start the backend. Visit your front


Developer Installation
----------------------

### Dependencies
- Python 3.4.x and Python 2.7.x with `pip2` and `pip3`
- MySQL 5.x or later with the [GHTorrent database](http://ghtorrent.org/)
  - You can use the [MSR14 dataset](http://ghtorrent.org/msr14.html) for testing
- NodeJS 7.x or newer

#### Ubuntu
```
   ## Python Installs on UBUNUTU
   sudo apt-get install python-pip
   sudo apt-get install python3-pip

   ## For Development you need NodeJS
   sudo apt-get install nodejs
```

First, clone the repo and checkout the dev branch:

```bash
git clone https://github.com/OSSHealth/ghdata/ && cd ghdata && git checkout dev
```

Install the Python and Node developer dependencies:
```bash
make install-dev
```

For futher instructions on how to add to GHData, here are guides to adding an endpoint to the full stack. 

[Dev Guide Part 1](docs/dev-guide-pt1.md) 

[Dev Guide Part 2](docs/dev-guide-pt2.md)

Frontend development guide coming soon!

You're good to go. You can start a single instance of the API by running `ghdata`. Run `make dev-start` to start both the Brunch server and Gunicorn server for full-stack development.

The screen sessions can be killed with `make dev-stop`

License and Copyright
---------------------
Copyright © 2018 University of Nebraska at Omaha, University of Missouri and CHAOSS Project at the Linux Foundation

GHData is free software: you can redistribute it and/or modify it under the terms of the MIT License as published by the Open Source Initiative. See the file [LICENSE](LICENSE) for more details.

(This work has been funded through the Alfred P. Sloan Foundation)
