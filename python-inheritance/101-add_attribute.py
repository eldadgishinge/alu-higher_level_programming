#!/usr/bin/python3
"""Yes"""


def add_attribute(obj, name, value):
    """Yes"""
    if hasattr(obj, '__dict__'):
        obj.__setattr__(name, value)

    elif (hasattr(type(obj), '__slots__') and name in type(obj).__slots__):
        obj.__setattr__(name, value)

    else:
        raise TypeError("can't add new attribute")
