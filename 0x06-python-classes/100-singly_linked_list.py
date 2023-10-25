#!/usr/bin/python3
"""
This module provides utility classes for Singlylinkedlist data structure.

The classes in this module can be used to create a list and manipulate it,
such as inserting, removing a node, ...etc.
"""


class Node:
    """
    A class to define a node of a singly linked list.

    Instance Attributes:
        - __data (int): the data value of the node.
        - __next_node (pointer): a pointer points to the next node in the list.

    Inhertiance: this class doesn't inherit from any other class.
    """

    def __init__(self, data, next_node=None):
        """
        Instantiate a node object with its data value and its next node.

        Args:
            - data (int): the data value of the new node
            - next_node (pointer): address of the next node of the new node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return the data value of an node object."""

        return self.__data

    @data.setter
    def data(self, value):
        """Update the value of an object node."""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return the next node after the given object node."""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Update the address of the next node of an object node."""

        if (not isinstance(value, Node)) and (value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list

    Instance Attributes:
        - __head (pointer): pointer points to the first node of the list
    """

    def __init__(self):
        """Instantiate a singlylinkedlist object."""

        self.__head = None

    def __str__(self):
        """print the entire list in stdout, one node number per line."""

        cur = self.__head
        string = ""

        while cur:
            string += str(cur.data)
            if cur.next_node:
                string += '\n'
            cur = cur.next_node

        return string

    def sorted_insert(self, value):
        """
        Inserts a new node into the correct stored position in the list

        Args:
            - value (int): the data value of the new node
        """

        prev, cur = None, self.__head
        new_node = Node(value)

        # handle empty linked list
        if not cur:
            self.__head = new_node
            return

        # search about the correct position and insert the new node
        while cur:
            if cur.data >= value:
                new_node.next_node = cur
                if not prev:
                    self.__head = new_node
                else:
                    prev.next_node = new_node
                return
            prev = cur
            cur = cur.next_node
        prev.next_node = new_node
