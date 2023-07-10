#!/usr/bin/python3
"""Class myList that inherits from list."""


class MyList(list):
    """Implements sorted printing for passed list object."""

    def print_sorted(self):
        """Instance method that prints the list in sorted ascendingly."""

        print(sorted(self))
