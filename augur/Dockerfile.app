FROM python:3.11-slim-bullseye

# Create a non-root user and group
RUN groupadd -r augur -g 1000 && \
    useradd -r -g augur -u 1000 augur && \
    mkdir -p /home/augur/.augur/logs && \
    chown -R augur:augur /home/augur && \
    chmod -R 755 /home/augur

# Install required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set ownership of application files
RUN chown -R augur:augur /app && \
    chmod -R 755 /app

# Switch to non-root user
USER augur

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV HOME=/home/augur

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Default command
CMD ["python", "test_container_logging.py"] 