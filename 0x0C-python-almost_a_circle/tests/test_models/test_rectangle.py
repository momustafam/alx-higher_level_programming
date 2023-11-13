#!/usr/bin/python3
'''The `TestRectangle` Module.'''

from sys import path
path.append("../../")

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):
    '''Test the `Rectangle` class.'''

    def test__init__(self):
        self.rect1 = Rectangle(2, 4, 10, 15, 324)
        self.rect2 = Rectangle(2, 5)

        self.assertEqual(self.rect1.width, 2)
        self.assertEqual(self.rect1.height, 4)
        self.assertEqual(self.rect1.x, 10)
        self.assertEqual(self.rect1.y, 15)
        self.assertEqual(self.rect1.id, 324)

        self.assertEqual(self.rect2.width, 2)
        self.assertEqual(self.rect2.height, 5)
        self.assertEqual(self.rect2.x, 0)
        self.assertEqual(self.rect2.y, 0)
        self.assertEqual(self.rect2.id, 3)

        with self.assertRaises(TypeError):
            self.rect3 = Rectangle()
            self.rect4 = Rectangle(234)
            self.rect5 = Rectangle('234', 23)
            self.rect6 = Rectangle(234, '234')

        with self.assertRaises(ValueError):
            self.rect7 = Rectangle(-1, 32)
            self.rect8 = Rectangle(32, 0)

    def test_area(self):
        self.rect1 = Rectangle(2, 4)
        self.rect2 = Rectangle(4, 4, 12, 325, 2)
        self.rect3 = Rectangle(4, 5, 213, 2)

        self.assertEqual(self.rect1.area(), 8)
        self.assertEqual(self.rect2.area(), 16)
        self.assertEqual(self.rect3.area(), 20)

    def test__str__(self):
        self.r1 = Rectangle(4, 6, 2, 1, 12)
        self.r2 = Rectangle(5, 5, 1)
        self.s1 = Square(1, 3, 12, 5)
        res1 = "[Rectangle] (12) 2/1 - 4/6"
        res2 = "[Rectangle] (4) 1/0 - 5/5"
        res3 = "[Square] (5) 3/12 - 1"

        self.assertEqual(str(self.r1), res1)
        self.assertEqual(str(self.r2), res2)
        self.assertEqual(str(self.s1), res3)

if __name__ == '__main__':
    unittest.main()
