#!/usr/bin/python3
"""A class rectangle that defines a rectangle."""


class Rectangle:
    """Define a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__width = width
        self.__height = height

    def width(self):
        """Get the widht of the rectangle."""
        return self.__width

    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    def height(self, value):
        """Set the width of the rectanlge."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
