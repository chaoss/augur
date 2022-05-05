Quickstart
==========

Get going fast! Intended for folks familiar with setting up DevOps environments. These instructions were tested using Ubuntu 20.04 and Ubuntu 18.04. 

PostgreSQL Installation
~~~~~~~~~~~~~~~~~~~~~~~~
- Gain access to an Ubuntu 18.04 or later environment and install PostgreSQL. Ubuntu 20.04 is recommended because its long-term support (LTS) window is longer. 

.. code-block:: bash 

	sudo apt update
	sudo apt upgrade
	sudo apt install software-properties-common
	sudo apt install python3-dev
	sudo apt install postgresql postgresql-contrib postgresql-client
	sudo apt install build-essential


- Create a PostgreSQL database for Augur to use

.. code-block:: bash

    $ sudo su - 
    $ su - postgres
    $ psql 

Then, once you've connected to your PostgreSQL instance\:

.. code-block:: postgresql

    postgres=# CREATE DATABASE augur;
    postgres=# CREATE USER augur WITH ENCRYPTED PASSWORD 'password';
    postgres=# GRANT ALL PRIVILEGES ON DATABASE augur TO augur;

Git Configuration
~~~~~~~~~~~~~~~~~~~~~~~~
- Configure Git: These instructions assume the potential of large repositories that occasionally perform significant refactoring within a small number of commits. Our experience is that nearly all organizations have at least one project that meets these criteria. 

.. code-block:: bash

	git config --global diff.renames true
	git config --global diff.renameLimit 200000
	git config --global credential.helper cache
	git config --global credential.helper 'cache --timeout=9999999999999'

- For each platform, perform a command line login in order to cache Git credentials for the LINUX user who operates Augur. This step is required in order to prevent the Facade Commit Counting Diesel from stalling on a command line prompt when repositories move or disappear. 

Install Go
~~~~~~~~~~~~~~~~~~~~~~~~
Two of Augur's workers use the Go programming language, which needs to be installed on your computer. Snap is the easiest way to install Go. If Snap does not work for you, see instructions here: https://www.digitalocean.com/community/tutorials/how-to-install-go-on-ubuntu-20-04

.. code-block:: bash

	sudo apt update
	sudo apt install snapd
	sudo snap install go --classic

Python Virtual Environment Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Set up a Python virtual environment (Python 3.8 and above are now required. Python 3.9 and python 3.10 work as well, though we have tested Python 3.9 on more platforms.) 
- Clone and install Augur as a regular user. 

.. code-block:: bash

	# make sure you are logged in as your own user (i.e. "sean")
	git clone https://github.com/chaoss/augur.git
	cd augur/
	sudo apt install make
	sudo apt-get install python3-venv 
	python3 -m venv $HOME/.virtualenvs/augur_env
	source $HOME/.virtualenvs/augur_env/bin/activate
	sudo apt install python-pip-whl
	sudo apt install python3-pip
	sudo apt install pythonpy
	python -m pip install --upgrade pip
	make install-dev {Follow prompts. You will need database credentials, a file location for cloned repositories, a GitHub Token, and a GitLab token.}

The following Note outlines the recommended choices for the questions that will come up during the 'make install-dev' run.

.. Note::
	- Would you like to...
		1) initialize a new database AND install the schema?
		2) connect to an existing empty database and ONLY install the schema?
		3) connect to a database with the schema already installed?
		
		- Since we have already created a database and user with postgres, you will want to choose option 2 when you reach the database credentials question
	- Please enter the credentials for the database.
		- If you have followed the steps outlined above for the database creation, the Database you will want to type is 'augur', the user is 'augur', and the password is 'password'. For the host and port, please put 'localhost' for the host and '5432' for the port, as this corresponds with postgres.
	- Please provide a valid GitHub API key.
		- When asked to create and enter a Github API Key, please use this link if you do not understand how to do so: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
	- The Facade data collection worker will clone repositories to this machine to run its analysis.Would you like to clone to an existing directory, or create a new one?
		1) Use an existing directory
		2) Create a new directory

		- When asked where to store, hit 2 to create a new direictory and give the full path

- Seven sample repositories will load by default. You can delete them if you want to use your own repositories by deleting records from the `repo` table first, then deleting the records from the `repo_groups` table. 

.. code-block:: bash

	augur --help
	augur db --help
	augur backend --help

Loading Repositories
~~~~~~~~~~~~~~~~~~~~~~~~
The commands for loading repos are: 

.. code-block:: bash

	augur db add-github-org
	augur db add-repo-groups
	augur db add-repos

We recommend that you test your instance using 50 or fewer repositories before undertaking a more substantial data collection. When you do take on more collection, you can "collect data faster" by adding additional tokens to the `worker_oauth` table in the `augur_operations` schema and increasing the number of workers for the pull request and GitHub worker blocks in the `augur.config.json` file that generates at install.
