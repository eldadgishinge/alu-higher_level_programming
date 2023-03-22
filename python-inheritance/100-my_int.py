#!/usr/bin/python3
"""Yes"""


class MyInt(int):
    """Yes"""
    def __eq__(self, other):
        return self.real != other

    def __ne__(self, other):
        return self.real == other
