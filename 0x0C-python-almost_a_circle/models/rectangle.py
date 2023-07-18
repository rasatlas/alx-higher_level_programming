#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int) : The x-coordinate of the new Rectangle.
            y (int): The y-coordinate of the new Rectangle.
            id (int): The id of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height is <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y is < 0.
        """

        self.validator(self, "width", width)
        self.__width = width
        self.validator(self, "height", height)
        self.__height = height
        self.validator(self, "x", x)
        self.__x = x
        self.validator(self, "y", y)
        self.__y = y
        super().__init__(id)

    def validator(self, key, value):
        """
        Validates value passed.

        Args:
            key (str): The name of the attribute being validated.
            value: The value to be validated.

        Raises:
            TypeError: If value is not an int.
            ValueError: If the value is <= 0 for 'width' or 'height',
            or < 0 for 'x' or 'y'.
        """
        if value is None or type(value) is not int:
            raise TypeError(name + " must be an integer")
        if (key == "width" or key == "height") and value <= 0:
            raise ValueError(key + " must be > 0")
        if (key == "y" or key == "x") and value < 0:
            raise ValueError(key + " must be >= 0")

    @property
    def width(self):
        """width getter."""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter."""
        validator(self, "width", width)
        self.__width = width

    @property
    def height(self):
        """height getter."""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter."""
        validator(self, "height", height)
        self.__height = height

    @property
    def x(self):
        """x-coordinate getter."""
        return self.__x

    @x.setter
    def x(self, x):
        """x-coordinate setter."""
        validator(self, "x", x)
        self.__x = x

    @property
    def y(self):
        """y-coordinate getter."""
        return self.__y

    @y.setter
    def y(self, y):
        """y-coordinate setter."""
        validator(self, "y", y)
        self.__y == y

    def area(self):
        """Calculates area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Override the '__str__' method."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args is not None and len(args) > 0:
            keys = ['id', 'width', 'height', 'x', 'y']
            for key, value in zip(keys, args):
                setattr(self, key, value)
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
