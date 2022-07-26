Use Augur
============

After you have installed Augur on your system, you can start collecting data. To test everything works fine, you can run the given command. It will run Augur using the one repository in the default database, and default worker settings.

.. code-block:: bash

   # To Start Augur: 
   nohup augur backend start >logs/run.log 2>logs/run.err &

   # To Stop Augur: 
   augur backend stop
   augur backend kill

You can check the database that you provided during installation for all data. The above commands are explained in details in the `command-line-interface` section.

The following sections explain how you can configure Augur to suit your needs.

.. toctree::
   :maxdepth: 1

   collecting-data
   frontend
   command-line-interface/toc
