#!/usr/bin/python3
def remove_char_at(str, n):
    z = 0
    rep = ""
    for char in str:
        if z != n:
            rep = rep + char
        z = z + 1
    return (rep)
