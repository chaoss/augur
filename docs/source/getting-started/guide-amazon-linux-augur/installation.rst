Installation
=============

This section of the documentation details how to install Augur's Python library from source. If you don't have a required dependency, please follow the provided links to install and configure it.

.. note::
  There are 3 main issues new developers encounter when first installing Augur: 

  1. The absence of a `gcc` or `fortran` compiler, required by numpy and nltk Python libraries. Look up how to install these compilers for your local operating system. Many times they simply need to be updated to a more current version.

  2. Conflicting versions of Python: The fix is platform specific. Some Python commands may be drawn from different paths because of how they are linked in `/usr/local/bin`. A clean install of Python from the terminal should be able to fix any issues.

  3. Multiple, or conflicting versions of postgresql, sometimes due to the absence of a functional `psql` function at the command line.


Prior to Installing
~~~~~~~~~~~~~~~~~~~


Installing GO
-------------

Augur requires a language called GO to fully install. This `simple method of installing`_ (shown directly below) works best, but a workaround is also listed in the event that it does not.

.. code-block:: bash
  
	$ sudo yum install golang -y

.. _simple method of installing: https://medium.com/cloud-security/go-get-go-download-install-8b48a0425717

The Workaround
---------------

There's a guide here_ for CentOS that can be adapted for the current version of GO and Amazon Linux without much difficulty. We recommend getting the latest version of GO from their website_ and following steps 2 and 3 from the guide (also listed below).

.. _here: https://www.digitalocean.com/community/tutorials/how-to-install-go-1-7-on-centos-7
.. _website: https://go.dev/dl/

.. code-block:: bash

	$ sudo tar -C /usr/local -xvzf [the GO file you just downloaded]
	$ mkdir -p ~/projects/{bin, pkg, src}

Then set up your PATH so those folders are included. Append onto */etc/profile.d/path.sh* this:

.. code-block:: 
	
	export PATH=$PATH:/usr/local/go/bin

Set up environmental variables so GO can be used - onto your *~/.bash_profile* , append these:

.. code-block::
	
	export GOBIN="$HOME/projects/bin"
	export GOPATH="$HOME/projects/src"
	
Don't forget to reload the profiles so the session updates!

.. code-block:: bash
	
	$ source /etc/profile && source ~/.bash_profile


Dependencies
~~~~~~~~~~~~~

Backend
---------
Required:

-  `GitHub Access Token <https://github.com/settings/tokens>`__ (``repo`` and all ``read`` scopes except ``enterprise``)
-  `GitLab Access Token <https://gitlab.com/profile/personal_access_tokens>`__
-  `Python 3.6 - 3.10 <https://www.python.org/downloads/>`__

**Python 3.10 is the latest version supported. If your machine workers (which work with TensorFlow) do not work, then try downgrading your version of Python. [Older versions of Augur support Python 3.6]**

Our REST API & data collection workers are written in Python 3.6. We query the GitHub & GitLab API to collect data about issues, pull requests, contributors, and other information about a repository, so GitLab and GitHub access tokens are **required** for data collection.

.. note::
  If you are simply trying Augur out, no GitLab token is necessary.

Optional:

-  `Go 1.12 or later <https://golang.org/doc/install>`__

The ``value_worker`` uses a Go package called `scc <https://github.com/boyter/scc>`_ to run COCOMO calculations.
Once you've installed Go, follow the appropriate steps for your system to install the ``scc`` package.

-  Install gcc OpenMP Support: `sudo apt-get install libgomp1` -- Ubuntu 

The ``message_insights_worker`` uses a system level package called OpenMP. You will need this installed at the system level for that worker to "work". 


Frontend
---------
If you're interested in using our visualizations, you can optionally install the frontend dependencies:

-  `node <https://nodejs.org/en/>`__
-  `npm <https://www.npmjs.com/>`__
-  `Vue.js <https://vuejs.org/>`__  
-  `vue-cli <https://cli.vuejs.org/>`__

We use Vue.js as our frontend web framework, and ``npm`` as our package manager.

**At this point in time, we do not recommend installing Frontend dependencies.**

Visualization API calls
---------------------------

On Amazon Linux flavors: if you want to use the new Augur API Calls that generate downloadable graphics developed in the `https://github.com/chaoss/augur-community-reports` repository, you need to install the `chromedriver`.

.. code-block:: bash

    $ sudo amazon-linux-extras install epel -y
    $ sudo yum install chromium
  
.. note::
  A possibly better solution is instead installing `firefox-geckodriver`; however, this does not appear to be built-in and requires far more configuration. We have hence chosen not to include it.
  
.. note::
  If you have BOTH firefox-geckodriver AND chromedriver installed the visualization API will not work. 


Installing Augur
~~~~~~~~~~~~~~~~

Now you're ready to build! The steps below outline how to create a virtual environment (**required**) and start the installation process,
after which you'll move on to the next section to configure the workers.

.. warning::
  Do **NOT** install or run Augur using ``sudo``. It is not required, and using it will inevitably cause some permissions trouble. Don't say we didn't warn you!

0. Clone the repository and change to the newly created directory.

.. code-block:: bash

   $ git clone 'https://github.com/chaoss/augur.git'
   $ cd augur/

1. Create a virtual environment in a directory of your choosing. Be sure to use the correct ``python`` command for
your installation of Python 3: on most systems, this is ``python3``, but yours may differ (you can use ``python -V`` or ``python3 -V`` to check).

.. code-block:: bash

    # to create the environment
    $ python3 -m venv $HOME/.virtualenvs/augur_env

    # to activate the environment
    $ source $HOME/.virtualenvs/augur_env/bin/activate

2. Run the install script. This script will:

- install Augur’s Python library and application server
- install Augur's data collection workers
- prompt you for configuration settings, including your database credentials
- generate a configuration file using your provided settings
- install Augur's schema in the configured database
- optionally, install Augur’s frontend and its dependencies
- generate and output an Augur API key

.. note::

    At the very end, the install script will also generate an Augur API key for your database. This key will be automatically inserted into your database and then printed to your terminal. It's required to use the repo & repo group creation endpoints, so **make sure you save it off somehwere!** There is only one key per database.

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
   This change is tested with Elasticserach v7.8.0_2 and Logstash v6.8.10.

Once everything is installed, you're ready to `configure your data collection workers <collecting-data.html>`_!
