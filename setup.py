#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django_antimat',
    version='1.1',
    description='Django antimat is application for filtering snub words.',
    license='BSD',
    url='https://github.com/ruscoder/django_antimat',
    author='Vadim',
    author_email='Vadim <rusmiligamer@gmail.com>',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.8',
        'pymorphy>=0.5.6',
    ],
    keywords='django antimat anti snub',

    setup_requires=['pytest-runner', 'pytest-django', "setuptools>=25.1.6"],
    tests_require=['pytest'],
)
