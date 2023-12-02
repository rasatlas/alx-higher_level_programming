#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
    - You must use the package urllib
    - You are not allowed to import any packages other than urllib
    - The body of the response must be formated (Refer README.md)
    - You must use a with statement
"""


import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        body = r.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
