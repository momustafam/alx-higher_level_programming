#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":
    obj =Rectangle.create(**{ 'width': 2, 'height': 3, 'x': 12, 'y': 1 })
    print(obj)
