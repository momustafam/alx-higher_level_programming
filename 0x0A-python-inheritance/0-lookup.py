#!/usr/bin/python3
"""
    The lookup module is a very simple module, since it has a one function
    called ``lookup``
"""


def lookup(obj):
    """return the list of available attributes and methods of an object"""
    return dir(obj)
