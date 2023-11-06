#!/usr/bin/python3
"""
    The `2-is_same_class` module is a very simple, since it has a one function
    called `is_same_class(obj, a_class)`
"""


def is_same_class(obj, a_class):
    """
        Return True if the given obj is an instance of the given class.

        The function excepts the object class

        Args:
            obj: the object what you want to check its type
            a_class: the class what you want to check that object is
            an instance of it

        Return:
            True if it's an obj is instance of a_class
            False otherwise
    """

    return True if type(obj) is a_class else False
