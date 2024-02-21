#!/usr/bin/python3

"""
python3 file

"""


def write_file(filename="", text=""):
    """

    Writes the provided text to a file

    Args:
        filename(str, optiona): The name of the file to be written
        text(str, optional): The text to be written to the file

    """

    with open(filename, 'w', encoding='UTF-8') as file:
        return file.tell()
