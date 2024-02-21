#!/usr/bin/python3
""" python3 file """

import json


def to_json_string(my_obj):
    """

    Convert the given python object to a JSON string

    Args:
        my_obj: The python object to be converted to JSON

    Return:
        str: A JSON string representing the input python object

    """

    return (json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
