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

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
