#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = (number % 10) if number > 0 else (abs(number) % 10) * -1 
const_str = f"Last digit of {number:d} is {ldigit:d} and is "
if ldigit > 5:
    print(const_str + "greater than 5")
elif ldigit == 0:
    print(const_str + "0")
else:
    print(const_str + "less than 6 and not 0")
