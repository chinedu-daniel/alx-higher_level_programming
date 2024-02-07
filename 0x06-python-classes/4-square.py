#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):

        """Propert"""

        print("Retrieving the size")

        return self.__size

    @size.setter
    def size(self, value):


        """Property setter"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):


        """Calculates the area of the square.

        Return:
            int: The area of the square.
        """
        return self.__size ** 2
