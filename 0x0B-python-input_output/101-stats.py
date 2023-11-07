#!/usr/bin/python3
from sys import stdin

status_code = {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
        }
i = total_size = 0


def print_stats():
    """print the statistic"""
    print(f"File size: {total_size}")
    for key, value in sorted(status_code.items()):
        if value > 0:
            print("{:s}: {:d}".format(key, value))


try:
    for line in stdin:
        lines = line.split()
        if len(lines) >= 2:
            stat = lines[-2]
            total_size += int(lines[-1])
            if stat in status_code:
                status_code[stat] += 1
        i += 1

        if i % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt as e:
    print_stats()
