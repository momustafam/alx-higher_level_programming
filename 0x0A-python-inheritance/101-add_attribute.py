#!/usr/bin/python3
"""Easy Task"""

def add_attribute(obj, name, value):
    '''add a new attribute to an object if it's possible'''
    if hasattr(obj, '__dict__'):
        obj.name = value
    else:
        raise TypeError("can't add new attribute")

