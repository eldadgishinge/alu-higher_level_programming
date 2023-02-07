#!/usr/bin/python3
for i in range (0, 100):
    if i < 10:
        print("0{}".format(int(i)), end=", ")
    else:
        print("{}".format(int(i)), end=", ")
