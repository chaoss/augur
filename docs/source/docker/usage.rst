Interacting with the containers
================================

Once the containers are up and running, you have a few options for interacting with them. They will automatically collect data for your repositories - but how do you add repositories? We're glad you asked!

Using the repo loading UI
--------------------------

Augur offers a special graphical interface for loading repository groups when using the Docker containers. This component is called ``augurface``, and is available anytime you are using the ``backend`` and ``frontend`` services together.

To use it, first start the two services (we recommend using `Docker Compose <docker-compose.html>`_ for this):

.. code-block:: bash

    # this example uses the database image, but will work with an external one as well
    $ docker-compose -f docker-compose.yml -f database-compose.yml up

Then, navigate to ``http://localhost:8080/augurface/`` in your browser - **note the trailing slash!** Once you're on this page, you'll need to enter in your Augur API key in the box on the top right. On a default Docker installation, you can use ``docker_key``, but we recommend changing this as soon as possible if you are planning to use the instance long-term. Commands for working with the API keys can be found `here <../getting-started/command-line-interface/db.html>`_.

Once you've entered your API key, you will be able to use the UI to automatically import GitHub organizations as a repo group, or manually create and edit repo groups yourself. Deleting repos or repo groups is not currently supported, but would be a great contribution!

.. warning::

    Because the UI only requires an API key to edit the database, **we recommend that you do not publicly deploy any Docker instance outside your local network or intranet.** The Docker build is intended ONLY for short term data collection usage and local development. We understand if this inconvenciences you, but the functionality is very new to Augur and still needs time to be production ready. **You have been warned.**

If are not using the ``frontend`` service, you can use the `database CLI <../getting-started/command-line-interface/db.html>`_ from within the container to add repos. See below for how to start a shell within the container.


Accessing the containers
---------------------------

If you need to access a running container (perhaps to check the worker logs) or run a CLI command, you can use the following helpful command, replacing ``<service_name>`` with the appropriate value:

.. code-block:: bash

    $ docker exec -it <service_name> /bin/bash


Viewing container logs
-------------------------

By default, the only logs shown by the container are the logs of Augur's main data collection process. If you started your container(s) in the background, and want to view these logs again, run the following command in the root ``augur`` directory\:

.. code-block:: bash

    # to quickly view the most recent logs
    $ docker-compose logs

    # to watch the logs in real time (like tail -f)
    $ docker-compose logs -f

Conclusion
-----------

This wraps up the Docker section of the Augur documentation. We hope it was useful! Happy hacking!
