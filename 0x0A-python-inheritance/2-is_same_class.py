#!/usr/bin/python3

""" python3 file """


def is_same_class(obj, a_class):

    """

    Check if the given object belongs to the specified class or any subclass

    Parameters:
        obj: object
            The object to be checked.
        a_class: typr
            The class or type to compare against.

    Returns:
        bool:
            True if the object is an instance of class or any subclass,

    """

    return type(obj) is a_class
