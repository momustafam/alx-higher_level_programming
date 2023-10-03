#!/usr/bin/python3
def uppercase(str):
    for char in str:
        asc_code = ord(char)
        if 97 <= asc_code < 123:
            print("{:s}".format(chr(asc_code - 32)), end="")
        else:
            print(char, end="")
    print()
