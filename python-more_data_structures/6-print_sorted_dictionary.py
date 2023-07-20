#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Obtener las claves ordenadas alfabéticamente
    sorted_keys = sorted(a_dictionary.keys())
    # Imprimir los pares clave-valor
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
    # Ejemplo de uso
        if __name__ == "__main__":
            ejemplo_diccionario = {
                "z": 3,
                "a": 1,
                "d": 4,
                "b": 2
            }
            print_sorted_dictionary(ejemplo_diccionario)
