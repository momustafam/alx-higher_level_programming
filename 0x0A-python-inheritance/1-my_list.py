#!/usr/bin/pytho3
"""
    The ``1-my_list`` module

    Classes:
        - MyList
"""


class MyList(list):
    """A subclass inherits the built-in class list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        print(sorted(self))
