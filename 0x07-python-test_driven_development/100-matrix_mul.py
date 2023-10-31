#!/usr/bin/python3
'''
    The 100-matrix_mul module.
'''


def matrix_mul(m_a, m_b):
    '''
        Function that multiplies 2 matrices.

        The m_a and m_b must be matrices of integers/floats.

        Args:
        -----
            m_a (list): the first matrix
            m_b (list): the second matrix
    '''

    is_rect1, is_rect2, result = 1, 1, 0
    multiplied_matrix = []

    # checking that the m_a and m_b are lists of lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for i in range(len(m_a)):
        row = m_a[i]
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if is_rect1 and i > 0:
            is_rect1 = 0 if len(row) != len(m_a[i-1]) else 1
        if not len(row):
            m_a.pop(i)
    for i in range(len(m_b)):
        row = m_b[i]
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if is_rect2 and i > 0:
            is_rect2 = 0 if len(row) != len(m_b[i-1]) else 1
        if not len(row):
            m_b.pop(i)

    # checking that the matrices are not empty lists
    if m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == []:
        raise ValueError("m_b can't be empty")

    # checking that each elem in each row in m_a is int/float
    for row in m_a:
        for elem in row:
            if not (isinstance(elem, int) or isinstance(elem, float)):
                raise TypeError("m_a should contain only integers or floats")
    # checking that each elem in each row in m_b is int/float
    for row in m_b:
        for elem in row:
            if not (isinstance(elem, int) or isinstance(elem, float)):
                raise TypeError("m_b should contain only integers or floats")

    # checking that the all rows of each matrix with the same length
    if not is_rect1:
        raise ValueError("each row of m_a must be of the same size")
    if not is_rect2:
        raise ValueError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # multiply m_a with m_b
    for row in m_a:
        multiplied_matrix.append([])
        for i in range(len(m_b[0])):
            result = 0
            for j in range(len(row)):
                result += row[j]*m_b[j][i]
            multiplied_matrix[-1].append(result)

    return multiplied_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
