#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ''' finda all multiplies of 2 in a list

    Args:
        my_list (list): the list being searched
    
    Returns: a new boolean list contains True of if the number multipliy of 2
            , False otherwise
    '''
    new_list = []

    for elem in my_list:
        if elem % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
