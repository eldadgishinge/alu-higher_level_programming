#!/usr/bin/python3
"""Yes"""
import json


def save_to_json_file(my_obj, filename):
    """yes"""
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
