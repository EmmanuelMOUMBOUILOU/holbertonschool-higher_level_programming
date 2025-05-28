#!/usr/bin/python3
"""
1-my_list module

Defines a class MyList that inherits from list,
with a method to print the list sorted in ascending order.
"""


class MyList(list):
    """A subclass of list that includes a method to print the list sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order (without modifying it)."""
        print(sorted(self))
