#!/usr/bin/python3
""" python 3 file """


class BaseGeometry:
    """
    Base class for geometric shapes.

    This class provides common functionality and attributes
    Subclasses can inherit from this class to implement
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        Raises:
            Exception: Indicates that the method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the integer value for a given attribute.

        Parameters:
            name (str): The name of the attribute.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from BaseGeometry

    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with given width and height

        Parameters:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less than or equal to 0

        """

        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def __str__(self):
        """
        Returns a string representation of the rectangle

        Returns:
            str: A string representation of the rectangle

        """

        return (f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        """
        Calculate the area of the rectangle

        Returns:
            int: The area of the rectangle

        """

        return self.__width * self.__height
