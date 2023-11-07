#!/usr/bin/python3
'''The 7-add_item module'''
import json
from sys import argv

save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

def add_item():
    f_name = "add_item.json"

    try:
        data = load("add_item.json")
    except Exception:
        data = []

    if len(argv) > 1:
        data.extend(argv[1:])
        save(data, "add_item.json")

add_item()
