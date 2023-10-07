#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ''' replaces an element in a list at a specific position without
    modifying the original one (like in C)

    Args:
        my_list (list): the original list
        idx (int): index of the spcified element
        element (int): the new value of the element with index idx of my_list

    Returns: on success reutrns the new list, or the original list on failure
    '''
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = [elem for elem in my_list]
    new_list[idx] = element

    return new_list
