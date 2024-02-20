#!/usr/bin/python3
"""
Python3 file

"""

class MyList(list):
    
    """

    A class that inherits from the built-in list class
    
    Public instance method:
    - print_sorted(self): Prints the list but sortedin ascending order


    """

    def print_sorted(self):

        """
        Prints the list sorted in ascending order

        """

        sorted_list = sorted(self)
        print(sorted_list)
