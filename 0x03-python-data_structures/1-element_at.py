#!/usr/bin/python3
def element_at(my_list, idx):
    '''
    Description: retrieves an element from a list like in C programming

    Args:
        my_list (list): the given list
        idx (int): the index of the element

    Return:
        - the element in the index idx in my_list if it's found,
        or None otherwise
    '''
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
