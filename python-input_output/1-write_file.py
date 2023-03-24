#!/usr/bin/python3
"""count"""


def write_file(filename="", text=""):
    """Yes"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
