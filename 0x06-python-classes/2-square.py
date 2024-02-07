#!/usr/bin/python3
"""Define a Square class."""

class Square:
    """Represent a Square."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int): The size of the square.
            Defaults to 0.

            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size