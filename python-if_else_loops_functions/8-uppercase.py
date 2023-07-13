#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        result += "{}". format(chr(ord(c) & ~32))
        print(result)
