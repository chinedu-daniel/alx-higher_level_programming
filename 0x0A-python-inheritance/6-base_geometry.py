#!/usr/bin/python3

""" python3 file """

class BaseGeometry:
    """
    Base class for geometric shapes

    This class provides common functionality and attributes for geometric shapes
    Subclasses can inherit from this class to implement specific geometric shapes

    """

    def area(self):
        
        """

        Calculate the area of the geometric shape

        Raises:
            Exception: indicates that the method is not implemented in the subclass

        """

        raise Exception("area() is not implemented")
