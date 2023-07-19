#!/usr/bin/python3
def max_integer(my_list=[]):
    # Verificar si la lista está vacía
    if not my_list:
        return None
    # Inicializar la variable para almacenar el entero más grande
    max_value = my_list[0]
    # Iterar por la lista para encontrar el entero más grande
    for num in my_list:
        if num > max_value:
            max_value = num
            return max_value
