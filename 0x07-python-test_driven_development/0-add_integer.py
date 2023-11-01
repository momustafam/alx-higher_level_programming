#!/usr/bin/python3
"""
    a simple module that has a one function

    add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
        Return addition of 2 integers
    """

    if not (isinstance(a, int) or isinstance(a, float) or b == float("NaN"):
        raise TypeError("a must be an integer")
    elif isinstance(a, float):
        a = int(a)

    if not (isinstance(b, int) or isinstance(b, float) or b == float("NaN"):
        raise TypeError("b must be an integer")
    elif isinstance(b, float):
        b = int(b)

    return a + b
