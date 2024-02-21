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
    if not isinstance(filename, str) or not isinstance(text, str):
        raise TypeError("Both filename and text must be strings")

    with open(filename, 'w', encoding='UTF-8') as file:
        file.write(text)

        return len(text)
