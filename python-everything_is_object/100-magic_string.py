#!/usr/bin/python3
def magic_string():
    """
    Returns a string "BestSchool" n times the number of the iteration, where n is the current iteration number.
    If called for the first time, initializes a counter attribute to keep track of the number of iterations.
    """
    if not hasattr(magic_string, 'counter'):
        magic_string.counter = 0
    magic_string.counter += 1
    return ', '.join(['BestSchool' for i in range(magic_string.counter)])
