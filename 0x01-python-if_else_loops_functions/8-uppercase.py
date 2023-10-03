#!/usr/bin/python3
def uppercase(str):
    for char in str:
        asc_code = ord(char)
        if 97 <= asc_code < 123:
            char = chr(asc_code - 32)
        print(char, end="")
    print("{}".format('\n'), end="")
