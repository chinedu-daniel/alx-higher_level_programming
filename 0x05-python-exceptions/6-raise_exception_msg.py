#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        raise NameError("Hi There")
    except NameError:
        print("An exception flew by!")
        raise
