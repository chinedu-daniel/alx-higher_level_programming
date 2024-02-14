#!/usr/bin/python3
"""

This module provides a function to add two integers.

"""

def add_integer(a, b=98):
    """

    Add two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Default is 98.


    Returns:
        int: The sum of a and b.


    Raises:
        TypeError: If a or b is not an integer or float.
    """

    # Check if a and b are integers or floats

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats

    a = int(a)
    b = int(b)

    # Return the addition of a and b

    return (a + b)
