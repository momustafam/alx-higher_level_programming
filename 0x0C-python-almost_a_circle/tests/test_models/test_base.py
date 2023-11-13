#!/usr/bin/python3
'''The `TestBase` Module.'''

import sys
sys.path.append("../../")

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
	'''Test the `Base` Class.'''

	def test_instantiation(self):
		'''Checking that the new instance of the class with a right id value.'''

		base1 = Base()
		base2 = Base(10)
		base3 = Base()

		self.assertEqual(base1.id, 1)
		self.assertEqual(base2.id, 10)
		self.assertEqual(base3.id, 2)


if __name__ == '__main__':
    unittest.main()
