#!/usr/bin/python3
"""
Module to use the GitHub API to display the user ID using Basic Authentication
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print("User ID:", user_data['id'])
    else:
        print("Failed to fetch user ID. Status code:", response.status_code)
