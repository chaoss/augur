Database setup
===============

One of the reasons that Augur is so powerful is because of its `unified data model <../schema/data-model.html>`_.
In order to ensure this data model remains performant with large amounts of data, we use PostgreSQL as our database engine. 
We'll need to set up a PostgreSQL instance and create a database, after which Augur can take care of the rest.
Make sure to save off the credentials you use when you create the database, you'll need them again to configure Augur.

First, make sure you have all the necessary packages for building Augur:

.. code-block:: bash

        sudo apt update
        sudo apt upgrade
        sudo apt install software-properties-common
        sudo apt install python3-dev
        sudo apt install build-essential

PostgreSQL Installation
~~~~~~~~~~~~~~~~~~~~~~~~

Before you can install our schema, you will need to make sure you have write access to a PostgreSQL 10 or later database. If you're looking for the fastest possible way to get Augur started, we recommend use our `database container <../docker/docker.html>`_. If you're looking to collect data long term, we recommend following the rest of this tutorial and setting up a persistent PostgreSQL installation.

.. warning::

    If you want to collect data over the long term, we strongly advise against `using a Docker container for your database <https://vsupalov.com/database-in-docker/>`_.

If you're a newcomer to to PostgreSQL, you can follow their excellent instructions `here <https://www.postgresql.org/docs/12/tutorial-install.html>`_ to set it up for your machine of choice, or use the following commands to install it.

.. code-block:: bash

        $ sudo apt install postgresql postgresql-contrib postgresql-client
        
There should be a command for starting your database server in the output of the above command (for example, ``pg_ctlcluster 12 main start``). Switch to the postgres user and run it.

.. code-block:: bash

        $ sudo su - postgres
        $ pg_ctlcluster 12 main start
        $ psql

Creating a Database
~~~~~~~~~~~~~~~~~~~~~

After you've setup your PostgreSQL instance, you'll need to create a database and user with the correct permissions. You can do this with the SQL commands below, but be sure to change the password!

.. code-block:: postgresql 
    
    postgres=# CREATE DATABASE augur;
    postgres=# CREATE USER augur WITH ENCRYPTED PASSWORD 'password';
    postgres=# GRANT ALL PRIVILEGES ON DATABASE augur TO augur;

For example, if you were using ``psql`` to connect to an instance on your machine ``localhost`` under the default user ``postgres`` on the default PostgreSQL port ``5432``, you might run something like this to connect to the server:

.. code-block:: bash

    $ psql -h localhost -U augur -p 5432

Once you've got the database setup, Augur will take care of installing the schema for you. You're now ready to `install Augur <installation.html>`_!
