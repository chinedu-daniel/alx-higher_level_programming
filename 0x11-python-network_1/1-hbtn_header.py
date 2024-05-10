#!/usr/bin/python3
"""
Display the value found in the header of the response
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

