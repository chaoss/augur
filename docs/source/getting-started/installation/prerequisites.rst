Installation Guide: Prerequisites 
=================================
This section shows how to install Augur's Python library from the source. If you don't have a required dependency, please follow the provided links to install and configure it.

Operating System Level Services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**A GCC and Fortran Compiler: required by NumPy and NLTK Python libraries. Look up how to install these compilers for your local operating system. Many times they need to be updated to a more current version.**

Caution - Conflicting versions of Python:** The fix is platform-specific. On Mac OS X, multiple versions of Pythons often have been installed by the OS, brew, Anaconda, or both. The result is some python commands draw from different paths because of how they link in `/usr/local/bin`. Anaconda versions of Python3 are not recommended.

Caution - Multiple, or conflicting versions of PostgreSQL, sometimes lead to the absence of a functional `psql` function at the command line.  

**Redis-server and rabbitmq are required.** Instructions are next. 

Caching System (Redis) - Augur uses ``redis-server`` for task and session persistence. 
----------------
* `Linux Installation <https://redis.io/docs/getting-started/installation/install-redis-on-linux/>`__
* `Mac Installation <https://redis.io/docs/getting-started/installation/install-redis-on-mac-os/>`__
* `Windows Installation <https://redis.io/docs/getting-started/installation/install-redis-on-windows/>`__

Message Broker (RabbitMQ) - Augur uses `rabbitMQ` to stage all of the jobs generated during data collection. It communicates with `celery` to manage and monitor data collection status.
----------------
Follow the instructions are for your operating system. 

* `Linux Installation <https://www.rabbitmq.com/download.html>`__
* `Mac Installation <https://www.rabbitmq.com/install-homebrew.html>`__
* `Windows Installation <https://www.rabbitmq.com/install-windows.html>`__

These general steps provide an overview that is operating system independent, which may help when you are navigating the more detailed operating system specific instructions.

To set up rabbitmq for augur you must install it with the relevant package manager
for your distro (see above). You can find more info on how to install rabbitmq here https://www.rabbitmq.com/download.html.

**During installation you will be prompted for this broker url.** 

After installation, you must also set up your rabbitmq instance by running the below commands:

- `sudo rabbitmqctl add_user augur password123`
- `sudo rabbitmqctl add_vhost augur_vhost` 

.. warning::
The `augur_vhost` value for `add_vhost` needs to be unique for every Augur instance running on a server. 

- `sudo rabbitmqctl set_user_tags augur augurTag`
- `sudo rabbitmqctl set_permissions -p augur_vhost augur ".*" ".*" ".*"``

.. warning::
Be sure to set `augur_vhost` value to whatever you set it to in the previous step. If you have only one instance of augur running, simply use augur_vhost to keep it simple. 

**NOTE: it is important to have a static hostname when using rabbitmq as it uses hostname
to communicate with nodes.**

**Starting RabbitMQ 

- Then, start rabbitmq server with `sudo systemctl start rabbitmq.service`
- If your setup of rabbitmq is successful your broker url should look like this: ``broker_url = 'amqp://augur:password123@localhost:5672/augur_vhost'``

Tokens and Python Versions Supported
---------
Required:

-  `GitHub Access Token <https://github.com/settings/tokens>`__ (``repo`` and all ``read`` scopes except ``enterprise``). Be sure to set this token to "never expire", unless you desire Augur to stop working at some point in the future.
-  `GitLab Access Token <https://gitlab.com/profile/personal_access_tokens>`__
-  `Python 3.7 - 3.9 <https://www.python.org/downloads/>`__



**Python 3.10 is not yet supported because TensorFlow, which we use in our machine learning workers, does not yet support Python 3.10.**

Our REST API & data collection workers write in Python 3.8. We query the GitHub & GitLab API to collect data about issues, pull requests, contributors, and other information about a repository, so GitLab and GitHub access tokens are **required** for data collection.

Optional:

-  `Go 1.19 or later <https://golang.org/doc/install>`__

The ``value_worker`` uses a Go package called `scc <https://github.com/boyter/scc>`_ to run COCOMO calculations.
Once you've installed Go, follow the appropriate steps for your system to install the ``scc`` package.

-  Install gcc OpenMP Support: ``sudo apt-get install libgomp1`` -- Ubuntu 

The ``message_insights_worker`` uses a system-level package called OpenMP. You will need this installed at the system level for that worker to work.