#!/usr/bin/python3
"""A function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.
"""


def def inherits_from(obj, a_class):
    """Checks if obj is inherited from a_class."""

    if not issubclass(obj, a_class):
        return False
    return True
