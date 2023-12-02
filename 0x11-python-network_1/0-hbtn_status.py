#!/usr/bin/python3
# A Python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request

if __name__ == "__main__":
    """
    A Python script that fetches https://alx-intranet.hbtn.io/status
    """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        body = r.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
