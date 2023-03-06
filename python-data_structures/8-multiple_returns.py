#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return "None"
    else:
        length = len(sentence)
        first = sentence[0:1]
        if first == "":
            first = None
        return length, first
