#!/usr/bin/python3
"""
     a Python script that takes 2 arguments in order to solve this challenge.
"""
from sys import argv
import requests


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    resp = requests.get(url)
    commits = resp.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
