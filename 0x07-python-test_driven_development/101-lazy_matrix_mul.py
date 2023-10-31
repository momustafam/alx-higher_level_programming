#!/usr/bin/python3
"""
    The 101-lazy_matrix_mul module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    A = np.array(m_a)
    B = np.array(m_b)

    return np.matmul(A, B)
