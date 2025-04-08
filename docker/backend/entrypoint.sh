#!/bin/bash
#SPDX-License-Identifier: MIT
set -e

# Activate virtual environment
source /opt/venv/bin/activate

# Ensure log directory exists and has correct permissions
mkdir -p /augur/logs
chmod 755 /augur/logs

# Handle database connection
if [[ "$AUGUR_DB" == *"localhost"* ]]; then
    echo "localhost db connection"
    export AUGUR_DB="${AUGUR_DB/localhost/host.docker.internal}"
elif [[ "$AUGUR_DB" == *"127.0.0.1"* ]]; then
    echo "localhost db connection"
    export AUGUR_DB="${AUGUR_DB/127.0.0.1/host.docker.internal}"
fi

# Set environment variables
export AUGUR_FACADE_REPO_DIRECTORY=/augur/facade/
export AUGUR_DOCKER_DEPLOY="1"
export AUGUR_HOME="/home/augur"
export AUGUR_LOGS_DIR="${AUGUR_HOME}/.augur/logs"

# Create user's home directory structure
mkdir -p "${AUGUR_HOME}/.augur/logs"
chmod 755 "${AUGUR_HOME}/.augur"
chmod 755 "${AUGUR_HOME}/.augur/logs"

# Handle Redis connection
if [[ "$REDIS_CONN_STRING" == *"localhost"* ]] || [[ "$REDIS_CONN_STRING" == *"127.0.0.1"* ]]; then
    echo "localhost redis connection"
    export redis_conn_string="redis://host.docker.internal:6379"
else
    export redis_conn_string=$REDIS_CONN_STRING
fi

# Execute command
exec $*
