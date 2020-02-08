#!/bin/bash

rm -rf dist

python setup.py sdist
pip install $(find dist -name neshan-*.tar.gz)
