#!/usr/bin/python3
""" Python3 file """


def append_write(filename="", text=""):
    """

    Appends the provided text to the UTF-8 text file

    If the file does not exist, it will be created

    Args:
        filename(str, optional): The name of the file that appends the text
        text(str, optional): The text that appends to file

    Return:
        int: The number of characters appended to the file

    """

    if not isinstance(filename, str) or not isinstance(text, str):
        raise TypeError("Both filename and text must be strings")

    with open(filename, 'a', encoding='UTF-8') as file:
        file.append(text)

        return len(text)
