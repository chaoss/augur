FROM postgres:16

# Create a non-root user and group
RUN groupadd -r augur && useradd -r -g augur augur

# Set up directories with correct permissions
RUN mkdir -p /var/lib/postgresql/data /var/log/postgresql /var/run/postgresql \
    && chown -R augur:augur /var/lib/postgresql /var/log/postgresql /var/run/postgresql \
    && chmod 700 /var/lib/postgresql/data

# Create log directory with correct permissions
RUN mkdir -p /home/augur/.augur/logs \
    && chown -R augur:augur /home/augur/.augur \
    && chmod 755 /home/augur/.augur \
    && chmod 755 /home/augur/.augur/logs

# Set environment variables
ENV POSTGRES_USER=augur
ENV POSTGRES_PASSWORD=augur
ENV POSTGRES_DB=augur
ENV PGDATA=/var/lib/postgresql/data

# Create initialization script
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
# Initialize database if needed\n\
if [ ! -f "$PGDATA/PG_VERSION" ]; then\n\
    echo "Initializing PostgreSQL database..."\n\
    initdb -U augur -D "$PGDATA" --auth=md5 --pwfile=<(echo "$POSTGRES_PASSWORD")\n\
    \n\
    # Modify postgresql.conf to allow connections\n\
    echo "listen_addresses = '\''*'\''" >> "$PGDATA/postgresql.conf"\n\
    echo "host all all all md5" >> "$PGDATA/pg_hba.conf"\n\
fi\n\
\n\
# Start PostgreSQL in the background\n\
postgres -D "$PGDATA" &\n\
\n\
# Wait for PostgreSQL to be ready\n\
until pg_isready -U augur; do\n\
    echo "Waiting for PostgreSQL to be ready..."\n\
    sleep 2\n\
done\n\
echo "PostgreSQL is ready!"\n\
\n\
# Create schema and tables\n\
PGPASSWORD=$POSTGRES_PASSWORD psql -U augur -d postgres -c "CREATE DATABASE augur;" || true\n\
\n\
PGPASSWORD=$POSTGRES_PASSWORD psql -U augur -d augur -c "CREATE SCHEMA IF NOT EXISTS augur_operations;"\n\
\n\
PGPASSWORD=$POSTGRES_PASSWORD psql -U augur -d augur -c "CREATE TABLE IF NOT EXISTS augur_operations.config (\n\
    section_name VARCHAR(50),\n\
    setting_name VARCHAR(50),\n\
    value TEXT,\n\
    type VARCHAR(20),\n\
    description TEXT,\n\
    PRIMARY KEY (section_name, setting_name)\n\
);"\n\
\n\
# Insert initial logging configuration\n\
PGPASSWORD=$POSTGRES_PASSWORD psql -U augur -d augur -c "INSERT INTO augur_operations.config (section_name, setting_name, value, type, description)\n\
VALUES \n\
    ('\''Logging'\'', '\''logs_directory'\'', '\''~/.augur/logs'\'', '\''str'\'', '\''Directory where log files will be stored'\''),\n\
    ('\''Logging'\'', '\''log_level'\'', '\''INFO'\'', '\''str'\'', '\''Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)'\''),\n\
    ('\''Logging'\'', '\''max_file_size_mb'\'', '\''10'\'', '\''int'\'', '\''Maximum size of each log file in megabytes'\''),\n\
    ('\''Logging'\'', '\''backup_count'\'', '\''5'\'', '\''int'\'', '\''Number of backup log files to keep'\''),\n\
    ('\''Logging'\'', '\''file_format'\'', '\''%(asctime)s [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)d] %(message)s'\'', '\''str'\'', '\''Format string for log file entries'\''),\n\
    ('\''Logging'\'', '\''console_format'\'', '\''%(asctime)s [%(levelname)s] %(message)s'\'', '\''str'\'', '\''Format string for console log entries'\''),\n\
    ('\''Logging'\'', '\''date_format'\'', '\''%Y-%m-%d %H:%M:%S'\'', '\''str'\'', '\''Format string for timestamps in log entries'\'')\n\
ON CONFLICT (section_name, setting_name) DO UPDATE SET \n\
    value = EXCLUDED.value,\n\
    type = EXCLUDED.type,\n\
    description = EXCLUDED.description;"\n\
\n\
# Keep PostgreSQL running in the foreground\n\
wait\n\
' > /usr/local/bin/docker-entrypoint.sh \
    && chmod +x /usr/local/bin/docker-entrypoint.sh

# Switch to non-root user
USER augur

# Expose the PostgreSQL port
EXPOSE 5432

# Set the entrypoint
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"] 