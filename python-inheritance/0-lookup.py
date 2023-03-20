#!/usr/bin/python3
    """
    Returns a list of available attributes and methods of an object.
    """


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    # Get the list of attributes and methods of the object
    attrs = dir(obj)
    filtered_attrs = []
    for attr in attrs:
        if attr.startswith(''):
            filtered_attrs.append(attr)

    # Filter out any private or special attributes/methods
    #filtered_attrs = [attr for attr in attrs if not attr.startswith('__')]

    # Return the filtered list of attributes/methods
    return filtered_attrs
