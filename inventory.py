#! /usr/bin/python

# Simple inventory script to be used by jenkins
# ANSIBLE_TARGET is set by a jenkins parameter

from os import environ
from json import dumps


if environ.get('ANSIBLE_TARGET'):
    ANSIBLE_TARGET = environ.get('ANSIBLE_TARGET')
else:
    print "ANSIBLE_TARGET environmet variable not set"
    exit(1)

inventory = { "web": { "hosts": [ ANSIBLE_TARGET ] } } 



print dumps(inventory)