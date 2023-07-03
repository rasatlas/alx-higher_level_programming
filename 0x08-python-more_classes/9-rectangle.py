#!/usr/bin/python3
"""A class rectangle that defines a rectangle."""


class Rectangle:
    """Define a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    def __del__(self):
        """Prints message for every deletion on instances."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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
                    rect.append(str(self.print_symbol))
                if h != (self.__height - 1):
                    rect.append("\n")
            return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigget rectangle based on area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size.

        Args:
            size (Int): The width and height of the new square
        """
        return (cls(size, size))
