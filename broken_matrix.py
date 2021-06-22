# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:51:51 2021

@author: Teodora
"""

seq = input()

seq_list = [int(x) for x in seq if x.isalnum()]
print(seq_list)

new_list = [seq_list[-1]] + seq_list + [seq_list[0]]
print(new_list)
result = ""


for i in range(1, len(new_list)-1):
    
    if new_list[i]==0:
        if new_list[i-1]==0 and new_list[i+1] == 1:
            result += str(0)
        elif new_list[i-1]==1 and new_list[i+1] == 0:
            result += str(0)
        elif new_list[i-1]==1 and new_list[i+1]==1:
            result += str(1)
            
    else:
        if new_list[i-1]==0 and new_list[i+1] == 0:
            result += str(0)
        elif new_list[i-1]==1 and new_list[i+1]==1:
            result += str(0)
        elif new_list[i-1]==0 and new_list[i+1] == 1:
            result += str(1)
        elif new_list[i-1]==1 and new_list[i+1] == 0:
            result += str(1)
        

       
print(result)

            
