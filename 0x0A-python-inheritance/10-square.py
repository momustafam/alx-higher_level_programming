#!/usr/bin/python3
'''
    The Square module
'''


Rectangle = __import__("8-rectangle").Rectangle

class Square(Rectangle):
    '''
        The Square class
    '''

    def __init__(self, size):
        '''Initialize an objec of Square class'''

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''Calculate the area of a square'''

        return size**2
