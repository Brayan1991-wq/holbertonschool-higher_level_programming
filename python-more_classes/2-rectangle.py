#!/usr/bin/python3
"""definicion de una clase"""


class Rectangle:
    """representacion de un  rectangulo"""

    def __init__(self, width=0, height=0):
        """constructor para inicializar los atributos"""
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
        return self.__width

    @height.setter
    def height(self, value):
        """Setter para establecer la altura del rectangulo"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """devuelvee el area del rectangulo"""
        return (self.__width * self.__height)

    def perimeter(self):
        """devuelve el perimetro del rectangulo"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
