# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:25:34 2021

@author: Teodora
"""
import math

client_budget = int(input())
standard_price = int(input())
discount = int(input())
price_threshold = int(input())

def calculate_discounted_price(price, my_discount): 
    return price - my_discount 
    
if client_budget < standard_price:
    print(0, client_budget)
else:
    counter = 1
    sum_spent = standard_price

    while sum_spent < client_budget:
        new_price = calculate_discounted_price(standard_price, discount * counter)
 #       print("The new price is: ", new_price)
        if new_price >= price_threshold and new_price <= client_budget - sum_spent:
            sum_spent += new_price
            counter += 1
        else:
            break
#    print("Counter after loop ", counter)
    additional_pairs = math.floor((client_budget - sum_spent) // price_threshold)   
#    print("Additional pairs: ", additional_pairs)
    counter += additional_pairs

    if counter >= 10:
        counter += 1
    sum_spent += additional_pairs * price_threshold
    print(counter, client_budget - sum_spent)    