# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file."""

first_seq = input().strip().split(" ")
second_seq = input().strip().split(" ")
code_seqs = input().strip().split(", ")
    
# print(first_seq)
# print(second_seq)
# print(code_seqs)


index = 0

while index < len(code_seqs):
    
    code_list = [int(char) for char in code_seqs[index] if char.isalnum()]
    #print(code_list)
    
    if code_list[0] < code_list[-1]:
        
        new_seq_1 = first_seq[:code_list[0]] + second_seq[code_list[0]:code_list[1]+1] + first_seq[code_list[1]+1:]
        new_seq_2 = second_seq[:code_list[0]] + first_seq[code_list[0]:code_list[1]+1] + second_seq[code_list[1]+1:]
         
        first_seq = new_seq_1
        second_seq = new_seq_2
        index += 1
        
    elif code_list[0] > code_list[-1]:
        
        new_seq_1 = second_seq[:code_list[1]] + first_seq[code_list[1]+1:code_list[0]] + second_seq[code_list[0]:]
        new_seq_2 = first_seq[:code_list[1]] + second_seq[code_list[1]+1:code_list[0]] + first_seq[code_list[0]:]
        
        first_seq = new_seq_1
        second_seq = new_seq_2
        index += 1

str1 = ""
str2 = ""               
for i in range(len(first_seq)):
    str1 = str1 + first_seq[i] + " "
    str2 = str2 + second_seq[i] + " "
                    
print(str1)
print(str2)

        


