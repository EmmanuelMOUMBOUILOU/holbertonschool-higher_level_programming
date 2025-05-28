#!/usr/bin/python3
"""
6-base_geometry module

Defines a class BaseGeometry with a method that raises an Exception.
"""


class BaseGeometry:
    """BaseGeometry class with unimplemented area method."""

    def area(self):
        """Raise an exception indicating that area is not implemented."""
        raise Exception("area() is not implemented")
