Installing Augur on Windows Using WSL2 (Docker-Based)
====================================================

Overview
--------

This guide explains how to run Augur on Windows using WSL2 with Docker.
Manual (non-Docker) installation inside WSL is **not recommended**.

Prerequisites
-------------

- Windows 10 or Windows 11
- WSL2 enabled
- Ubuntu 22.04
- Docker Desktop with WSL integration enabled

Recommended Setup (Docker)
--------------------------

1. Install Docker Desktop on Windows:

   https://docs.docker.com/desktop/install/windows-install/

2. Enable WSL integration for Ubuntu:

   - Open Docker Desktop
   - Go to **Settings → Resources → WSL Integration**
   - Enable integration for Ubuntu

3. Clone Augur inside WSL (not in the Windows filesystem):

   ::

      git clone https://github.com/chaoss/augur.git
      cd augur

Common Issues and Solutions
--------------------------

PostgreSQL Port Conflicts
~~~~~~~~~~~~~~~~~~~~~~~~~

- Stop PostgreSQL running on the Windows host.
- Ensure only the Docker container uses port **5432**.

File Permission Issues
~~~~~~~~~~~~~~~~~~~~~

- Always clone the repository inside your WSL home directory.
- Avoid using paths under ``/mnt/c``.

Docker Resource Limits
~~~~~~~~~~~~~~~~~~~~~

- Increase Docker memory allocation to at least **8 GB** in Docker Desktop.

What Not To Do
--------------

- Do **not** run manual backend installations inside WSL.
- Do **not** run PostgreSQL separately outside Docker.
