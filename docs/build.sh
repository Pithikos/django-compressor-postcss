#! /bin/bash

#
# Build the documentation to .rst so that it's not a mess in the cheeseshop
#

echo "Install pandoc.."
sudo apt-get install pandoc -yq &> /dev/null

echo "Convert files.."
pandoc --from=markdown --to=rst ../README.md -o README.rst
