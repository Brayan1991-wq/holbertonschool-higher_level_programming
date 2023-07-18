#!/usr/bin/python3
def print_matrix_integer(matriz=[[]]):
    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            print("{:d}".format(elemento), end=" ")
            if (j + 1) % 3 == 0:
                print()
