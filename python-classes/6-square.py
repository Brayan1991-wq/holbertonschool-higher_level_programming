#!/usr/bin/python3
"""Define a class Square."""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """initializes the object's attributes"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter para obtener el tamaño del cuadrado.

        Retorna:
            int: Tamaño del cuadrado.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter para establecer el tamaño del cuadrado.

        Parámetros:
            value (int): Tamaño del cuadrado.

        Lanza:
            TypeError: Si el valor no es un número entero.
            ValueError: Si el valor es negativo.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter para obtener la posición del cuadrado en la impresión.

        Retorna:
            tuple: Posición del cuadrado en la impresión (x, y).
        """
        return self.__podition

    @position.setter
    """
        Setter para establecer la posición del cuadrado en la impresión.

        Parámetros:
            value (tuple): Posición del cuadrado en la impresión (x, y).

        Lanza:
            TypeError: Si el valor no es una tupla de 2 enteros positivos.
        """
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calcula el área del cuadrado.

        Retorna:
            int: Área del cuadrado (lado * lado).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Imprime el cuadrado en la salida estándar (stdout).

        Si el tamaño es 0, imprime una línea vacía.
        La posición se usa para
        agregar espacios a la izquierda cuando la posición[1] > 0.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
