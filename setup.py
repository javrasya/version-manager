# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ahmetdal'

from setuptools import setup, find_packages

entrypoints = {}

console_scripts = entrypoints['console_scripts'] = [
    'update_version = src.bin.update_version:main',
    'current_version = src.bin.current_version:main',
]

# -*- %%% -*-

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ''

setup(
    name='version-manager',
    version='0.5.1',
    description="Version upgrader in all spesific files like setup.py, package.json, bower.json etc.",
    author="Ahmet DAL",
    author_email="ceahmetdal@gmail.com",
    url="https://github.com/javrasya/version-manager",
    platforms=['any'],
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'repoze.lru',
        'colorama'
    ],
    include_package_data=True,
    entry_points=entrypoints,
    long_description=long_description
)
