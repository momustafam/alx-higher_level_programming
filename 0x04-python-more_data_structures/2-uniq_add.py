#!/usr/bin/python3
def uniq_add(my_list=[]):
    ''' add all unique integers in a list (only once for each intgere)

    Parameters:
    -----------
    my_list: two dimensional array

    Returns:
    --------
    summation of the my_list values after removing its duplicate values
    '''
    return sum(set(my_list))
