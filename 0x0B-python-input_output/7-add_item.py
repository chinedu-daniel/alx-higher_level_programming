#!/usr/bin/python3
""" python3 file """

import sys

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_to_list_and_save(args):
    try:
        items = load_from_json_file("add_item.json")

    except FileNotFoundError:
        items = []

    items.extend(args)

    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":

    args = sys.agv[1:]
    add_to_list_and_save(args)
