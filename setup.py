#!/usr/bin/env python

import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import hanging_threads

setup(name='hanging_threads',
      version=hanging_threads.__version__,
      description='Deadlocks? Detect where your threads hang in Python with one import.',
      long_description=hanging_threads.__doc__,
      author=hanging_threads.__author__,
      author_email='niccokunzmann' + '@' + 'gmail.com',
      url='https://github.com/niccokunzmann/hanging_threads',
      py_modules=['hanging_threads'],
      scripts=['hanging_threads.py'],
      license='MIT',
      platforms='any',
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.3',
                   'Programming Language :: Python :: 2.4',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   ],
      )