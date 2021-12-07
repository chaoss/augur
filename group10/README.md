# group10

## Overview

This document describes the work done for each sprint of integrating HTTPS support into Augur.

## Sprint 1

(Use case diagram not needed, discussed in meeting 2 for Sprint 1)

**Background:**

Our goal is to make Augur as safe and secure as possible in order to fully gain the trust and confidence of our users.
In order to maintain the highest standard and class possible, it is vital that web services only provide their services through a secure connection, and the strongest happens to be Hypertext Transfer Protocol Secure or HTTPS.

Standard HTTP does not protect data from being intercepted or altered, which can result in eavesdropping, tracking, and the modification of received data.
They create a privacy flaw and expose sensitive information about the users of the web services.
Data sent over HTTP is vulnerable to interception, manipulation, and impersonation.
HTTPS verifies the identity of a website and encrypts all vital information that is being sent.
This prevents the data from being intercepted and modified.

**Requirement(s):**

Make Augur compatible with HTTPS in order to provide the best, and most secure and reliable service for our users.

Ensure there are no conflicts with the current framework of Augur upon adding HTTPS compatibility as to avoid causing problems that would need to be solved or maintained in the future.
Ensure that existing tests still pass after implementation.

Make sure any internal links that worked with http now are properly changed to https, as this could also break some functionality.

**Development process:**

Methodology:
Do a team mob during the initial implementation to keep everyone on the same page.
Then, split up into sub-teams to tackle sub-components of the feature such as certificate generation/management, configuring flask to use the certificates, configuring all endpoints to use HTTPS.

Implementation steps:
- Acquire and setup SSL certificate
- Configure and update Augur (flask) to enable HTTPS
- Configure and update endpoints to use HTTPS

## Sprint 2

### Goals

1. Get access to the “group10” database and code so we can start testing https functionality
1. Install augur for development
1. Ensure installation is correct and that it can be rebuilt after changing code
1. Ensure existing tests pass
1. Create preliminary tests for https in case some critical system interferes with trying to modify the http functionality
1. Establish https functionality and compatibility on the guillotine.io server
1. Search for and clean out any bugs and issues created by the new functionality, so that it is ready to be transferred to the actual augur server

### Tests

There aren’t any new tests that need to be made specifically for our project, since our focus is making sure that existing tests and functionality all perform the same on https servers as they do with http.
Make sure https support doesn’t break existing tests.
Maybe add new tests for the API protocol.

## Sprint 3

### Experimentation

Our first attempt at serving the backend over HTTPS was to use a "snakeoil" certificate (self-signed) for a proof of concept.

The snakeoil certificate was generated with the following command:

```bash
group10@Ubuntu-2004-focal-64-minimal:~/github/augur/group10/certs$ openssl req \
  -newkey rsa:4096 -new -nodes -x509 -days 365 \
  -subj '/C=US/ST=MO/L=Columbia/O=University of Missouri, CS 4320, Group 10/CN=team10.guillotine.io' \
  -keyout augur-snakeoil.key -out augur-snakeoil.pem
```

Note: Both files were committed to the repository ([private key](./certs/augur-snakeoil.key), [certificate](./certs/augur-snakeoil.pem)), which is typically *highly discouraged*. Given that these files are self-signed and are only for a proof of concept, this poses no security risk.

Our first approach at the code lead us to try configuring the Flask server to use our certificate as seen in [this SO answer](https://stackoverflow.com/a/65152383/5673922). After searching through the code for a call to `Flask.run` we realized that the Flask server is managed by Gunicorn, meaning that we must configure Gunicorn and not Flask.

An example of Gunicorn SSL configuration can be seen in [this SO answer](https://stackoverflow.com/a/67129353/5673922), but Augur does not use a config file for Gunicorn. So, working forwards from running the backend start command we can find where Gunicorn is configured. When `augur backend start` is run, the corresponding function in `augur.cli.backend` is invoked which creates an instance of `augur.application.Application`. Here, we can see a dictionary named `gunicorn_options` which sets some familiar looking values that were also used in the config file from the previously mentioned SO answer. After adding `certfile` and `keyfile` with paths to our snakeoil cert files and restarting the server, we see the gunicorn log file changes to now use HTTPS in the URL on which it is listening.

Gunicorn log before config change:

```bash
(augur_env) group10@Ubuntu-2004-focal-64-minimal:~/github/augur$ cat logs/gunicorn.log
[2021-12-07 00:59:21 +0100] [486894] [INFO] Starting gunicorn 20.1.0
[2021-12-07 00:59:21 +0100] [486894] [INFO] Listening at: http://0.0.0.0:5099 (486894)  # Note the HTTP URL here
[2021-12-07 00:59:21 +0100] [486894] [INFO] Using worker: sync
[2021-12-07 00:59:21 +0100] [487129] [INFO] Booting worker with pid: 487129
[2021-12-07 00:59:21 +0100] [487130] [INFO] Booting worker with pid: 487130
[2021-12-07 00:59:21 +0100] [487131] [INFO] Booting worker with pid: 487131
[2021-12-07 00:59:21 +0100] [487132] [INFO] Booting worker with pid: 487132
[2021-12-07 00:59:21 +0100] [487133] [INFO] Booting worker with pid: 487133
[2021-12-07 00:59:21 +0100] [487134] [INFO] Booting worker with pid: 487134
```

The new Gunicorn config dictionary:

```python
self.gunicorn_options = {
    'bind': '%s:%s' % (self.config.get_value("Server", "host"), self.config.get_value("Server", "port")),
    'workers': int(self.config.get_value('Server', 'workers')),
    'timeout': int(self.config.get_value('Server', 'timeout')),
    **'certfile': '/home/group10/github/augur/group10/certs/augur-snakeoil.pem',**
    **'keyfile': '/home/group10/github/augur/group10/certs/augur-snakeoil.key'**
}
```

Restart the backend:

```bash
(augur_env) group10@Ubuntu-2004-focal-64-minimal:~/github/augur$ augur backend stop
(augur_env) group10@Ubuntu-2004-focal-64-minimal:~/github/augur$ augur backend kill
(augur_env) group10@Ubuntu-2004-focal-64-minimal:~/github/augur$ (nohup augur backend start >logs/test.out 2>logs/test.err &)
```

Gunicorn log after config change:

```bash
(augur_env) group10@Ubuntu-2004-focal-64-minimal:~/github/augur$ cat logs/gunicorn.log
[2021-12-07 01:00:32 +0100] [488873] [INFO] Starting gunicorn 20.1.0
[2021-12-07 01:00:32 +0100] [488873] [INFO] Listening at: https://0.0.0.0:5099 (488873)  # Note the HTTPS URL here
[2021-12-07 01:00:32 +0100] [488873] [INFO] Using worker: sync
[2021-12-07 01:00:32 +0100] [489111] [INFO] Booting worker with pid: 489111
[2021-12-07 01:00:32 +0100] [489114] [INFO] Booting worker with pid: 489114
[2021-12-07 01:00:32 +0100] [489116] [INFO] Booting worker with pid: 489116
[2021-12-07 01:00:32 +0100] [489119] [INFO] Booting worker with pid: 489119
[2021-12-07 01:00:32 +0100] [489138] [INFO] Booting worker with pid: 489138
```

Test endpoint with HTTPS URL:

```bash
# curl -L is required because the server will redirect
# curl -k is required because the certificate is not signed by a CA, this allows insecure connections
(augur_env) group10@Ubuntu-2004-focal-64-minimal:~/github/augur$ curl -ksSL https://localhost:5099/
{"status": "OK"}
```

New line in Gunicorn log from curl:

```bash
(augur_env) group10@Ubuntu-2004-focal-64-minimal:~/github/augur$ tail -2 logs/gunicorn.log
127.0.0.1 - - [07/Dec/2021:02:41:02 +0100] "GET / HTTP/1.1" 302 231 "-" "curl/7.68.0"
127.0.0.1 - - [07/Dec/2021:02:41:02 +0100] "GET /api/unstable HTTP/1.1" 200 16 "-" "curl/7.68.0"
```

### Improvements for the next sprint

- Get values for `certfile` and `keyfile` in `gunicorn_options` similarly to other options: from the augur config
- During installation, generate certificates or request them from letsencrypt
- Update frontend to use new HTTPS URL for backend queries
- Update frontend Nginx config to use the same certificate
