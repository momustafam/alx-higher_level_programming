#!/usr/bin/python3
"""module for task 13"""


def append_after(filename="", search_string="", new_string=""):
    """
        inserts a line of text to a file,
        after each line containing a specific string.

        Args:
            filename (str): file path
            search_string (str): string to insert after
            new_string (str): string to insert
    """
    with open(file=filename, mode="r", encoding="utf-8") as f:
        lines = []
        while True:
            line = f.readline()
            if line == "":
                break
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(file=filename, mode="w", encoding="utf-8") as f:
        f.writelines(lines)
