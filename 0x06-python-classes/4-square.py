#!/usr/bin/python3
"""Square module"""


class Square:
    """An incomplete class"""
    def __init__(self, size=0):
        """Instantiate a Square class with size equal to given size"""
        self.size = size

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
