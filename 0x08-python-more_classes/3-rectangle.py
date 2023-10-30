#!/usr/bin/python3
"""
    The ``rectangle`` module

    A very simple module, since it have a one class called ``Rectangle``
    that defines a rectangle
"""


class Rectangle:
    '''
        A class that defines a rectangle
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        string = ""

        if self.perimeter() != 0:
            for i in range(self.height):
                string += ("#" * self.width)
                if i != (self.height - 1):
                    string += '\n'
            return string
        return string

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
