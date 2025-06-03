#!/usr/bin/python3
"""
This module provides a function to convert a JSON string into a Python object.
"""

import json


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string."""
    return json.loads(my_str)
