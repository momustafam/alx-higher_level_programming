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

    number_of_instances = 0
    print_symbol = '#'

    # Built-in Methods
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        string = ""

        if self.perimeter() != 0:
            for i in range(self.height):
                string += (str(self.print_symbol) * self.width)
                if i != (self.height - 1):
                    string += '\n'
            return string
        return string

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    # Public Instance Methods
    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    # Class Methods
    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    # Static Methods
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    # Pythonic way to define setters and getters
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
