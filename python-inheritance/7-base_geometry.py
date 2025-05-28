#!/usr/bin/python3
"""
7-base_geometry module

Defines BaseGeometry class with area method and integer validation.
"""


class BaseGeometry:
    """BaseGeometry class with area and integer validation methods."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
