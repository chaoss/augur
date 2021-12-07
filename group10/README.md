# group10

## Overview

This document describes the work done for each sprint of integrating HTTPS support into Augur.

## Sprint 1

- Added the requirements document for HTTPS modifications.

## Sprint 2

- Goals document (detailing plan of action for implementing our sprint goals) created

## Sprint 3

- Testing and documentation: 


certfile and keyfile alteration: 

        self.gunicorn_options = {
            'bind': '%s:%s' % (self.config.get_value("Server", "host"), self.config.get_value("Server", "port")),
            'workers': int(self.config.get_value('Server', 'workers')),
            'timeout': int(self.config.get_value('Server', 'timeout')),
            'certfile': '/home/group10/github/augur/certs/ssl-cert-snakeoil.pem',
            'keyfile': '/home/group10/github/augur/certs/ssl-cert-snakeoil.key'
        }

# GUnicorn backend with certfile and keyfile before and after: 
before- 
[2021-12-07 00:59:21 +0100] [486894] [INFO] Starting gunicorn 20.1.0
[2021-12-07 00:59:21 +0100] [486894] [INFO] Listening at: http://0.0.0.0:5099 (486894)
[2021-12-07 00:59:21 +0100] [486894] [INFO] Using worker: sync
[2021-12-07 00:59:21 +0100] [487129] [INFO] Booting worker with pid: 487129
[2021-12-07 00:59:21 +0100] [487130] [INFO] Booting worker with pid: 487130
[2021-12-07 00:59:21 +0100] [487131] [INFO] Booting worker with pid: 487131
[2021-12-07 00:59:21 +0100] [487132] [INFO] Booting worker with pid: 487132
[2021-12-07 00:59:21 +0100] [487133] [INFO] Booting worker with pid: 487133
[2021-12-07 00:59:21 +0100] [487134] [INFO] Booting worker with pid: 487134

after-
cat logs/gunicorn.log 
[2021-12-07 01:00:32 +0100] [488873] [INFO] Starting gunicorn 20.1.0
[2021-12-07 01:00:32 +0100] [488873] [INFO] Listening at: https://0.0.0.0:5099 (488873)
[2021-12-07 01:00:32 +0100] [488873] [INFO] Using worker: sync
[2021-12-07 01:00:32 +0100] [489111] [INFO] Booting worker with pid: 489111
[2021-12-07 01:00:32 +0100] [489114] [INFO] Booting worker with pid: 489114
[2021-12-07 01:00:32 +0100] [489116] [INFO] Booting worker with pid: 489116
[2021-12-07 01:00:32 +0100] [489119] [INFO] Booting worker with pid: 489119
[2021-12-07 01:00:32 +0100] [489138] [INFO] Booting worker with pid: 489138
