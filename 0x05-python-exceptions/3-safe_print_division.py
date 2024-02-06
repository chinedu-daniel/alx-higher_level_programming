#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except (ValueError, TypeError):
        print("Error: Please provide vaid numerical inputs.")
    finally:
        print("{:d} / {:d} = {}".format(a, b, result), end="")
    return result
