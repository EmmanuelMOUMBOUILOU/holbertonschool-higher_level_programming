#!/usr/bin/python3
"""
Script that adds command-line arguments to a list
and saves them to a JSON file.
"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing data if the file exists, otherwise start with an empty list
if os.path.exists(filename):
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []
else:
    items = []

# Add command-line arguments (skipping the script name itself)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
