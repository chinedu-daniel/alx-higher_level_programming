#!/usr/bin/python3

import unittest
from models.base import Base



class TestBase(unittest.TestCase):
    def test_constructor_with_id(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_constructor_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)


if __name__ == '__main__':
    unittest.main()
