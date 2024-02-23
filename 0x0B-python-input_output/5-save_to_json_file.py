#!/usr/bin/python3
"""pythone file"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save a python object to a JSON file

    Parameters:
    - my_obj (obj): THe python object to be saved
    - filename (str): The name of the JSON file to save to

    Return:
    - None

    """

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
