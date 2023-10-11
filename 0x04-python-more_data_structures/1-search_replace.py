#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ''' replaces all occurrences of an element by another in a new list

    Parameters:
    -----------
    my_list: the initial list
    search: the element to replace in the list
    replace: the new element

    Returns:
    --------
    new_list: the update list of my_list
    '''
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
