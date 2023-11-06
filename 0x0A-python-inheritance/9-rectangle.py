#!/usr/bin/python3
"""Module Rectangle
Creates a Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A rectangle class with BaseGeomtery class (inherit it)'''

    def __init__(self, width, height):
        '''
            Initialize an object of Rectangle class

            Args:
                - width: rectangle width
                - height: rectan
        '''

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Calculate the area of the rectangle object'''

        return self.__width * self.__height

    def __str__(self):
        '''overwrite the built-in str function'''

        return f"[Rectangle] {width}/{<height}
