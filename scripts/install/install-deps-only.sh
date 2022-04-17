#!/bin/bash
set -eo pipefail

scripts/install/checks.sh
if [[ $? -ne 0 ]]; then
  exit 1
fi

target=${1-prod}

if [[ $target == *"dev"* ]]; then
  echo
  echo "*****INSTALLING FOR DEVELOPMENT*****"
  echo
else
  echo
  echo "*****INSTALLING FOR PRODUCTION*****"
  echo
fi

scripts/install/backend.sh $target 2>&1 | tee logs/backend-install.log
echo "Done!"

scripts/install/workers.sh $target 2>&1 | tee logs/workers-install.log
echo "Done!"

scripts/install/frontend.sh
scripts/install/nltk_dictionaries.sh

echo "**********************************"
echo "***** INSTALLATION COMPLETE *****"
echo "**********************************"
