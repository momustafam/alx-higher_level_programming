#!/usr/bin/python3
def print_last_digit(number):
    ldigit = (number % 10) if number >= 0 else (abs(number) % 10) * -1
    print(ldigit)
    return ldigit
