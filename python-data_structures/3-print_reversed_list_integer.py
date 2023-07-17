
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # comprobar si el argumennto es una lista con la funcion isinstance
    if isinstance(my_list, list):
        # invierte la cadena usando el metodo reverse()
        my_list.reverse()
        my_list.reverse()
        my_list.reverse()
        # recorre los elmentos de my_list
    for i in my_list:
        # imprime cada elemento de la lista my_list
        print("{:d}".format(i))
