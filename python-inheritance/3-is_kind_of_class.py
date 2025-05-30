#!/usr/bin/python3
"""
3-is_kind_of_class module

This module defines a function that checks if an object
is an instance of a class or a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of or inherits from a_class,
      else False."""
    return isinstance(obj, a_class)
