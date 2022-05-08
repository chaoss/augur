Installation
=============

This section of the documentation details how to install Augur's Python library from source. If you don't have a required dependency, please follow the provided links to install and configure it.

.. note::
  There are 3 main issues new developers encounter when first installing Augur: 

  1. The absence of a `GCC` or `Fortran` compiler, required by numpy and NLTK Python libraries. Look up how to install these compilers for your local operating system. Many times they simply need to be updated to a more current version.

  2. Conflicting versions of Python: The fix is platform specific. Some Python commands may be drawn from different commands because of how they are linked in `usr/local/bin`. A clean install of Python from the terminal should be able to fix any issues.

  3. Multiple, or conflicting versions of PostgreSQL, sometimes due to the absence of a functional `psql` function at the command line.


Dependencies
~~~~~~~~~~~~~

Backend
---------
Required:

-  `GitHub Access Token <https://github.com/settings/tokens>`__ (``repo`` and all ``read`` scopes except ``enterprise``)
-  `GitLab Access Token <https://gitlab.com/profile/personal_access_tokens>`__
-  `Python 3.6 - 3.10 <https://www.python.org/downloads/>`__
-  `Go 1.12 or later <https://golang.org/doc/install>`__

**Python 3.10 is the latest version supported. If your machine workers (which work with TensorFlow) do not work, then try downgrading your version of Python. [Older version of Augur support Python 3.8 at the latest.]**

Our REST API & data collection workers are written in Python 3.6. We query the GitHub & GitLab API to collect data about issues, pull requests, contributors, and other information about a repository, so GitLab and GitHub access tokens are **required** for data collection.

.. note::

   If you are simply trying Augur out, no GitLab token is necessary.

Installing Go
--------------
Go can be installed via the following command:

.. code-block:: bash

        sudo apt install golang-go

If this command fails, try installing Go through Snap. If Snap does not work for you, follow the instructions `here <https://www.digitalocean.com/community/tutorials/how-to-install-go-on-ubuntu-20-04>`__.

Optional: 

The ``value_worker`` uses a Go package called `scc <https://github.com/boyter/scc>`_ to run COCOMO calculations.
Once you've installed Go, follow the appropriate steps for your system to install the ``scc`` package.

-  Install gcc OpenMP Support: `sudo apt-get install libgomp1`

The ``message_insights_worker`` uses a system level package called OpenMP. You will need this installed at the system level for that worker to "work". 


Frontend
---------
If you're interested in using our visualizations, you can optionally install the frontend dependencies:

-  `Node <https://nodejs.org/en/>`__
-  `npm <https://www.npmjs.com/>`__
-  `Vue.js <https://vuejs.org/>`__  
-  `Vue-CLI <https://cli.vuejs.org/>`__

We use Vue.js as our frontend web framework, and ``npm`` as our package manager.

**At this point in time, we do not recommend installing Frontend dependencies.**

Visualization API calls
---------------------------

If you want to use the new Augur API Calls that generate downloadable graphics developed in the `https://github.com/chaoss/augur-community-reports` repository, you need to install the `firefox-geckodriver`. This dependency exists because the Bokeh libraries we use for these APIs require a web browser engine. 

.. code-block:: bash

    - which firefox-geckodriver
    - if nothing returned, then: 
    - sudo apt install firefox-geckodriver

.. note::
  If you have BOTH firefox-geckodriver AND chromedriver installed the visualization API will not work. 

Installing Augur
~~~~~~~~~~~~~~~~~

Now you're ready to build! The steps below outline how to create a virtual environment (**required**) and start the installation process,
after which you'll move on to the next section to configure the workers.

.. warning::
  Do **NOT** install or run Augur using ``sudo``. It is not required, and using it will inevitably cause some permissions trouble. Don't say we didn't warn you!

1. Clone the repository and change to the newly created directory.

.. code-block:: bash

   $ git clone 'https://github.com/chaoss/augur.git'
   $ cd augur/

2. Create a virtual environment in a directory of your choosing. Be sure to use the correct ``python`` command for
your installation of Python 3: on most systems, this is ``python3``, but yours may differ (you can use ``python -V`` or ``python3 -V`` to check).

.. code-block:: bash

    # to create the environment
    $ python3 -m venv $HOME/.virtualenvs/augur_env

    # to activate the environment
    $ source $HOME/.virtualenvs/augur_env/bin/activate

3. Run the install script. This script will:

- Install Augur’s Python library and application server
- Install Augur's data collection workers
- Prompt you for configuration settings, including your database credentials
- Generate a configuration file using your provided settings
- Install Augur's schema in the configured database
- Optionally, install Augur’s frontend and its dependencies
- Generate and output an Augur API key

.. note::

    At the very end, the install script will also generate an Augur API key for your database. This key will be automatically inserted into your database and then printed to your terminal. It's required to use the repo & repo group creation endpoints, so **make sure you save it off somewhere!** There is only one key per database.

.. code-block:: bash

   # run the install script
   $ make install

.. code-block:: bash

   # If you want to develop with Augur, use this command instead
   $ make install-dev

If you think something went wrong, check the log files in ``logs/``. If you want to try again, you can use ``make clean`` to delete any build files before running ``make install`` again.

If you want to test new code you have written, you can rebuild Augur using: 

.. code-block:: bash

   $ make rebuild-dev

.. note::

  If you chose to install Augur's frontend dependencies, you might see a bunch of ``canvas@1.6.x`` and ``canvas-prebuilt@1.6.x`` errors in the installation logs. These are harmless and are caused by a few of our dependencies having *optional* requirements for old versions of these libraries. If they seem to be causing you trouble, feel free to open an `issue <https://github.com/chaoss/augur/issues>`_.

To enable log parsing for errors, you need to install `Elasticsearch <https://www.elastic.co/downloads/elasticsearch>`_ and `Logstash <https://www.elastic.co/downloads/past-releases/logstash-6-8-10>`_ .

.. warning::
   Please note, that Logstash v7.0 and above has unresolved issues that affect this functionality.
   In order to use it in the near future, please download v6.8.
   If you use a package manager, it defaults to v7+, so we recommend downloading `binary <https://www.elastic.co/downloads/past-releases/logstash-6-8-10>`_ .
   This change is tested with Elasticsearch v7.8.0_2 and Logstash v6.8.10.

Once everything is installed, you're ready to `configure your data collection workers <../collecting-data.html>`_!
