#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dictionary = dict(a_dictionary.items())
    for key in new_dictionary:
        if new_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
