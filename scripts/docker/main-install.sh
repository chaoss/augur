#!/bin/bash

#This needs to be run as augur user.
sudo --user=augur source /home/augur/virtualenv/augur_env/bin/activate
set -x

#so does this.
sudo --user=augur pip install .