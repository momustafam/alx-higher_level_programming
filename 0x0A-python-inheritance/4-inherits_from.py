#!/usr/bin/python3
'''
    The inherits_from module
'''


def inherits_from(obj, a_class):
    '''
        Return True if the object is an instance of a class that inherited
        from the specidied class, otherwise return False
    '''

    return issubclass(type(obj), a_class) and type(obj) is not a_class
