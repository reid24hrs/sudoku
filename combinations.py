# python 2 program to calculate the valid combinations of 
# n digits in the set n E {1-9} where each n digit does not repeat 
# that add up to the total s

import itertools as iter

n = input("Enter length of combination: ")
s = input("Enter the total value the combination must add up to: ")
sequence_length = 9 # every line in Sudoku is always 9 values long

x = list(range(1,10)) # create a list of the numbers 1-9

# create the matrix of combinations of n digits

combinations = list(iter.combinations(x, n))
# print(combinations)

solutions = [] # create an empty list to append valid solutions

for i in range(len(combinations)):
   if sum(combinations[i]) == s:
      solutions.append(combinations[i]) 

print(solutions)



