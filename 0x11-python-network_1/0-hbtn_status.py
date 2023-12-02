#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    """
    A Python script that fetches https://alx-intranet.hbtn.io/status
    """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        body = r.read().decode('utf-8')
        print(body)
