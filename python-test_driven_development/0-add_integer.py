#!/usr/bin/python3
"""
This module provides a function to add two integers.
The function ensures input types and performs integer conversion if needed.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats casted to integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float, default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
