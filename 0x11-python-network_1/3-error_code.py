#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
    - You have to manage urllib.error.HTTPError exceptions and print:
      Error code: followed by the HTTP status code
    - You must use the packages urllib and sys
    - You are not allowed to import other packages than urllib and sys
    - You don’t need to check arguments passed to the script (number or type)
    - You must use the with statement
"""


import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as r:
            response = r.read().decode('utf-8')
            print(response)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
    except urllib.error.urlerror as e:
        print('Error code: ', e.code)
