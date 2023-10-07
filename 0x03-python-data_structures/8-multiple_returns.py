#!/usr/bin/python3
def multiple_returns(sentence):
    ''' returns a tuple with the length of a string and its first character

    Args:
        sentence (string): used string from tuple

    Returns: a tuple with length of a string and its first character
    '''
    length = len(sentence)
    return (length, sentence[0]) if length != 0 else (length, None)
