#!/usr/bin/python3
'''
    The `Base` module

    Classes:
        Base 
'''

import json
import csv
import turtle

class Base:
    '''
    A class that manages id attribute in all your child classes
    and to avoid duplicating the same code.

    Variables:
        __nb_objects (int):

    Functions:
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Instanitiate an object of the Base class.'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Return the json string representation of `list_dictionaries`.'''

        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        '''Return a json string representation.'''

        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        '''Write the json string representation `list_objs` to a file.'''

        with open(f"{cls.__name__}.json", "w") as f:
            temp = []
            for obj in list_objs:
                temp.append(obj.to_dictionary())
            f.write(Base.to_json_string(temp))

    @classmethod
    def create(cls, **dictionary):
        '''Return an instance with all attributes already set.'''

        dummy = cls(1, 1)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        '''Return a list of instances.'''

        objs = []
        try:
            with open(f"{cls.__name__}.json") as f:
                objs_attrs = cls.from_json_string(f.read())
                for obj_attr in objs_attrs:
                    obj = cls.create(**obj_attr)
                    objs.append(obj)
        except FileNotFoundError:
            print("not found")
        finally:
            return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Write a json string representation `list_obj` to a csv file.'''
        with open(f"{cls.__name__}.csv", "w") as f:
            writer = csv.writer(f)
            data = []
            if cls.__name__ == 'Rectangle':
                data.append(['id', 'width', 'height', 'x', 'y'])
            elif cls.__name__ == 'Square':
                data.append(['id', 'size', 'x', 'y'])
            for obj in list_objs:
                data.append(obj.to_dictionary().values())
            writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        '''Return a list of instances that read from a scv file.'''

        objs = []
        try:
            with open(f"{cls.__name__}.csv") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    row = list(map(int, row))
                    obj = cls(1, 1)
                    obj.update(*row)
                    objs.append(obj)
        except FileNotFoundError:
            pass
        finally:
            return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
