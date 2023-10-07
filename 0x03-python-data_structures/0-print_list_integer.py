#!/usr/bin/python3
def print_list_integer(my_list=[]):
    '''
    Description: prints all integers of a list

    Args:
        my_list (list): the given list

    Returns: NULL
    '''
    for elem in my_list:
        print("{:d}".format(elem))
