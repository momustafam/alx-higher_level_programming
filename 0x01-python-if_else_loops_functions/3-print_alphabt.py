#!/usr/bin/python3
for alpha in range(97, 123):
    if alpha == ord('q') or alpha == ord('e'):
        continue
    print("{}".format(chr(alpha)), end="")
