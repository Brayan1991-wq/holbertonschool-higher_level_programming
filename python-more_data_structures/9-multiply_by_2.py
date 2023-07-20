#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nuevo_diccionario = {}
    for key, value in a_dictionary.items():
        nuevo_diccionario[key] = value * 2
    return nuevo_diccionario
