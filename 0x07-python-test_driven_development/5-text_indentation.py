#!/usr/bin/python3
'''
    The ``5-text_indentation`` module

    only has one funciton called ``text_indentation``
'''


def text_indentation(text):
    '''
        Function that prints a text with 2 new lines after each of those chars
        ., ? and :
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = False
    for char in text:
        if start and char == ' ':
            continue
        else:
            print(char, end='')
            start = False

        if char in ['.', '?', ':']:
            print("\n")
            start = True
