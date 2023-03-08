#!/usr/bin/python3
def max_integer(my_list=[]):
    z = len(my_list)
    if len(my_list) == 0:
        return
    my_list.sort()
    return (my_list.pop())
