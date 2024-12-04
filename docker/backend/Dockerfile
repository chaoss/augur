# Stage 1: Builder
FROM python:3.11-slim-bullseye AS builder

LABEL maintainer="outdoors@acm.org"
LABEL version="0.76.6"

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/bin/:/usr/local/bin:/usr/lib:${PATH}"

# Install build dependencies
RUN apt-get update && apt-get -y install \
        git \
        gcc \
        python3-dev \
        python3-venv \
        wget \
        curl \
        postgresql-client \
        libpq-dev \
        && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Add cargo and rustup to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Install specific version of Rust
RUN rustup install 1.78.0 && rustup default 1.78.0

# Create virtual environment
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip wheel

# Copy application code
WORKDIR /augur
COPY ./setup.py .
COPY ./scripts/ scripts/
COPY ./alembic.ini .
COPY ./metadata.py .
COPY ./augur/ augur/
COPY ./README.md .

# Install application dependencies
RUN /opt/venv/bin/pip install .

# Stage 2: Runtime
FROM python:3.11-slim-bullseye AS runtime

LABEL maintainer="outdoors@acm.org"
LABEL version="0.76.5"

# Install runtime dependencies, including jq, curl, and wget
RUN apt-get update && apt-get install -y \
        postgresql-client \
        firefox-esr \
        chromium \
        tar \
        chromium-driver \
        jq \                    
        wget \                  
        curl \                   
        && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Geckodriver
RUN GECKODRIVER_VERSION=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | jq -r '.tag_name' | sed 's/v//') \
    && ARCH=$(uname -m) \
    && if [ "$ARCH" = "aarch64" ]; then \
         GECKODRIVER_URL="https://github.com/mozilla/geckodriver/releases/download/v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux-aarch64.tar.gz"; \
       else \
         GECKODRIVER_URL="https://github.com/mozilla/geckodriver/releases/download/v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz"; \
       fi \
    && wget $GECKODRIVER_URL \
    && tar -xzf geckodriver-v${GECKODRIVER_VERSION}-linux*.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && rm geckodriver-v${GECKODRIVER_VERSION}-linux*.tar.gz

# Copy virtual environment and application code from builder
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /augur /augur

# Execute the install-workers-deps.sh script here
RUN chmod +x /augur/scripts/docker/install-workers-deps.sh /augur/scripts/docker/install-go.sh
RUN ./augur/scripts/docker/install-workers-deps.sh 
RUN ./augur/scripts/docker/install-go.sh

RUN mkdir -p /augur/facade/ repos/ logs/

COPY ./docker/backend/entrypoint.sh /
COPY ./docker/backend/init.sh /
RUN chmod +x /entrypoint.sh /init.sh

# Set the environment
ENV PATH="/opt/venv/bin:/root/.cargo/bin:${PATH}"

EXPOSE 5000
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
CMD ["/init.sh"]