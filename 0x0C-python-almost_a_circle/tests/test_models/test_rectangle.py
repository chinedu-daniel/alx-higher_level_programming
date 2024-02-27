import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_setters(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.width = 7
        rect.height = 12
        rect.x = 4
        rect.y = 6
        rect.id = 2
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 6)
        self.assertEqual(rect.id, 2)

        # Test invalid updates
        with self.assertRaises(TypeError):
            rect.width = "invalid"
        with self.assertRaises(ValueError):
            rect.width = 0
        with self.assertRaises(ValueError):
            rect.x = -1
        with self.assertRaises(TypeError):
            rect.height = "invalid"
        with self.assertRaises(ValueError):
            rect.height = 0
        with self.assertRaises(ValueError):
            rect.y = -1

if __name__ == "__main__":
    unittest.main()
