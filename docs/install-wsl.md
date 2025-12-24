# Installing Augur on Windows using WSL2 (Docker-based)

## Overview
This guide explains how to run Augur on Windows using WSL2 with Docker.
Manual (non-Docker) installation inside WSL is not recommended.

## Prerequisites
- Windows 10/11
- WSL2 enabled
- Ubuntu 22.04
- Docker Desktop with WSL integration enabled

## Recommended Setup (Docker)

1. Install Docker Desktop on Windows  
   https://docs.docker.com/desktop/install/windows-install/

2. Enable WSL integration for Ubuntu  
   Docker Desktop → Settings → Resources → WSL Integration

3. Clone Augur inside WSL (not Windows filesystem):
   ```bash
   git clone https://github.com/chaoss/augur.git
   cd augur


## Common Issues & Solutions
### PostgreSQL port conflicts
- Stop PostgreSQL running on Windows host
- Ensure only Docker container uses port 5432

### File permission issues
- Clone repo inside WSL home directory
- Avoid `/mnt/c` paths

### Docker resource limits
- Increase memory to at least 8GB in Docker Desktop

## What Not To Do
- Do not run manual backend installs inside WSL
- Do not run PostgreSQL separately outside Docker
