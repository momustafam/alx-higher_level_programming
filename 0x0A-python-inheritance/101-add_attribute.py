#!/usr/bin/python3
"""Easy Task"""

def add_attribute(obj, name, value):
    '''add a new attribute to an object if it's possible'''
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    elif not hasattr(obj, name) and hasattr(obj, '__slots_'):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
