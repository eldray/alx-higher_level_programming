#!/usr/bin/python3


class Square:
    """Represents a square
    Attributes:
        __size (int): size of the sides of a square
    """

    def __init__(self, size=0):
        '''init method of class Square
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size**2
