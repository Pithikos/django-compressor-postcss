from setuptools import setup
import os
import io


def file_content(fname):
    return io.open(os.path.join(os.path.dirname(__file__), fname), encoding="UTF-8").read()


dist = setup(
    name='django-compressor-postcss',
    version='0.8',
    description='PostCSS support for django-compressor',
    long_description=file_content('docs/README.rst'),
    author='Johan Hanssen Seferidis',
    author_email='manossef@gmail.com',
    url='https://github.com/pithikos/django-compressor-postcss',
    license='MIT',

    classifiers=[
        'Intended Audience :: Developers'
        'License :: OSI Approved :: MIT License',
    ],
    keywords='django-compressor django postcss post-processing css ' +
             'web-development autoprefixer',

    # Package
    packages=['compressor_postcss'],
    install_requires=[
        'django'
        'django-compressor',
    ],
    data_files=[('', ['LICENSE', 'README.md'])],
)
