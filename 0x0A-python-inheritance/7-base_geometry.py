#!/usr/bin/python3
""" python3 file """

class BaseGeometry:
    
    """

    Base class for geometric shapes.

    This class provides common functionality and attributes for geometric shapes
    Subclasses can inherit from this class to implement specific geometric shapes

    """

    def area(self):
        """
        Calculate the area of the geometric shape

        Raises:
            Exception: Indicates that the method is not implemented in the subclass

        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the integeer value for a given attribute

        Parameters:
            name (str): The name of the attribute
            value (int): The value to be validated

        """

        if not isinstance(value, int):
            raise TypeError(f"<name> must be an integer")
        if value <= 0:
            raise ValueError(f"<name> must be greater then 0")
