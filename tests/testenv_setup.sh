#! /bin/bash

# Setup a small virtual environment for testing
virtualenv --clear testenv
source testenv/bin/activate
mkdir testenv/tmp
cd testenv/tmp
shopt -s extglob
cp -r ../../../!(tests) .
