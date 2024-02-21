#!/usr/bin/python3

""" python3 file """


class BaseGeometry:
    """
    Base class for geometric shapes

    This class provides common functionality and attributes
    Subclasses can inherit from this class to implement specific

    """

    def area(self):

        """

        Calculate the area of the geometric shape

        Raises:
            Exception: indicates that the method is not implemented

        """

        raise Exception("area() is not implemented")
