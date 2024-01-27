#!/usr/bin/python3
"""
    a Python script that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable
    found in the header of the response.
"""
import urllib.request
from sys import argv

url = argv[1]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as resp:
    print(dict(resp.headers).get("X-Request-Id"))
