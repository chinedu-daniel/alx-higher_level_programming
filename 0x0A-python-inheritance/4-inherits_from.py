#!/usr/bin/python3

""" python3 files """

def inherits_from(obj, a_class):
    """

    Check if the object inherits from the specified class.

    Parameters:
        obj: object
            The object to be cheked
        a_class: type
            The class or type to check for inheritance

    Returns:
        bool:
            True if the object inherits from the specified class (or is an 
            instance of it), False otherwise

    """

    return any(a_class in cls.mro() for cls in type(obj).mro())

    
