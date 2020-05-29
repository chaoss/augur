import subprocess
import psycopg2
from subprocess import PIPE
import json
import re
import os
import requests
from os.path import expanduser

import sbom_populate as p
import initial_scans as s

if __name__ == "__main__":
    with open("../../augur.config.json") as json_file:
        config = json.load(json_file)
        dbname = config["Database"]["database"]
        user = config["Database"]["user"]
        password = config["Database"]["password"]
        host = config["Database"]["host"]
        port = config["Database"]["port"]
        dsfile = config["Workers"]["license_worker"]["tagfile"]
        depth = config["Workers"]["license_worker"]["search_depth"]
        ipath = config["Workers"]["facade_worker"]["repo_directory"]
        home = expanduser("~")

        print("IPATH EQUALS " + ipath)
        print("HOME EQUALS " + home)

        configtools = 'postgresql://{}:{}@{}:{}/{}'.format(
            user, password, host, port, dbname
        )

        with open("dosocs2-example.conf") as configfile:
            content = configfile.read()
            content_new = re.sub('(connection_uri = .*)\n', "connection_uri = " + configtools + "?options=--search_path=spdx\n", content)
            with open("dosocs2.conf","w+") as outfile:
                outfile.write(content_new)
            with open(home + "/.config/dosocs2/dosocs2.conf","w+") as coreconfig:
                coreconfig.write(content_new)

        wd = os.getcwd()

        print("---------------------")
        print("INITIAL SCANS RUNNING")
        print("---------------------")
        s.scan(dbname, user, password, host, port, dsfile, ipath, depth)
        #print(os.getcwd())
        os.chdir(wd)
        #print(os.getcwd())
        print("------------------")
        print("SBOM SCANS RUNNING")
        print("------------------")
        p.scan(dbname, user, password, host, port, dsfile, ipath)
