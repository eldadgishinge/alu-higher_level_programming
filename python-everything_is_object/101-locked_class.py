#!/usr/bin/python3
"""magic_string"""

def magic_string():
    """magic_string"""
    if not hasattr(magic_string, 'counter'):
        magic_string.counter = 0
    magic_string.counter += 1
    return ', '.join(['BestSchool' for i in range(magic_string.counter)])
