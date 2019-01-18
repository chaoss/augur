Docker Installation
==================================

Before we begin, make sure you have everything you need installed:
`Git <https://git-scm.com/downloads>`__,
`Docker <https://www.docker.com/community-edition>`__, `Docker
Compose <https://docs.docker.com/compose/install/>`__

`*Also remember the database dependency in the README.md
file* <http://ghtorrent.org/msr14.html>`__

Now, to install:

1. Clone the repo and enter its directory:

.. code:: bash

    git clone https://github.com/chaoss/augur
    cd augur

2. Set the following variables in your environment:

.. code:: bash

    #Most likely required
    AUGUR_DB_USER
    AUGUR_DB_PASS
    AUGUR_DB_HOST
    AUGUR_DB_PORT
    AUGUR_DB_NAME
    AUGUR_GHTORRENT_PLUS_USER
    AUGUR_GHTORRENT_PLUS_PASS
    AUGUR_GHTORRENT_PLUS_HOST
    AUGUR_GHTORRENT_PLUS_PORT
    AUGUR_GHTORRENT_PLUS_NAME
    AUGUR_GITHUB_API_KEY

    # Optional
    AUGUR_HOST
    AUGUR_PORT
    AUGUR_PUBLIC_WWW_API_KEY
    AUGUR_LIBRARIESIO_API_KEY

::

    docker-compose will automatically pass the relevant variables from the local environment to the container.

3. Build the container with ``docker-compose build``
4. Launch the container with ``docker-compose up``
