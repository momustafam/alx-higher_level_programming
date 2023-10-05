#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


def calculator():
    '''
    calculates basic mathematical operations (+ , -, *, /)

    Args: NULL

    Returns: NULL
    '''
    n_args = len(argv)

    # handle invalid number of arguments
    if n_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operand1 = int(argv[1])
    operand2 = int(argv[3])
    operator = argv[2]

    # handle unavailable operator
    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    # calculate the requested operation
    if operator == '+':
        print(f"{operand1} + {operand2} = {add(operand1, operand2)}")
    elif operator == '-':
        print(f"{operand1} - {operand2} = {sub(operand1, operand2)}")
    elif operator == '*':
        print(f"{operand1} * {operand2} = {mul(operand1, operand2)}")
    else:
        print(f"{operand1} / {operand2} = {div(operand1, operand2)}")


if __name__ == "__main__":
    calculator()
