#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.sort()
    my_list.reverse()
    i = 0
    for my_list[i] in my_list:
        print(my_list[i])
