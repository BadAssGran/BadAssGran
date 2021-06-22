# -*- coding: utf-8 -*-

"""
The Matrix Rules

The Architect did his best to make the current iteration of the Matrix as unpredictable and chaotic as possible. If only he could change the fundamental rules that governed the Matrix he would get rid of the Oracle once and for all!. Unfortunately for him the rules of the Matrix could not be changed. Not by him, not by anyone. This immutability of the rules was ensuring that the predictions of the Oracle would always be correct.
The source code of the Matrix is a long sequence of 0s and 1s. These 0s and 1s are called cells, for short, and each cell can be either dead (0) or alive (1). To give you a better understanding the sequence 101 has 2 alive cells and 1 dead cell whereas the sequence 11010 has 3 alive cells and 2 dead. By applying the fundamental rules to a sequence of code the Oracle can calculate its next state and calibrate her predictions of the future.
The fundamental rules of the Matrix are: 1. Any dead cell with less than two live neighbours remains dead. 2. Any dead cell with two live neighbours becomes a live cell. 3. Any live cell with two dead neighbours dies, as if by starvation. 4. Any live cell with two live neighbours dies, as if by overpopulation. 5. Any live cell with exactly one live neighbour survives.
Your task is to help the Oracle by applying the rules to several code seqences.
Input
Read from the standard input:
•	There is one line of input, a string:
•	101
Output
Print to the standard output:
•	One line of output - the next state of the sequence.
•	111
Constraints
•	Each cell has exactly two neighbours - left and right.
•	The left neighbour of the first cell is the last cell in the sequence.
•	The right neighbour of the last cell is the first cell in the sequence.
•	3 <= sequence length <= 50
Sample tests
Input
101
Output
111
________________________________________
Input
0111
Output
1101

"""
seq = input()

seq_list = [int(x) for x in seq if x.isalnum()]

new_list = [seq_list[-1]] + seq_list + [seq_list[0]]

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

            
