#!/usr/bin/python3


def max_integer(my_list=[]):
    go = 0
    for i in range(len(my_list)):
        if len(my_list) == 0:
            return "None"
        if my_list[i] > go:
            go = my_list[i]
    return go
