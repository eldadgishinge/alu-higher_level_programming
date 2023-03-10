#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    all = 0
    down = 0
    for x, y in my_list:
        all = all + x*y
        down = down + y
    return all/down
