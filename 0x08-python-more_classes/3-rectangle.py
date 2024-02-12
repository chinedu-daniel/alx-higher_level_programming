#!/usr/bin/python3

""" python task """

class Rectangle:

    """

    class that defines a rectangle

    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):

        """ 

        width property 

        """

        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an interger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """ 

        height property

        """

        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """ 

        public instaance tat returns the area of a rectangle 

        """

        return ((self.__width) * (self.__height))

    def perimeter(self):

        """ 

        public instance that returns the perimeter of a rectangle 

        """

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * (self.__width) + (self.__height)))

    def __str__(self):

        """ 

        should print rectangle with the character 

        """

        if self.__width == 0 or self.__height == 0:
            return ""
        return ('\n'.join(['#' * self.__width] * self.__height))
