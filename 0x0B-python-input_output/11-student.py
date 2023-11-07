#!/usr/bin/python3
"""Module that contains the solution for task 9."""


class Student:
    """Student class"""

    def __init__(self, firstname, lastname, age):
        """Constructor"""
        self.first_name = firstname
        self.last_name = lastname
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of student"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        dic = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                dic[key] = value
        return dic

    def reload_from_json(self, json):
        """replaces all attributes of the Student"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
