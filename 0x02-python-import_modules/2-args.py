#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    arg_plural = "s" if num_args != 1 else ""

    print("Number of argument{}: {}".format(arg_plural, num_args), end="")
    print("{}".format(":" if num_args > 0 else "."))

    for i in range(1, num_args + 1):
        print("{:d}: {}".format(i, argv[i]))
