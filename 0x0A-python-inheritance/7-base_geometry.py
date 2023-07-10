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

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
