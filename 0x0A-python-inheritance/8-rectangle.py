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
