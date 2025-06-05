#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a dictionary and save it to a JSON file.

    Args:
        data (dict): The data to serialize.
        filename (str): The file to save the JSON data to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file.

    Args:
        filename (str): The JSON file to read from.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
