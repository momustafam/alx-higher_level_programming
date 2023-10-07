#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    ''' replaces an element of a list at a specific position (like in C)

    Args:
        my_list (list): the given list
        idx (int): the index of the element
        element (int): the new value of the my_list[idx]

    Returns: on success the new list, or the original list on failure
    '''
    # handle invalid given index
    if idx < 0 or idx >= len(my_list):
        return my_list
    # update the element with index idx in the given list
    my_list[idx] = element
    return my_list
