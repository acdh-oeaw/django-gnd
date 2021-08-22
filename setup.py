#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from gnd/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("gnd", "__init__.py")


setup(
    name='django-gnd',
    version=version,
    description="""A django package to query and store data from Lobid's GND-API""",
    author='Peter Andorfer',
    author_email='peter.andorfer@oeaw.ac.at',
    url='https://github.com/acdh-oeaw/django-gnd',
    packages=[
        'gnd',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=3.1',
        'pylobid>=1.3.1',
        'python-dateutil>=2.8'
    ],
    license="MIT",
    zip_safe=False,
    keywords='django-gnd'
)
