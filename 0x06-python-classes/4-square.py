#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int): The size of the square (default 0)
        """

        self.size = size

    @property
    def size(self):

        """Retrieve the size of the square."""

        print("Retrieving the size")

        return self.__size

    @size.setter
    def size(self, value):


        """Set the size of the square.

        Args:
            value (int): The size of the square
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def area(self):


        """Calculates the area of the square."""
        return self.__size ** 2
