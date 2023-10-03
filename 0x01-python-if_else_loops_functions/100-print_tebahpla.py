#!/usr/bin/python3
for i in range(90, 64, -1):
    temp = i
    if temp % 2 == 0:
        temp += 32
    print("{:s}".format(chr(temp)), end="")
