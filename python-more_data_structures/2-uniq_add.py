#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = set(my_list)
    my_list = list((my_list))
    add = 0
    for i in range(0, len(my_list)):
        add = add + my_list[i]
    return add
