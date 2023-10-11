#!/usr/bin/python3
def best_score(a_dictionary):
    ''' returns a key with the biggest integer value '''
    if a_dictionary is None:
        return None

    max_int = max(a_dictionary.values())
    for key in a_dictionary:
        if a_dictionary[key] == max_int:
            return key
