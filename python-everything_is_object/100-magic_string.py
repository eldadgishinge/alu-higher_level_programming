#!/usr/bin/python3
def magic_string():
    if not hasattr(magic_string, 'counter'): magic_string.counter = 0
    magic_string.counter += 1; return ', '.join(['Holberton'*magic_string.counter])