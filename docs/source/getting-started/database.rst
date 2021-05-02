Database setup
===============
Abstract
--------
One of the reasons that Augur is so powerful is because of its `unified data model <../schema/data-model.html>`_.
In order to ensure this data model remains performant with large amounts of data, we use PostgreSQL as our database engine. 
We'll need to set up a PostgreSQL instance and create a database, after which Augur can take care of the rest.
Make sure to save off the credentials you use when you create the database, you'll need them again to configure Augur.


PostgreSQL Installation
=======================

Before you can install our schema, you will need to make sure you have write access to a PostgreSQL 10 or later database.

To download and install Postgres, follow the `instructions here. <https://www.postgresql.org/download/>`_

Using Docker 
------------

If you're looking for the fastest possible way to get Augur started, we recommend use our `database container <../docker/docker.html>`_. If you're looking to collect data long term, we recommend following the rest of this tutorial and setting up a persistent PostgreSQL installation.

.. warning::

    If you want to collect data over the long term, we strongly advise against `using a Docker container for your database <https://vsupalov.com/database-in-docker/>`_.


For Windows Users
-----------------

For windows specific instructions, `go here <https://www.postgresql.org/download/linux/>`_
You can also use WSL with a Ubuntu Distribution. `go there <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_
And then follow the linux instructions

For Linux Users 
---------------
For linux specific instructions, `go here <https://www.postgresql.org/download/linux/>`_

On Linux/Unix `pgAdmin <https://www.pgadmin.org/>`_ is a great open source alternative (dashboard).

For Mac Users
-------------
We recommend using `Postgres.app <https://postgresapp.com/>`_ if you're on macOS

Installation instructions can also be `found here <https://www.postgresql.org/download/macosx/>`_.

Creating a Database
===================
Running the Postgres Server 
---------------------------
Creating the Augur Table & Database User 
----------------------------------------
Using the Postgres Skeleton generator (tentative)
-------------------------------------------------

Connecting to the database during "make install"
================================================

