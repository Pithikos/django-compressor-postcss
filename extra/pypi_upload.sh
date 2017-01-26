#! /bin/bash

#
# Script to upload the project on PyPI
#

if [ -e "../README.md" ]; then
   cd ..
fi


echo "Installing dependencies.."
sudo apt-get install pandoc -yq &> /dev/null
pip install twine &> /dev/null


echo "Converting markdown to rst.."
output=`pandoc --from=markdown --to=rst README.md -o README.rst`
if [ $? = 1 ]; then
   echo "$output"
   exit 1
fi
sed -i -e 's/<[^>]*>//g' README.rst # remove any html tags
sed -i '/^.. raw:: html$/d' README.rst # remove '.. raw:: html'


echo "Building wheel.."
output=`python setup.py bdist_wheel --universal`
if [ $? = 1 ]; then
   echo "$output"
   exit 1
fi


echo "Uploading to PyPI.."
twine upload dist/django_compressor_postcss-*.whl
