# -*- coding: utf-8 -*-
"""
Calculate the sum of balanced numbers

Balanced 3-digit numbers are those for which 1st plus last digit equal the middle digit (e.g. 242, 121, etc.).
The numbers are read as user input, one at a time. The sum calculation continues until a non-balanced number is given.

"""
import math

def is_balanced(any_number):
    last = any_number % 10
    remainder = math.floor(any_number // 10)
    middle = remainder % 10
    first = math.floor(remainder // 10)
    if first + last == middle:
        return True
    else:
        return False
    
my_sum = 0

while True:
    new_num = int(input())

    if is_balanced(new_num):
        my_sum += new_num
    else:
        break
print(my_sum)
