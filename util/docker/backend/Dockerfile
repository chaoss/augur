#SPDX-License-Identifier: MIT
FROM python:3.8.11-slim-buster

LABEL maintainer="outdoors@acm.org"
LABEL version="0.17.0"

RUN addgroup --gid 1000 augur
RUN adduser --disabled-password --gecos '' --uid 1000 --gid 1000 augur

ENV DEBIAN_FRONTEND=noninteractive

RUN set -x \
    && apt-get update \
    && apt-get -y install --no-install-recommends \
        git \
        gcc \
        python3-pip \
        wget \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

USER augur
RUN mkdir /virtualenv
RUN python -m venv /virtualenv/augur_env
USER root
EXPOSE 5000

WORKDIR /augur
USER augur
COPY ./README.md .
COPY ./augur/ augur/
COPY ./metadata.py .
COPY ./setup.py .
COPY ./scripts/ scripts/
COPY ./workers/ workers/
COPY ./schema/ schema/

COPY ./util/docker/backend/backend.docker.config.json .

RUN ./scripts/docker/main-install.sh


USER root
RUN ./scripts/docker/install-go.sh
RUN ./scripts/install/workers.sh

USER augur
RUN ./scripts/docker/docker-config.sh

COPY ./util/docker/backend/entrypoint.sh /
USER ROOT
RUN chmod +x /entrypoint.sh

USER augur
ENTRYPOINT /entrypoint.sh
