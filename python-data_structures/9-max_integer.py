#!/usr/bin/python3
def max_integer(my_list=[]):
    go = 0
    for i in range(len(my_list)):
        if my_list[i] > go:
            go = my_list[i]
        elif range(len(my_list)) == "":
            return my_list
    return go
