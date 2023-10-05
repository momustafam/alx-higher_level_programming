#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n_args = len(argv)
    if (n_args == 1):
        print("0 argument.")
    elif (n_args == 2):
        print("1 arugment:")
        print(f"1: {argv[1]}")
    else:
        print(f"{n_args - 1} arguments")
        for i in range(1, n_args):
            print(f"{i}: {argv[i]}")
