macOS Errata
~~~~~~~~~~~~~
If you’re running Augur on macOS, we strongly suggest updating your shell’s initialization script in the following.

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

Please follow this link back to the Detailed Installation guide to continue installation once you have completed this step:

- :ref: 'detailed-installation'
