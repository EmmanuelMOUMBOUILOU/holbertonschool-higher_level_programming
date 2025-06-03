#!/usr/bin/python3
"""
This module provides a function that returns
the JSON representation of an object.
"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of a Python object as a string."""
    return json.dumps(my_obj)
