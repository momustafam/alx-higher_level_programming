#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ''' prints a dictionar by ordered keys '''
    ordered_dict = sorted(a_dictionary.items())
    for key, value in ordered_dict:
        print(f"{key}: {value}")
