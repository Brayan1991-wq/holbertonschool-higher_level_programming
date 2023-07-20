#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = []
    for num in my_list:
        if num not in unique_integers and isinstance(num, int):
            unique_integers.append(num)
    return sum(unique_integers)
