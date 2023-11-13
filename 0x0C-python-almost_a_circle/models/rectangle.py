#!/usr/bin/python3
'''
        The `Rectangle` Module.

        Classes:
            - Rectangle
'''

from models.base import Base


class Rectangle(Base):
    '''A Rectangle Class that inherits from Base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instantiate an object of Rectangle class.'''

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        '''Return string representation of the class.'''

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

    def area(self):
        '''Calculate the area of the rectangle.'''

        return self.width * self.height

    def display(self):
        '''Display the rectanlge shape using `#` character.'''
        print("\n"*self.y, end='')
        print((" "*self.x + "#"*self.width + '\n') * self.height, end='')

    def update(self, *args, **kwargs):
        '''Update the rectangle object attributes.'''

        if args and len(args) > 0:
            for i in range(len(args)):
                arg = args[i]

                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        '''Return all rectangle attributes in a dictionary.'''

        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['width'] = self.width
        rect_dict['height'] = self.height
        rect_dict['x'] = self.x
        rect_dict['y'] = self.y

        return rect_dict

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
