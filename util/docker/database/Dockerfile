#SPDX-License-Identifier: MIT
FROM postgres:12 as setup-stage

LABEL maintainer="outdoors@acm.org"
LABEL version="0.15.4"

ENV POSTGRES_PASSWORD "augur"
ENV POSTGRES_USER "augur"
ENV POSTGRES_DB "augur"

FROM setup-stage as generate-schema

COPY ./schema/generate/ /docker-entrypoint-initdb.d/

EXPOSE 5432
