#!/bin/bash
#SPDX-License-Identifier: MIT
set -e

# Create necessary directories with proper permissions
mkdir -p /augur/logs /augur/facade
chmod 755 /augur/logs /augur/facade

# Initialize database schema if needed
if [[ "$AUGUR_DB_SCHEMA_BUILD" == "1" ]]; then
    augur db create-schema
fi

# Load configuration if not disabled
if [ ! -v AUGUR_NO_CONFIG ]; then
	./scripts/install/config.sh docker
fi

# Import repo groups if provided
if [[ -f /repo_groups.csv ]]; then
    augur db add-repo-groups /repo_groups.csv
fi

# Import repos if provided
if [[ -f /repos.csv ]]; then
   augur db add-repos /repos.csv
fi

# Ensure log directory exists and is writable
if [[ -d /augur/logs ]]; then
    touch /augur/logs/log.holder
    chmod 644 /augur/logs/log.holder
fi

# Create user's home directory structure if it doesn't exist
mkdir -p "${AUGUR_HOME}/.augur/logs"
chmod 755 "${AUGUR_HOME}/.augur"
chmod 755 "${AUGUR_HOME}/.augur/logs"

echo $PATH

# Start the backend
exec augur backend start
