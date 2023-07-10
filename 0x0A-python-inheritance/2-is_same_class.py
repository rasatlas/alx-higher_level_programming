#!/usr/bin/python3
"""A function that returns True if the object is exactly an instance
of the specified class; otherwise False."""


def is_same_class(obj, a_class):
    """Check if obj is instance of a_class."""

    if not isinstance(obj, a_class):
        return False
    return True
