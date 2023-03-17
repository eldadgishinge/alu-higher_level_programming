#!/usr/bin/python3

"""First rectangle"""


class Rectangle:
    """First rectangle"""
    
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object with the given width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retrieve the value of the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the value of the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the value of the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the value of the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle using '#' characters"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """Returns a string representation of the rectangle that can be used to recreate the object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
