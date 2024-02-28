import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        rect = Rectangle(5, 10, 2, 3)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_setters(self):
        rect = Rectangle(5, 10, 2, 3)

        # Test valid updates
        rect.width = 7
        rect.height = 12
        rect.x = 4
        rect.y = 6
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 6)

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

    def test_area_calculation(self):
        # Create a rectangle with width=5 and height=10
        rect = Rectangle(5, 10)
        # Test the area calculation
        self.assertEqual(rect.area(), 50)

        # Update width and height
        rect.width = 7
        rect.height = 3
        # Test the area calculation after update
        self.assertEqual(rect.area(), 21)

    def test_negative_values(self):
        # Test with negative values (should raise exceptions)
        rect = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rect.width = -5
            rect.area()
        with self.assertRaises(ValueError):
            rect.height = -10
            rect.area()

    def setUp(self):
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_display(self):
        # Create a rectangle with width=5 and height=3
        rect = Rectangle(5, 3)
        
        # Call display method
        rect.display()
        
        # Get the printed output
        printed_output = sys.stdout.getvalue()

        # Expected output
        expected_output = "#####\n#####\n#####\n"
        
        # Assert that printed output matches expected output
        self.assertEqual(printed_output, expected_output)

    def test_str(self):
        # Create a rectangle with id=1, width=5, height=3, x=2, y=1
        rect = Rectangle(5, 3, 2, 1, 1)

        # Call __str__ method
        rect_str = str(rect)

        # Expected output
        expected_output = "[Rectangle] (1) 2/1 - 5/3"

        # Assert that __str__ output matches expected output
        self.assertEqual(rect_str, expected_output)


if __name__ == "__main__":
    unittest.main()
