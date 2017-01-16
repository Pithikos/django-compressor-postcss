from setuptools import setup
from setuptools.command.install import install as orig_install
from shutil import copyfile
from pkg_resources import DistributionNotFound, get_distribution
import pkg_resources
import subprocess
import pkgutil
import os
import io
import sys


def is_compressor_installed():
    try:
        get_distribution('django-compressor')
        return True
    except DistributionNotFound:
        return False


def read(fname):
    return io.open(os.path.join(os.path.dirname(__file__), fname), encoding="UTF-8").read()


def pre_install():
    """Require django-compressor to be installed first"""
    # if not pkgutil.find_loader('compressor'):
    #     print('ERROR: django-compressor needs to be installed before installing this module')
    #     exit(1)
    pass


def post_install():
    """Copy module directly to django-compressor's filters"""
    pkg_resources.get_distribution('django-compressor')
    filters_path = pkg_resources.resource_filename('compressor', 'filters')
    src = os.path.join('compressor_postcss', 'postcss.py')
    dest = os.path.join(filters_path, 'postcss.py')
    copyfile(src, dest)


class install(orig_install):
    """Allow pre/post installation tasks"""
    def run(self):
        pre_install()
        orig_install.run(self)
        post_install()


if not is_compressor_installed():
    sys.stderr.write("ERROR: django-compressor needs to be installed before installing this module!\n")
    sys.stderr.write("Make sure you have installed the package and then try again\n")
    exit(1)


dist = setup(
    name='django-compressor-postcss',
    version='0.8',
    description='PostCSS support for django-compressor',
    long_description=read('README.md'),
    author='Johan Hanssen Seferidis',
    author_email='manossef@gmail.com',
    url='https://github.com/pithikos/django-compressor-postcss',
    license='MIT',

    classifiers=[
        'Intended Audience :: Developers'
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='django-compressor django postcss post-processing css web-development',

    # Package
    packages=['compressor_postcss'],
    install_requires=[
        'django-compressor',
    ],
    data_files=[('', ['LICENSE', 'README.md'])],

    # Customize installation so it extends Django Compressor
    cmdclass={'install': install}
)
