#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
    - You must use the package requests
    - You are not allow to import packages other than requests
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- Content: {}".format(response.text))
