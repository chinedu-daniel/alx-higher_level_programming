import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        # Create a rectangle with width=5 and height=10
        rect = Rectangle(5, 10)
        # Test the area calculation
        self.assertEqual(rect.area(), 50)

        rect.width = 7
        rect.height = 3
        self.assertEqual(rect.area(), 21)

        with self.assertRaises(ValueError):
            rect.width = -5
            rect.area()
        with self.assertRaises(ValueError):
            rect.height = -10
            rect.area()

if __name__ == "__main__":
    unittest.main()

