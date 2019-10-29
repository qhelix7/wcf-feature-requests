#!/usr/bin/env python
from distutils.core import setup

import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="feature_server",
    version="1.0.0",
    author="Martin Mayne",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=[],
    packages=setuptools.find_packages(exclude=["tests"]),
)
