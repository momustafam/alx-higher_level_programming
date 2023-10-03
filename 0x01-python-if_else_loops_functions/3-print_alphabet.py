#!/usr/bin/python3
for alpha in range(97, 123):
    if alpha == 'q' or alpha == 'e':
        continue
    print("{}".format(chr(alpha)), end="")
