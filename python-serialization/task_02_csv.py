#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts CSV data into JSON format and writes it to data.json

    Args:
        csv_filename (str): The path to the CSV file to be converted.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
