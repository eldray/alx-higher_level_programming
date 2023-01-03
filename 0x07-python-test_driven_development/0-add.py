#!/usr/bin/python3
'''
This is module adds two integers
'''


def add_integer(a, b):

    """Add two integers.
    Keyword arguments:
    a -- first integer
    b -- second integer
    """

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    c = a + b
    return c
