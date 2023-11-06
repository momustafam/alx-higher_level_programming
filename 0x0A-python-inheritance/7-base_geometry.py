#!/usr/bin/python3
'''The BaseGeometry module'''


class BaseGeometry:
    '''An empty class'''

    def area(self):
        '''funciton that raise an exception'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates the `value`'''

        if type(name) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
