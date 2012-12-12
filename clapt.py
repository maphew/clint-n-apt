#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@+leo-ver=5-thin
#@+node:maphew.20121210013627.1447: * @file clint-n-apt/clapt.py
#@@first
#@@first
#@@language python
#@@tabwidth -4
print
#@+others
#@+node:maphew.20121210013627.1450: ** docstring
"""
clapt: a clint + apt o4w command line installer

clapt setup
    Create a skeleton osgeo4w file system, and download latest setup.ini

clapt update --mirror http://alternate.osgeo.org/osgeo4w/x64
    fetch new setup.ini, from a different mirror than usual

clapt install iconv curl ... --download-only
    fetch iconv and curl packages, but only store in local cache, don't install

clapt install iconv curl ... --from d:\downloads\osgeo4w\cache
    install iconv and curl from local file system, don't download anything

clapt remove iconv curl ...
    uninstall the iconv and curl packages

clapt list
    list installed packages

clapt locate filename.ext
    search installed packages for "filename.ext" and report where it was
    installed to

clapt search url
    search for substring "url" in installed and available packages, and
    report the package name:

        installed:  curl
        available:  furlagong, churlish

clapt requires iconv
    List packages which depend on iconv

clapt depends iconv
    List packages which iconv depends on
"""
#@+node:maphew.20121210013627.1448: ** imports etc.
import os
import sys

from clint import args
from clint.textui import puts, colored, indent, columns

d = args.grouped['_']
command = d[0]
packages = d[1:]
#@+node:maphew.20121210013627.1456: ** Options
try:
    mirror = args.grouped['--mirror'].get(0)
    puts('using mirror %s' % colored.green(mirror))
except KeyError :
    pass
#@+node:maphew.20121212012030.1379: ** Commands
#@+node:maphew.20121212012030.1376: *3* setup
def setup(location):
    print("Creating skeleton folder tree & database rooted at %s" % colored.green(location[0]))
#@+node:maphew.20121212012030.1378: *3* update
def update(mirror):
    puts("Fetching up to date package list from %s" % colored.green(mirror))
#@+node:maphew.20121210013627.1455: ** Package Commands
#@+node:maphew.20121210013627.1449: *3* install
def install(packages):
    for p in packages:
        puts('downloading and installing %s' % colored.green(p))

#@+node:maphew.20121210013627.1454: *3* remove
def remove(packages):
    for p in packages:
        puts('uninstalling %s' % colored.green(p))

#@+node:maphew.20121212012030.1377: ** dummy
def dummy():
    """Actually nothing has been done. This is a stub for yet to be implemented functions."""
    print("")    
    width = 60
    with indent(4, quote=colored.cyan('-->')):
        puts(columns([dummy.__doc__, width]))
#@+node:maphew.20121210013627.1457: ** Main
# this transforms into install(packages) or remove(packages) or list(packages) etc.
# courtesy of http://stackoverflow.com/questions/3061/calling-a-function-from-a-string-with-the-functions-name-in-python
locals()[command](packages)

dummy()
#@-others

#@-leo
