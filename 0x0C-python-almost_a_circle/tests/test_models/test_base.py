#!/usr/bin/python3
'''The `TestBase` Module.'''

import sys
sys.path.append("../../")

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Test the `Base` class.'''

    def setUp(self):
        self.base1 = Base()
        self.base2 = Base()


    def test__init__(self):
        '''Checking the constructor of the class.'''

        self.base3 = Base(10)
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 2)
        self.assertEqual(self.base3.id, 10)

if __name__ == '__main__':
    unittest.main()
