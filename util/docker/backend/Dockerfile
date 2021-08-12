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

RUN mkdir /virtualenv
RUN python -m venv /virtualenv/augur_env
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

RUN /bin/bash -c "source /virtualenv/augur_env/bin/activate"
RUN set -x \
    && pip install .


USER root
RUN ./scripts/docker/install-go.sh
RUN ./scripts/install/workers.sh

USER augur
RUN /bin/bash -c "source /virtualenv/augur_env/bin/activate"
RUN augur config init --rc-config-file /augur/backend.docker.config.json \
    && mkdir -p repos/ logs/

COPY ./util/docker/backend/entrypoint.sh /
USER ROOT
RUN chmod +x /entrypoint.sh

USER augur
RUN /bin/bash -c "source /virtualenv/augur_env/bin/activate"
ENTRYPOINT /entrypoint.sh
