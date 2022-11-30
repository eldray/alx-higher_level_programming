#!/usr/bin/python3

"""Print the numbers from 1 to 100 separated by a space.
   For multiples of three, print Fizz instead of the number
   For multiples of five, print Buzz instead of the number.
   For multiples of three and five, print FizzBuzz instead of the number.
"""

def fizzbuzz():
   [print("FizzBuzz", end=" ") if not (x % 3) and not (x % 5)
    else print("Fizz", end=" ") if not (x % 3)
    else print("Buzz", end=" ") if not (x % 5)
    else print(x, end=" ") for x in range(1, 101)]
