#!/usr/bin/python3
"""First rectangle"""


class Rectangle:
    """First rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """width"""
        return self.__height

    @height.setter
    def height(self, value):
        """width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0:
            return 0
        elif self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height)*2
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            print("")
        str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str = str + "#"
            if i != self.__height -1:
                str = str + "\n"
        return str
