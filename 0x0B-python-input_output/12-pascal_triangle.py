#!/usr/bin/python3
"""Module that contains solution for task 12"""


def pascal_triangle(n):
    """
        Creates a pascal triangle

        Args:
            n (int): height of triangle

        Returns: returns a list of lists of integers
                representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        row = [1]
        for i in range(len(tri) - 1):
            row.append(tri[i] + tri[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
