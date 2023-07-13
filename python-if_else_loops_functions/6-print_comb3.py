#!/usr/bin/python3
for com1 in range(0, 10):
    for com2 in range(com1 + 1, 10):
        if com1 == 8 and com2 == 9:
            print("{}{}".format(com1, com2))
        else:
            print("{}{}".format(com1, com2), end=", ")
