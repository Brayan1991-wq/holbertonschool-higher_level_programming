#!/usr/bin/python3
"""square class creation"""


class Square:
    """represent a square"""
    def __init__(self, size=0):
        """initialize a square with value"""

        """checks if size is an integer otherwise throws an exception"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
