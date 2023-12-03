#!/usr/bin/python3
"""
A Python script that takes 2 arguments in order to solve this challenge.
    - The first argument will be the repository name
    - The second argument will be the owner name
    - You must use the packages requests and sys
    - You are not allowed to import packages other than requests and sys
    - You don’t need to check arguments passed to the script (number or type)
"""


import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = requests.get(url)
    json_data = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(json_data[i].get("sha"),
                  json_data[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
