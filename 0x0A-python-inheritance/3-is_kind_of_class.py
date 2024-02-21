#!/usr/bin/python3

"""
python3 file

"""


def is_kind_of_class(obj, a_class):

    """

    Check if the given object is an instance of, or an instance of a class
    that inherited from, the specified class

    Parameters:
        obj: object
            The object to be checked.
        a_class: type
            The class or type to compare against

    Return:
        bool:
            True if the object is an instance of the specified class or any
            subclass, False otherwise

    """

    return isinstance(obj, a_class)
