#!/bin/bash
set -e

# Ensure logs directory exists with correct permissions
mkdir -p /home/augur/.augur/logs
chown -R augur:augur /home/augur/.augur
chmod -R 755 /home/augur/.augur
chmod 755 /home/augur/.augur/logs

# Ensure application directory has correct permissions
chown -R ${AUGUR_USER}:${AUGUR_GROUP} /app
chmod -R 755 /app

# Execute the command passed to docker run
exec "$@" 