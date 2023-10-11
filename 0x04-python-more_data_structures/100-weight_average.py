#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    temp = 0
    sum = 0

    for x, y in my_list:
        sum += x * y
        temp += y

    return sum / temp
