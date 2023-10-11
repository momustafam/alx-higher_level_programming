#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ''' computes the square value of all integers of a matrix

    Parameters:
    -----------
    matrix: 2 dimensional array
    the container being squared

    Returns:
    --------
    new_matrix: 2 dimensional array
    a container that includes squared values of the given matrix
    '''
    new_matrix = [list(map(lambda x: x**2, arr)) for arr in matrix]
    return new_matrix
