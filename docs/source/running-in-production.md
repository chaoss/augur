# Running Augur in Production

This guide explains how to run Augur in a production environment.

## Prerequisites
- Docker and Docker Compose installed
- PostgreSQL database configured
- Redis installed and running

## Environment Variables
Make sure to configure the following environment variables:

- `AUGUR_RESET_LOGS`: Determines whether logs should be reset on startup.
- `REFRESH_MATERIALIZED_VIEWS_INTERVAL_IN_DAYS`: Controls how often materialized views are refreshed. (Default: 1 day)
- `AUGUR_DB`: Database connection string
- `AUGUR_REDIS_URL`: Redis connection string

## Related Resources
- [oss-aspen/infra-ansible](https://github.com/oss-aspen/infra-ansible/)
- [chaoss/augur-utilities](https://github.com/chaoss/augur-utilities/)

## Steps to Run
1. Clone the repository
   ```bash
   git clone https://github.com/chaoss/augur.git
   cd augur
