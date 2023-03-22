#!/usr/bin/python3
"""
Module 10-square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Yess"""
    def __init__(self, size):

        self.__size = size
        super().__init__(size, size)
        super().integer_validator("size", size)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
