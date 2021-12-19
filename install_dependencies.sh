#!/bin/bash
set -eo pipefail

sudo apt update
sudo apt upgrade -y
sudo apt install -y postgresql postgresql-contrib
sudo apt install -y build-essential
sudo apt install -y python3-venv
sudo apt install -y python3-pip
sudo python3 -m pip install tensorflow==2.5.1
sudo apt install -y golang
sudo apt install -y nodejs
sudo apt install -y npm
sudo npm install vue
sudo npm install -g @vue/cli

echo
echo "*********************************"
echo "Setting up PostgreSQL Database..."
echo "*********************************"
echo

read -p "Database name: " database
read -p "Username: " username
while true; do
  read -s -p "Password: " password
  echo
  read -s -p "Retype password: " password2
  echo
  if [ "$password" = "$password2" ]; then
    break
  else
    echo "Sorry, passwords do not match. Please try again."
    echo
  fi
done

sudo -i -u postgres psql -c "CREATE DATABASE $database;"
sudo -i -u postgres psql -c "CREATE USER $username WITH ENCRYPTED PASSWORD '$password';"
sudo -i -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $database TO $username;"

echo
echo "********************************************"
echo "***** FINISHED INSTALLING DEPENDENCIES *****"
echo "********************************************"