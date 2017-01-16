#! /bin/bash

. testenv_setup.sh

# Build distribution without django-compressor preinstalled
python setup.py sdist
if [ $? = 0 ]; then
   echo "Should not build distribution without django-compressor preinstalled"
   exit 1
fi

# Build distribution with django-compressor preinstalled
pip install django-compressor
python setup.py sdist
if [ $? = 1 ]; then
   echo "Should build distribution with django-compressor preinstalled"
   exit 1
fi

# Install distribution
pip install dist/*.gz
if [[ $? -eq 1 ]]; then
   echo "Should install without problems"
   exit 1
fi
