#!/bin/bash

set -exo pipefail

if ! python3 -m pip --version; then
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    sudo python3 get-pip.py
    sudo python3 -m pip install nox
else
    python3 -m pip install nox
fi
