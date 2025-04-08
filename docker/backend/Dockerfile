# SPDX-License-Identifier: MIT


FROM golang:1.23 AS golang


# RUN ./scripts/docker/install-go.sh
ENV PATH="${PATH}:/usr/local/go/bin"
COPY ./scripts/ scripts/
RUN ./scripts/docker/install-golang-deps.sh


# FROM rust:1.78 as rust

# # Ensure Rust directories are writable
# RUN mkdir -p /root/.rustup/downloads /root/.cargo/registry && \
#     chmod -R 777 /root/.rustup /root/.cargo

# # Add rust and cargo to PATH
# # ENV PATH="/root/.cargo/bin:${PATH}"

# # Install the specific version of Rust
# # RUN set -x \
# #     && rustup install 1.78.0
# # RUN set -x \
# #     && rustup default 1.78.0


# # Add rust and cargo to PATH
# ENV PATH="/usr/bin/:/root/.cargo/bin:/usr/local/bin:${PATH}"

FROM python:3.11-slim-bullseye

LABEL maintainer="outdoors@acm.org"
LABEL version="0.85.3"

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/bin/:/usr/local/bin:/usr/lib:${PATH}"

# Create non-root user and group
RUN groupadd -r augur && useradd -r -g augur augur

RUN set -x \
    && apt-get update \
    && apt-get -y install \
        git \
        bash \
        curl \
        gcc \
        software-properties-common \
        postgresql-contrib \
        musl-dev \
        python3-dev \
        python3-distutils \
        python3-venv \
        wget \
        postgresql-client \
        libpq-dev \
        build-essential \
        chromium \
        tar \
        jq \
        chromium-driver \
        && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Firefox from Debian repositories for ARM64 architecture
RUN set -x \
    && apt-get update \
    && apt-get install -y firefox-esr

# Install Geckodriver
RUN GECKODRIVER_VERSION=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | jq -r '.tag_name' | sed 's/v//') \
    && ARCH=$(uname -m) \
    && if [ "$ARCH" = "aarch64" ]; then \
         GECKODRIVER_URL="https://github.com/mozilla/geckodriver/releases/download/v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux-aarch64.tar.gz"; \
         GECKODRIVER_FILE="geckodriver-v${GECKODRIVER_VERSION}-linux-aarch64.tar.gz"; \
       else \
         GECKODRIVER_URL="https://github.com/mozilla/geckodriver/releases/download/v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz"; \
         GECKODRIVER_FILE="geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz"; \
       fi \
    && wget $GECKODRIVER_URL \
    && tar -xzf $GECKODRIVER_FILE \
    && mv geckodriver /usr/local/bin/ \
    && rm $GECKODRIVER_FILE

# Verify installations
RUN firefox --version
RUN geckodriver --version

EXPOSE 5000

WORKDIR /augur

# Copy application files
COPY --chown=augur:augur ./README.md .
COPY --chown=augur:augur ./alembic.ini .
COPY --chown=augur:augur ./augur/ augur/
COPY --chown=augur:augur ./metadata.py .
COPY --chown=augur:augur ./setup.py .
COPY --chown=augur:augur ./scripts/ scripts/
COPY --chown=augur:augur ./keyman/ keyman/

# Create and configure virtual environment
RUN python3 -m venv /opt/venv && \
    chown -R augur:augur /opt/venv

# Install Python dependencies
RUN set -x \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install wheel \
    && /opt/venv/bin/pip install .

# Install worker dependencies
RUN ./scripts/docker/install-workers-deps.sh

# Copy Golang binaries
COPY --from=golang --chown=augur:augur "/root/scc" "/root/scc"
COPY --from=golang --chown=augur:augur "/root/scorecard/scorecard" "./scorecard"

# Create necessary directories with proper permissions
RUN mkdir -p /augur/repos /augur/logs /augur/facade && \
    chown -R augur:augur /augur

# Copy and configure entrypoint scripts
COPY --chown=augur:augur ./docker/backend/entrypoint.sh /
COPY --chown=augur:augur ./docker/backend/init.sh /
RUN chmod +x /entrypoint.sh /init.sh

# Switch to non-root user
USER augur

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
CMD /init.sh
