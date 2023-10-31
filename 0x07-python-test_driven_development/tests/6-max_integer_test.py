#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
        TestCase Class that test the max_integer of the 6-max_integer module

        functions:
            test_valid_inputs()
            test_empty_inputs(self)
            test_invalid_inputs(self)
    '''

    def test_valid_inputs(self):
        '''Test max_integer outputs by passing valid non-empty inputs'''

        t1 = [1, 2, 3, float("NaN"), 4, 5]
        t2 = t1[::-1]
        t3 = [3.0, 235.1352, 52.45, 89.234, 289.123, float("inf"), 1e10]
        t4 = [-2, 0, 2, -5, -10, 34]
        t5 = [10 for i in range(5)]

        self.assertEqual(max_integer(t1), 5)
        self.assertEqual(max_integer(t2), 5)
        self.assertEqual(max_integer(t3), float("inf"))
        self.assertEqual(max_integer(t4), 34)
        self.assertEqual(max_integer(t5), 10)

    def test_empty_inputs(self):
        '''Test max_integer outputs by passing empty inputs'''

        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_invalid_inputs(self):
        '''
        Test max_integer exceptions, warnings, and log messages
        by passing invalid inputs.
        '''

        with self.assertRaises(TypeError):
            max_integer(None)
            max_integer(324)
            max_integer(-34j)
            max_integer("test")
            max_integer([100, "s", None, 10.1, True, [12]])
