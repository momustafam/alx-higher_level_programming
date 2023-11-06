#!/usr/bin/python3
"""
    The Module base_Geometry

    Creates a BaseGeometry class
"""


class BaseGeometry:
    """Class with public instance methods"""

    def area(self):
        """Raises an Exception with the message"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
