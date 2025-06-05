#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file using pickle.

        Args:
            filename (str): The name of the file to save the object to.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            pass  # Silently ignore errors as per instructions

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file using pickle.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject | None: The deserialized object,
              or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
