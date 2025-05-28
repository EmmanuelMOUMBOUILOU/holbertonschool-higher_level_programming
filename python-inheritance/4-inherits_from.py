#!/usr/bin/python3
"""
4-inherits_from module

Defines a function that checks if an object
 is a subclass instance of a given class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass
      of a_class (not a_class itself).
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
