#!/usr/bin/python3
""" python3 file """

def read_file(filename=""):
    """
    Reads the content of a file and returns it as a string

    Args:
        filename (str, optional): The name of the file to be read

    Returns:
        str: The content of the file as a string

    """
    
    with open("", "r", encoding="utf-8") as read_file:
        read_file.read()
