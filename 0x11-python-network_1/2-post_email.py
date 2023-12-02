#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
    - The email must be sent in the email variable
    - You must use the packages urllib and sys
    - You are not allowed to import packages other than urllib and sys
    - You don’t need to check arguments passed to the script (number or type)
    - You must use the with statement
"""


import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data_to_encode = urllib.parse.urlencode({'email': email})
    encoded_data = data_to_encode.encode('utf-8')
    request = urllib.request.Request(url, data=encoded_data, method='POST')
    with urllib.request.urlopen(req) as r:
        response = r.read().decode('utf-8')
        print(response)
