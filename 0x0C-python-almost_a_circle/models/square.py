#!/usr/bin/python3
'''
    The `Square` module
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        Square class.
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        '''Update the attributes of a square object.'''

        if args and len(args) > 0:
            for i in range(len(args)):
                arg = args[i]

                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                    self.height = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.width = value
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        squ_dict = {}
        squ_dict['id'] = self.id
        squ_dict['size'] = self.size
        squ_dict['x'] = self.x
        squ_dict['y'] = self.y

        return squ_dict

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
