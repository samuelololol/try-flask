#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Dec 07, 2014 '
__author__= 'samuel'

from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt', 'r') as f:
    reqs = f.read()

requires = []
for line in reqs.splitlines():
    requires.append(line)
requires = requires[::-1]

setup(
        name='cerebro',
        version='0.1',
        long_description=__doc__,
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=requires,
        author='samuelololol',
        author_email='samuelololol@gmail.com',
        )
