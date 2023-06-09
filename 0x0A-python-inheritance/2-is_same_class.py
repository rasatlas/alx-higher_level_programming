#!/usr/bin/python3
"""A function that returns True if the object is exactly an instance
of the specified class; otherwise False."""


def is_same_class(obj, a_class):
    """Checks if obj is type of a_class."""

    if not (type(obj) == a_class):
        return False
    return True
