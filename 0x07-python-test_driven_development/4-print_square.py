#!/usr/bin/python3
"""
    The 4-print_square module
    Functions:
        print_square(szie)
"""


def print_square(size):
    '''
        A function that prints a square with the character #.
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#"*size)
