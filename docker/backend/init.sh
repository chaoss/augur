#!/bin/bash
#SPDX-License-Identifier: MIT
set -e

if [[ "$AUGUR_DB_SCHEMA_BUILD" == "1" ]]; then
    augur db create-schema
fi


if [ ! -v AUGUR_NO_CONFIG ]; then
	./scripts/install/config.sh docker
fi

if [[ -f /repo_groups.csv ]]; then
    augur db add-repo-groups /repo_groups.csv
fi

if [[ -f /repos.csv ]]; then
   augur db add-repos /repos.csv
fi

if [[ -d /augur/logs ]]; then
    echo "The directory exists" > /augur/logs/log.holder

fi

echo $PATH

exec augur backend start
