#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='auto_twitter',
      version='0.0.1',
      packages=find_packages(),
      package_data = {
          # If any package contains *.txt or *.rst files, include them:
          '': ['*.json'],

          },
      install_requires=['robotframework-selenium2library','robotframework-faker'],
      )
