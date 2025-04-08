#!/bin/bash
set -e

# Function to check if PostgreSQL is ready
wait_for_postgres() {
    until pg_isready -U augur; do
        echo "Waiting for PostgreSQL to be ready..."
        sleep 2
    done
    echo "PostgreSQL is ready!"
}

# Create necessary directories if they don't exist
mkdir -p /home/augur/.augur/logs
chown -R augur:augur /home/augur/.augur

# Initialize database if needed
if [ ! -f "$PGDATA/PG_VERSION" ]; then
    echo "Initializing PostgreSQL database..."
    initdb -U augur
    
    # Modify postgresql.conf to allow connections
    echo "listen_addresses='*'" >> "$PGDATA/postgresql.conf"
    echo "host all all all md5" >> "$PGDATA/pg_hba.conf"
fi

# Start PostgreSQL
exec postgres 