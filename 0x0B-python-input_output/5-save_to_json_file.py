#!/usr/bin/python3
'''
    The 5-save_to_json_file module
'''
import json


def save_to_json_file(my_obj, filename):
    '''Write an object to a text file, using a JSON representation.'''

    with open(filename, encoding='utf-8') as f:
        json.dump(my_obj, f)
