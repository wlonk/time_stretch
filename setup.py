#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import time_stretch
version = time_stretch.__version__

setup(
    name='time_stretch',
    version=version,
    author='',
    author_email='bwarren2@gmail.com',
    packages=[
        'time_stretch',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['time_stretch/manage.py'],
)
