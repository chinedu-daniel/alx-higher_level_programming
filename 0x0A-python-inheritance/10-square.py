#!/usr/bin/python3

class BaseGeometry:
    """
    Base class for geometric shapes.

    This class provides common functionality and attributes for geometric shapes.
    Subclasses can inherit from this class to implement specific geometric shapes.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        Raises:
            Exception: Indicates that the method is not implemented in the subclass.
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
    Represents a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with given width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        super().__init__()  # Call the constructor of the base class
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a square with a given size.

        Parameters:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size)

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        self._Rectangle__width = self.integer_validator("size", value)
        self._Rectangle__height = self.integer_validator("size", value)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"

