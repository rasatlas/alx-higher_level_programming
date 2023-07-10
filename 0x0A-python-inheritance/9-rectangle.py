#!/usr/bin/python3
"""Defines Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent Rectangle inheritting BaseGeometry."""

    def __init__(self, width, height):
        """constructor

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Implements area method."""

        return self.__width * self.__height

    def __str__(self):
        """Return the print() and stry() representation of a Rectangle."""
        return ("[" + str(self.__class__.__name__) "]"
                + str(self.__width) + "/" + str(self.__height))
