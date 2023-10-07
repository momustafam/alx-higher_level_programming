#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    ''' prints a matrix of integers

    Args:
        matrix (2d list): the matrix what you want to print

    Returns: NULL
    '''
    for row in matrix:
        n_col = len(row)
        for column in range(n_col):
            if column == (n_col - 1):
                print("{:d}".format(row[column]))
                break
            print("{:d} ".format(row[column]), end="")
