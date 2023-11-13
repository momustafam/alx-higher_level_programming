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
        '''Instantiate an object of the Base class.'''

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

        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            temp = []
            for obj in list_objs:
                temp.append(obj.to_dictionary())
            f.write(cls.to_json_string(temp))

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
            pass
        finally:
            return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Write a json string representation `list_obj` to a csv file.'''
        with open(f"{cls.__name__}.csv", "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            data = []
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
        '''
            Open a window using turtle and draw all rectangles and squares.
        '''

        screen = turtle.Screen()
        screen.bgcolor("black")
        pen = turtle.Turtle()
        pen.pencolor("yellow")
        pen.fillcolor("red")

        for shape in list_rectangles + list_squares:
            pen.penup()
            pen.goto(shape.x, shape.y)
            pen.pendown()
            for i in range(2):
                pen.forwardi(shape.width)
                pen.left(90)
                pen.forward(shape.height)
                pen.left(90)

        turtle.done()
