#!/usr/bin/python3
"""Yes"""


def inherits_from(obj, a_class):
    """Yes"""
    if not type(obj) == a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
