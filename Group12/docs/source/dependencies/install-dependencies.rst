Installing Augur's Dependencies
===============================
Once you have set up the Ubuntu Amazon EC2 instance, you will need to install all of Augur’s dependencies before proceeding on to Augur’s installation. To do this, you can run the script ``install_dependencies.sh`` to automatically install all of Augur’s dependencies for you.

.. code-block:: bash

    ./install_dependencies.sh

After the script has finished, you are now ready to install Augur starting from the installing Augur stub `here <https://oss-augur.readthedocs.io/en/main/getting-started/installation.html#installing-augur>`_ and running the commands ``make install-dev`` instead of ``make install``
