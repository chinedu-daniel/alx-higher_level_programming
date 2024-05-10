#!/usr/bin/python3
"""
Python script that takes in a URL

sends a request to the URL

displays the value of the variable in the response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
    else:
        print("X-Request-Id not found in the response header.")
