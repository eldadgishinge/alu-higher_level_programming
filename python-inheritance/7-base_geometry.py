#!/usr/bin/python3
"""Yess"""


class BaseGeometry:
    """Yes"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.__value  = value
        self.__name = name
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")

