#!/usr/bin/python3
"""
    a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    data = requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
