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
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the widht of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the width of the rectanlge."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of a rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates perimeter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """Prints rectangle with the character #
        if height or width is 0 print an empty string.
        """
        if self.__height == 0 or self.__width == 0:
            return ("")
        else:
            rect = []
            for h in range(self.__height):
                for w in range(self.__width):
                    rect.append("#")
                if h != (self.__height - 1):
                    rect.append("\n")
            return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
