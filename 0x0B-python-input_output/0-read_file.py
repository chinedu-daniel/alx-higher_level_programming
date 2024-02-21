#!/usr/bin/python3
""" python3 file """


def read_file(filename=""):

    """

    Reads the content of a file and returns it as a string

    Args:
        filename (str, optional): The name of the file to be read

    """

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
