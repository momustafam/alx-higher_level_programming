#!/usr/bin/python3
"""Square module"""


class Square:
    """An incomplete class"""
    def __init__(self, size=0):
        """Instantiate a Square class with size equal to given size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the square of the size attribute"""
        return self.__size**2
