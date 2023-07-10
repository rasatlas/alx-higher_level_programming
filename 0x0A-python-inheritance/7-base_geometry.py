#!/usr/bin/python3
"""Defines class BaseGeometry."""


class BaseGeometry():
    """Represents base geometry."""

    def area(self):
        """Implements method area that raise exception with a specific message.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value of value.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
