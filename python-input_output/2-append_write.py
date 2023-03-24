#!/usr/bin/python3
"""yes"""


def append_write(filename="", text=""):
    """Yes"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text + text)
