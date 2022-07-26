====================
Logging Commands
====================

``augur logging``
==================

The collection of the ``augur logging`` commands is for interacting with logs.

``directory``
--------------
Prints the location of the directory to which Augur is configured to write its logs.

Example usage::

  # to print path to logs directory
  $ augur logging directory

  # successful output looks like:
  > /Users/carter/projects/work/augur/logs/


``tail``
---------
Prints the last ``n`` lines of each ``.log`` and ``.err`` file in the logs directory. ``n`` defaults to 20.

Example usage::

  # to print last ``n`` lines of ``.log`` and ``.err``
  $ augur logging tail

  # successful output looks like:
  > ********** Logfile: augur.log
    <contents of augur.log>

  > ********** Logfile: augur.err
    <contents of augur.err>


