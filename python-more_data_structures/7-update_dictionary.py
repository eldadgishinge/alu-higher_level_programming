#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key, value in a_dictionary.items():
        if key in a_dictionary.keys():
            a_dictionary[key] = value
        if key not in a_dictionary.keys():
            a_dictionary[key] = value
    return a_dictionaryi
