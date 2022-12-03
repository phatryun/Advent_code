import os
import numpy as np

with open('day 1/input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

array_lines = np.array(lines)

print('## Excercice 1')
## Excercice 1
for i in range(len(lines)) :
    i_val = array_lines[i]
    diff = 2020 - i_val
    temp_array = array_lines[array_lines == diff]
    if len(temp_array) > 0 :
        elt = temp_array[0]
        print(f'{i_val} + {elt} = {i_val + elt} & {i_val} * {elt} = {i_val * elt}')

print('## Excercice 2')
## Exercice 2
for i in range(len(lines)) :
    i_val = array_lines[i]
    diff = 2020 - i_val
    temp_array = array_lines[array_lines <= diff]
    if len(temp_array) > 0 :
        #print('coucou')
        for j in range(len(temp_array)) :
            j_val = temp_array[j]
            diff_2 = diff - j_val
            temp_array2 = temp_array[temp_array == diff_2]
            if len(temp_array2) > 0 :
                elt = temp_array2[0]
                print(f'{i_val} + {j_val} + {elt} = {i_val + j_val + elt} & {i_val} * {j_val} * {elt} = {i_val * j_val * elt}')
