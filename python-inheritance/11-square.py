#!/usr/bin/python3
"""
11-square module

Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the square description [Square] size/size."""
        return "[Square] {}/{}".format(self.__size, self.__size)
