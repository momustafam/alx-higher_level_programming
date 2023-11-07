#!/usr/bin/python3
'''
    The ``1-write_file`` module
'''


def write_file(filename="", text=""):
    '''
    Writes a string to a text file(UTF8)

    Return the number of characters
    '''

    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)
