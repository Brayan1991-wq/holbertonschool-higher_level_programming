#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nueva_lista = []
    for elemento in my_list:
        if elemento == search:
            nueva_lista.append(replace)
        else:
            nueva_lista.append(elemento)
    return nueva_lista
