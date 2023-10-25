#!/usr/bin/python3
"""Square module"""


class Square:
    """An incomplete class"""
    def __init__(self, size=0):
        """Instantiate a Square class with size equal to given size"""
        self.size = size

    def __eq__(self, other):
        """equal function."""

        return self.area() == other.area()

    def __lt__(self, other):
        """less than function."""

        return self.area() < other.area()

    def __le__(self, other):
        """less than or equal."""

        return self.area() <= other.area()

    def __ne__(self, other):
        """not equal method"""

        return self.area() != other.area()

    def __gt__(self, other):
        """grater than method"""

        return self.area() > other.area()

    def __ge__(self, other):
        """greater than method."""

        return self.area() >= other.area()

    @property
    def size(self):
        """Return the value of the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Update the value of the size attribute"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the square of the size attribute"""
        return self.__size**2
