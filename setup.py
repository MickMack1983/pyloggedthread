#!/usr/bin/env python

from distutils.core import setup
setup(
    name='pyloggedthread',
    version='1.0a',
    description='Basic replacement for threading.Thread that logs start and termination of thread and exceptions,',
    author='Mikael Magnusson',
    author_email='mikael.m.magnusson@gmail.com',
    packages=[ 'pyloggedthread'   ],
    requires=['logging']
)
