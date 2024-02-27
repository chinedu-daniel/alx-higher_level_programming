#!/usr/bin/python3
"""
model for square

"""

from retangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square]({self.id}) {self.x}/{self.y} 
        - self.width"

    @property
    def width(self):
        return self.width
    
    @width.setter
    def width(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
            else:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                    elif key == 'size':
                        self.size = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value

    def to_dictionary(self):
        return {
                'id' = self.id,
                'size' = self.size,
                'x' = self.x,
                'y' = self.y
                }
