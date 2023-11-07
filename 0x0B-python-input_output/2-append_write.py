#!/usr/bin/python3
'''
    The 2-append_write module.
'''


def append_write(filename="", text=""):
    '''
        Append a string at the end of a file.

        Return the number of characters added
    '''

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
