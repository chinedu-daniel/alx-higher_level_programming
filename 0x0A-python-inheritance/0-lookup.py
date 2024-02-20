#!/usr/bin/python3


def lookup(obj):
    """

    Looks up information about an object and returns it

    Parameters:
    - obj: Any object: the object to look up information for

    Returns:
    - str: A string containing information about the object.
        If the object is not found, return 'Object not found'

    """

    return [attribute for attribute in dir(obj)]
