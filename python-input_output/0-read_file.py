#!/usr/bin/python3
"""
This module provides a function to read a UTF-8 text file
and print its content to standard output.
"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
