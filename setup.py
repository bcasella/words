#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='words',
    version='1.0',
    description='Words has two functions: verify if a given word is a palindrome, and to spell check in ptbr a word or phrase',
    author='Bruno Casella',
    author_email='brunocasella@gmail.com',
    url='https://github.com/bcasella/words',
    packages=['words'],
    eager_resources=['words/palavrasptbr.txt'],
      long_description="""\
      Words has two functions: verify if a given word is a palindrome, and to spell check in ptbr a word or phrase
      """,
      classifiers=[
          "License :: OSI Approved :: MIT",
          "Programming Language :: Python",
      ],
      license='MIT',
      install_requires=[
        'setuptools',
      ],
      entry_points={
          'console_scripts': [
              'words = words:main'
          ]
      },
      include_package_data = True,
      package_data={'words': ['words/palavrasptbr.txt']},

      )
