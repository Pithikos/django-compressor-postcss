#! /bin/bash

#
# Build the documentation to .rst so that it's not a mess in the cheeseshop
#

echo "Install pandoc.."
sudo apt-get install pandoc -yq &> /dev/null

echo "Convert files.."
if [ `ls README.md` ]; then
   README_PATH='.'
elif [ `ls ../README.md` ]; then
   README_PATH='..'
fi

pandoc --from=markdown --to=rst "$README_PATH"/README.md -o "$README_PATH"/docs/README.rst
