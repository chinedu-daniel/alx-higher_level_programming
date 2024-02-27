#!/usr/bin/python3
"""
test casses
"""

import unittest
from models.base import Base


class TestRectangle(unittest.TestCase):
    def test_constructor_with_id(self):
        rect = Rectangle(10, 20, 1, 2, 5)
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)

    def test_constructor_without_id(self):
        rect = Rectangle(5, 10, 2, 3)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_getters_and_setters(self):
        rect = Rectangle(10, 20, 1, 2, 5)
        rect.width = 15
        rect.height = 25
        rect.x = 3
        rect.y = 4
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

if __name__ == '__main__':
    unittest.main()
