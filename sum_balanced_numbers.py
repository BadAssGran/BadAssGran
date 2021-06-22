# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:41:28 2021

@author: Teodora
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