#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    roman_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    total = roman_nums[roman_string[0]]
    prev = roman_nums[roman_string[0]]
    length = len(roman_string)

    if length == 1:
        return prev

    for i in range(1, length):
        num = roman_nums[roman_string[i]]
        if num > prev:
            total += num - (prev * 2)
        else:
            total += num
        prev = num

    return total
