#!/usr/bin/python3
'''The MyInt module'''


class MyInt(int):
    '''Class that invert the == and != operators of the int class.'''

    def __eq__(self, other):
        '''equal method'''

        super().__ne__(other)

    def __ne__(self, other):
        '''not equal method'''

        super().__eq__(other)
