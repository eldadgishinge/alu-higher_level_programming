#!/usr/bin/python3
"""size must be an integer"""


class Square:
    """size must be an integer"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
