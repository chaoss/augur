Other Env: Set up Augur
=======================

In this page we shall look at setting up Augur in any Unix-like system. There are 3 main steps in setting up Augur:

1. Setting PostgreSQL database
2. Setting prerequisites (Git, python, python virtual environment, etc)
3. Installing Augur

Let us look at these steps in detail.

1. Setting PostgreSQL database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the reasons that Augur is so powerful is because of its `unified data model <../schema/data-model.html>`_.
To ensure this data model remains performant with large amounts of data, we use PostgreSQL as our database engine.
You will need to have **write access** to a PostgreSQL 10 or later database.
We'll need to set up a PostgreSQL instance and create a database, after which Augur can take care of the rest.

If you're looking for the fastest possible way to get Augur started, we recommend use our `database container <../docker/docker.html>`_. If you're looking to collect data long-term, we recommend following the rest of this tutorial and setting up a persistent PostgreSQL installation.

.. warning::

    If you want to collect data over the long term, we strongly advise against `using a Docker container for your database <https://vsupalov.com/database-in-docker/>`_.

PostgreSQL Installation
------------------------
You can follow any of various instructions to install PostgreSQL available on internet depending on your operating system.
If you're a newcomer to PostgreSQL, you can follow their excellent instructions `here <https://www.postgresql.org/docs/12/tutorial-install.html>`_ to set it up for your machine of choice. We recommend using ``Postgres.app`` if you're on macOS, but if you're running UNIX or are looking for an alternative to ``Postgres.app`` then pgAdmin is a great open-source alternative.

Creating database
------------------
After you set up your PostgreSQL instance, you'll need to create a database and user with the correct permissions. You can do this with the SQL commands below, but be sure to change the password!

.. code-block:: postgresql 
    
    CREATE DATABASE augur;
    CREATE USER augur WITH ENCRYPTED PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE augur TO augur;

Make sure to save the database name, user name and password. They will be required while building augur.

2. Setting prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~

Git configuration
------------------
Install git in your system if it is not already installed.

- Configure Git: These instructions assume the potential of large repositories that occasionally perform significant refactoring within a small number of commits. Our experience is that nearly all organizations have at least one project that meets these criteria.

.. code-block:: bash

	git config --global diff.renames true
	git config --global diff.renameLimit 200000
	git config --global credential.helper cache
	git config --global credential.helper 'cache --timeout=9999999999999'

- For each platform, perform a command-line login  to cache Git credentials for the LINUX user who operates Augur. This step is required in order to prevent the Facade Commit Counting Diesel from stalling on a command-line prompt when repositories move or disappear.

Install Go
------------
The ``value_worker`` uses a Go package called `scc <https://github.com/boyter/scc>`_ to run COCOMO calculations, therefore ``Go`` needs to be installed on your computer. Follow the instructions present here: https://go.dev/doc/install

The ``message_insights_worker`` uses a system-level package called OpenMP. You will need this installed at the system level for that worker to work. 

Python Virtual Environment Configuration
-------------------------------------------
- Set up a Python virtual environment (Python 3.8 and above are now required. Python 3.9 and python 3.10 work as well, though we have tested Python 3.9 on more platforms.)

Follow various instructions present on internet to install ``python 3.8`` , ``pip3``, ``python virtual environment``.

Run the following commands to create new virtual environment:

.. code-block:: bash

	python3 -m venv $HOME/.virtualenvs/augur_env
	source $HOME/.virtualenvs/augur_env/bin/activate
	python -m pip install --upgrade pip

Token requirements
---------------------
You will be asked to enter GitHub token as well as GitLab token while building Augur. Make sure you have them ready:

-  `GitHub Access Token <https://github.com/settings/tokens>`__ (``repo`` and all ``read`` scopes except ``enterprise``)
-  `GitLab Access Token <https://gitlab.com/profile/personal_access_tokens>`__


Frontend (Optional)
---------------------
If you're interested in using our visualizations, you can optionally install the frontend dependencies:

-  `Node <https://nodejs.org/en/>`__
-  `npm <https://www.npmjs.com/>`__
-  `Vue.js <https://vuejs.org/>`__  
-  `Vue-CLI <https://cli.vuejs.org/>`__

We use Vue.js as our frontend web framework and ``npm`` as our package manager.

Visualization API calls (Optional)
------------------------------------
On Ubuntu and other Linux flavors: if you want to use the new Augur API Calls that generate downloadable graphics developed in the `https://github.com/chaoss/augur-community-reports` repository, you need to install the `firefox-geckodriver` (on Ubuntu or Red Hat Fedora) or `geckodriver` on Mac OSX, at the system level. This dependency exists because the Bokeh libraries we use for these APIs require a web browser engine.

For Fedora you can use

.. code-block:: bash

    - which firefox-geckodriver
    - if nothing returned, then: 
    - sudo dnf install firefox-geckodriver

For Mac OSX you can use: 

.. code-block:: bash

    -  which geckodriver
    -  if nothing returned, then:
    -  brew install geckodriver

.. note::
  If you have BOTH Firefox-geckodriver AND ChromeDriver installed the visualization API will not work. 
  
  We have fully tested with Firefox-gecko driver on Linux platforms, and geckodriver on OSX. If you have ONLY ChromeDriver installed, it will probably work. Open an issue if you have a functioning ChromeDriver implementation.  

4. Installing Augur
~~~~~~~~~~~~~~~~~~~~~

Setting up Augur
-----------------
- Clone and install Augur as a regular user. Run the following commands.
- Keep the database name, user name and password from PostgreSQL Installation section ready.

.. code-block:: bash

	# Ensure you are logged in as your user on Github and change the "<YOUR_GITHUB_USERNAME>" to your Github username (e.g. "sean")
	git clone https://github.com/<YOUR_GITHUB_USERNAME>/augur.git
	cd augur/
	source $HOME/.virtualenvs/augur_env/bin/activate
	make install
  # If you want to develop with Augur, use this command instead
  make install-dev

- Follow prompts. You will need database credentials, a file location for cloned repositories, a GitHub Token, and a GitLab token.

If you think something went wrong, check the log files in ``logs/``. If you want to try again, you can use ``make clean`` to delete any build files before running ``make install`` again.

The above script performs following actions

- Install Augur’s Python library and application server
- Install Augur's data collection workers
- Prompt you for configuration settings, including your database credentials
- Generate a configuration file using your provided settings
- Install Augur's schema in the configured database
- Optionally, install Augur’s frontend and its dependencies
- Generate and output an Augur API key

.. note::

  The install script will also generate an Augur API key for your database at the very end. This key will be automatically inserted into your database and printed to your terminal. It requires to use the repo & repo group creation endpoints, so **make sure you save it off somewhere!** There is only one key per database.

- Seven sample repositories will load by default. You can delete them if you want to use your repositories by deleting records from the `repo` table first, then deleting the records from the `repo_groups` table.

We have successfully set up augur on our system and we can move to the section dedicated to how to use it.

Miscellaneous
~~~~~~~~~~~~~~

For macOS Errata
-----------------
If you’re running Augur on macOS, we strongly suggest updating your shell’s initialization script in the following:

In a terminal, open the script:

  nano .bash_profile
 
Add the following line to the end of the file:

  export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

Save the file and exit.
Run this command to reload bash_profile:

  source .bash_profile

Check if it is updated:

  env

``env`` should contain ``OBJC_DISABLE_INITIALIZE_FORK_SAFETY``.

macOS takes "helpful" measures to prevent Python subprocesses (which Augur uses) from forking cleanly, and setting this environment variable disables these safety measures to restore regular Python functionality.

.. warning::
  If you skip this step, you'll likely see all housekeeper jobs randomly exiting for no reason, and the Gunicorn server will not behave nicely either. Skip this step at your own risk!

MacOS users: 
------------
If your build fails and in gunicorn.log you see this error: ``Connection in use: ('0.0.0.0', 5000)``, that means port 5000 is being used by another process. To solve this issue, go to System Preferences -> Sharing -> Disable Airplay Receiver.

If you want to test new code you have written, you can rebuild Augur using: 

.. code-block:: bash

   $ make rebuild-dev

.. note::

  If you chose to install Augur's frontend dependencies, you might see a bunch of ``canvas@1.6.x`` and ``canvas-prebuilt@1.6.x`` errors in the installation logs. These are harmless and caused by a few of our dependencies having *optional* requirements for old versions of these libraries. If they seem to be causing you trouble, feel free to open an `issue <https://github.com/chaoss/augur/issues>`_.

To enable log parsing for errors, you need to install `Elasticsearch <https://www.elastic.co/downloads/elasticsearch>`_ and `Logstash <https://www.elastic.co/downloads/past-releases/logstash-6-8-10>`_.

.. warning::

   Please note, that Logstash v7.0 and above have unresolved issues that affect this functionality.
   
   In order to use it in the near future, please download v6.8.

   If you use a package manager, it defaults to v7+, so we recommend downloading `binary <https://www.elastic.co/downloads/past-releases/logstash-6-8-10>`_ .

   This change is tested with Elasticsearch v7.8.0_2 and Logstash v6.8.10.

