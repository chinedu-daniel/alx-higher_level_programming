#!/usr/bin/python3
islower = __import__('7-islower').islower

print("{} is {}".format("lower" if islower("") else "upper"))
