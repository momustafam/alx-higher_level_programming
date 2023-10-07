#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ''' prints all integers of a list, in reverse order

    Args:
        my_list (list): the list what you want to reverse it

    Returns: NULL
    '''
    if my_list is None:
        print("", end="")
    else:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
