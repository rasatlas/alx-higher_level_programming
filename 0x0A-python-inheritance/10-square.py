#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Defines Square."""


class Square(Rectangle):
    """Represents square."""

    def __init__(self, size):
        """constructor.
        Args:
            size (int) dimension of the square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
