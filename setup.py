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
    description="""A python package to integrate gnd-js in a django-project""",
    author='Peter Andorfer',
    author_email='peter.andorfer@oeaw.ac.at',
    url='https://github.com/acdh-oeaw/django-gnd',
    packages=[
        'gnd',
    ],
    include_package_data=True,
    install_requires=[
        'requests>=2'
    ],
    license="MIT",
    zip_safe=False,
    keywords='django-gnd',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
    ],
)
