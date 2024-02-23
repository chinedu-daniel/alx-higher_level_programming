#!/usr/bin/python3
""" python3 file """

import json


def load_from_json_file(filename):
    """
    Load a python object from a JSON file

    Parameters:
    - filename (str): THhe name of the JSON file to load from

    Return:
    - obj: A python object representing the stored data in JSON file

    """

    with open(filename, 'r') as file:
        return json.load(file)
