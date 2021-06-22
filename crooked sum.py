# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file."""
import math

number_string = input()

my_str = ""

for char in number_string:
    if char.isdigit():       
        my_str += char
            
def sum_of_digits(any_num):
    if abs(any_num) <= 9:
        return any_num
    
    else:
        last = abs(any_num) % 10
        remainder = math.floor(abs(any_num) // 10)
        return sum_of_digits(last + sum_of_digits(remainder))
    
print(sum_of_digits(int(my_str)))

    





            
                
                


        


