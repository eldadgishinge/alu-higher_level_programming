#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    new_list = []
    for i in my_list:
        if idx < 0 and idx >= range(0, len(my_list)):
            return my_list
        else:
            del my_list[idx]
        return my_list
