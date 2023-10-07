#!/usr/bin/python3
def max_integer(my_list=[]):
    ''' finds the biggest integer of a list

    Args:
        my_list (list): the container of elements

    Returns: the max element in my_list
    '''
    if my_list = []:
        return None
    _max = my_list[0]
    for elem in my_list:
        if elem > _max:
            _max = elem
    return _max
