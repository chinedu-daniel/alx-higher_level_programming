import unittest

def max_integer(lst=[]):
    """
    Returns the maximum integer or float from a list of numbers.

    Args:
        lst (list): A list of integers or floats.

    Returns:
        int or float: The maximum number in the list. Returns None if the list is empty.

    Example:
        >>> max_integer([1, 2, 3, 4, 5])
        5

    """

    if not lst:
        return None
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

class TestMaxInteger(unittest.TestCase):
    """
    Unit tests for the max_integer function.
    """

    def test_empty_list(self):
        """
        Test case for an empty list.
        """
        self.assertIsNone(max_integer([]), "Empty list should return None")

    def test_single_element_list(self):
        """
        Test case for a single element list.
        """
        self.assertEqual(max_integer([5]), 5, "Single element list should return the element itself")

    def test_positive_numbers(self):
        """
        Test case for a list of positive numbers.
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5, "List of positive numbers should return the maximum")

    def test_negative_numbers(self):
        """
        Test case for a list of negative numbers.
        """
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1, "List of negative numbers should return the maximum")

    def test_mixed_numbers(self):
        """
        Test case for a list of mixed numbers.
        """
        self.assertEqual(max_integer([-5, 1, 0, -3, 2]), 2, "List of mixed numbers should return the maximum")

    def test_float_numbers(self):
        """
        Test case for a list of float numbers.
        """
        self.assertEqual(max_integer([1.5, 2.7, 3.8]), 3.8, "List of float numbers should return the maximum")

    def test_string_elements(self):
        """
        Test case for a list of string elements.
        """
        self.assertEqual(max_integer(["apple", "banana", "orange"]), "orange", "List of strings should return the maximum")

if __name__ == '__main__':
    unittest.main()

