#!/usr/bin/python3
"""
Defines the rectangle class
"""

from base import Base


class Rectangle(Base):
    """
    rectangle Base class

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            return self.x

        @x.setter
        def x(self, value):
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            elif value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            elif value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            return self.width * self.height

        def display(self):
            for _ in range(self.y):
                print()
            for _ in range(self.height):
                print(" " * self.x + "#" * self.width)

        def __str__(self):
            return f"[Rectangle]({self.id}) {self.x}/{self.y} -
            {self.width}/{self.height}"

        def update(self, *args):
            if args:
                self.id = args[0] if len(args) >= 1 else self.id
                self.width = args[1] if len(args) >= 2 else self.width
                self.height = args[2] if len(args) >= 3 else self.height
                self.x = args[3] if len(args) >= 4 else self.x
                self.y = args[4] if len(args) >= 5 else self.y
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)

        def to_dictionary(self):
            return {
                    'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y
                    }
