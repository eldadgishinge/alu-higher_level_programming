#!/usr/bin/python3
"""count"""


def write_file(filename="", text=""):
    """count"""
    with open(filename, encoding="utf-8") as f:
        count = f.write(text)
    return count
