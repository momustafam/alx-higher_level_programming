#!/usr/bin/python3
"""Square module."""


class Square:
    """An incomplete class."""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiate a Square class with size equal to given size."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the value of the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Update the value of the size attribute."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the value of the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Update the value of the position attribute."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the square of the size attribute."""
        return self.__size**2

    def my_print(self):
        """Print in stdout the square with the character '#'"""
        if not self.size:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" "*self.position[0], end="")
            print("#"*self.size)
