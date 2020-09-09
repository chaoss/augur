#!/bin/bash
set -eo pipefail

echo "Installing backend dependencies..."
echo "**********************************"
echo

target=$1

if [[ $target == *"prod"* ]]; then
    pip install -e .
else
    pip install -e .[dev]
fi

