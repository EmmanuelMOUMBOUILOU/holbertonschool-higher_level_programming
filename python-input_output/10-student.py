#!/usr/bin/python3
"""Student class definition with selective JSON serialization."""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of a Student instance.

        If `attrs` is a list of strings, only return those attributes.
        Otherwise, return all attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
