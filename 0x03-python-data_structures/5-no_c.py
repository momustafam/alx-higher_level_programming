#!/usr/bin/python3
def no_c(my_string):
    ''' removes all characters c and C from a string

    Args:
        my_string (string): the container

    Returns: the new string
    '''
    new_string = list(my_string)
    length = len(new_string)
    for i in range(length):
        char = new_string[i]
        if char in ['c', 'C']:
            new_string[i] = ''
    new_string = "".join(new_string)
    return new_string
