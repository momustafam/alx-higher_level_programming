#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ''' adds 2 tuples

    Args:
        tuple_a (tuple): first tuple
        tuple_b (tuple): second tuple

    Returns: a tuple with 2 integers:
            - the first one is the addition of the first element of each arg
            - the second one is the addition of the second element of each arg
    '''
    i = 0
    sum1, sum2 = 0, 0
    for elem in tuple_a:
        sum1 = elem if i == 0 else sum1
        sum2 = elem if i == 1 else 0

        i += 1
        if i > 1:
            break
    i = 0
    for elem in tuple_b:
        sum1 += elem if i == 0 else 0
        sum2 += elem if i == 1 else 0

        i += 1
        if i > 1:
            break

    return (sum1, sum2)
