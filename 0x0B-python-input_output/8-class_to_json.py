#!/usr/bin/python3
"""Module that contains the solution for task 8."""


def class_to_json(obj):
    """
        JSON serialization of an object.

        Args:
            obj (any): object

        Returns: the dictionary description with simple data structure
    """
    return obj.__dict__
