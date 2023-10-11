#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    max_key, max_ = None, float("-inf")
    for key in a_dictionary:
        if a_dictionary[key] > max_:
            max_key = key
            max_ = a_dictionary[key]
    return max_key
