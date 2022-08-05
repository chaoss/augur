#!/bin/bash
set -eo pipefail

scripts/control/clean.sh

scripts/install/checks.sh
if [[ $? -ne 0 ]]; then
  exit 1
fi

target=${1-prod}

scripts/install/backend.sh $target

echo
echo
echo
echo "Database history shown below if current is not head please run augur db upgrade-db-version"
echo 
augur db check-for-upgrade
echo 
