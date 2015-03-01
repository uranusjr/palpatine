#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = ()
if os.name != 'posix':
    requirements += ('colorama',)

test_requirements = (
    'mock',
    'nose',
)

setup(
    name='palpatine',
    version='0.1.0',
    description='Manipulate your console screen like an emperor.',
    long_description=readme + '\n\n' + history,
    author='Tzu-ping Chung',
    author_email='uranusjr@gmail.com',
    url='https://github.com/uranusjr/palpatine',
    packages=[
        'palpatine',
    ],
    package_dir={'palpatine':
                 'palpatine'},
    include_package_data=True,
    install_requires=requirements,
    license='BSD',
    zip_safe=False,
    keywords='palpatine',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
