#SPDX-License-Identifier: MIT
FROM postgres:16

LABEL maintainer="outdoors@acm.org"
LABEL version="0.90.0"

ENV POSTGRES_DB="test"
ENV POSTGRES_USER="augur"
ENV POSTGRES_PASSWORD="augur"

EXPOSE 5432

COPY ./docker/database/augur-new-schema.sql /docker-entrypoint-initdb.d/
