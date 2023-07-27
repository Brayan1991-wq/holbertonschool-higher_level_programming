#!/usr/bin/python3
"""definition of a class"""


class Rectangle:
    """Represent of a rectangle"""

    def __init__(self, width=0, height=0):
        """constructor de la clase para inicializar los atributos"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter para obtener el ancho del rectangulo"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter para establecer el ancho del rectangulo"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter para obtener la altura del rectangulo"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter para establecer la altura del rectangulo"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
