#!/usr/bin/python3
"""A function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is of instance of a_class."""

    if not isinstance(obj, a_class):
        return False
    return True
