#!/usr/bin/python3
""" python3 task """

class Rectangle:

    """

    class that defines a rectangle

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        
        """ width property """

        return (self.__width)

    @width.setter
    def width(self, value):
        if not isintance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """ height property """

        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """ public instance that returns the area of a rectangle """
        return (self.__width * self.__height)

    def perimeter(self):

        """ public instance that returns the perimeter of a rectangle """

        if self.__width ==  0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):

        """ print the rectangle with the character """

        if self.__width == 0 or self.__height == 0:
            return ""
        return ('\n'.join([str(self.print_symbol) * self.__width] * self.__height))

    def __repr__(self):
        """ return a string representation of the rectangle """

        return (f"Rectanle({self.__width}, {self.__height})")

    def __del__(self):

        """ prints the message with an instance of delete """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        """ returns the biggest rectangle based on area """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 + rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return (rect_1)
        else:
            return (rect_2)

        @classmethod
        def square(cls, size=0):

            """ returns a new rectangle instance """

            return (cls(size, size))
