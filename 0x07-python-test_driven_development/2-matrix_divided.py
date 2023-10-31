#!/usr/bin/python3
"""
    The ``matrix_divided`` module

    A simple module, since it has a single function matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
        divides all elements of a matrix
    """

    length = None
    new_matrix = []
    err_mess = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(errr_mess)

    for i in range(len(matrix)):
        row = matrix[i]
        if not isinstance(row, list):
            raise TypeError(err_mess)

        if len(row) != length and length is not None:
            raise TypeError("Each row of the matrix must have the same size")
        length = len(row)
        new_matrix.append([])

        for j in range(length):
            elem = matrix[i][j]
            if not (isinstance(elem, int) or isinstance(elem, float)):
                raise TypeError(err_mess)
            new_matrix[i].append(round(elem / div, 2))

    if not (isinstance(div, float) or isinstance(div, int)):
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return new_matrix
