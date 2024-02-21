#!/usr/bin/python3
""" a python file """


def lookup(obj):
    """

    Returns a list of available attributes and methods of an object.

    Parameters:
    - obj: Any object: the object to look up attributes and methods for.

    Returns:
    - list: A list containing the names of attributee and methods of the object

    """

    return [attribute for attribute in dir(obj)]
