#!/usr/bin/python3
""" python3 file """

import json


def from_json_string(my_str):
    """
    Converts a JSON formatted string into a python object

    Parameters:
    - my_str (str): A JSON formatted string to be converted

    Return:
    - obj: A python object representing the data encoded in JSON

    Raises:
    - ValueError: If the input string is not valid JSON

    """

    return json.loads(my_str)
