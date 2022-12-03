import os
import numpy as np

with open('day 9/input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

array_lines = np.array(lines)
working_array = np.array(lines)

def getSumElement(array_elt, sum_val) :

    for i in range(len(array_elt)) :
        i_val = array_elt[i]
        diff = sum_val - i_val
        temp_array = array_elt[array_elt == diff]
        if len(temp_array) > 0 :
            if temp_array[0] != i_val :
                #print(f'{i_val} + {temp_array[0]} = {sum_val}')
                return True

    return False




sum_ok = True
nb_elt = 25
elt_failed = 0

while (len(working_array) > (nb_elt + 1)) & sum_ok :
    #print(f'{working_array[:5]} -> {working_array[5]}')
    sum_ok = getSumElement(working_array[:nb_elt], working_array[nb_elt])
    if sum_ok :
        working_array = np.delete(working_array, 0)
    else :
        print(f'Part 1 : {working_array[nb_elt]}')
        elt_failed = working_array[nb_elt]


def getContiguousSet(array_elt, sum_val) :

    for start in range(len(array_elt) - 1) :
        cpt = array_elt[start]
        for end in range(start+1, len(array_elt)) :
            cpt += array_elt[end]
            if cpt == sum_val :
                return start, end

    return -1, -1

working_array = np.array(lines)
i_elt = np.where(working_array == elt_failed)[0][0]

print(i_elt)


i_start, i_end = getContiguousSet(working_array[:i_elt], elt_failed)
min_arr = working_array[i_start:i_end+1].min()
max_arr = working_array[i_start:i_end+1].max()
print(f'{working_array[i_start:i_end+1]} -> {min_arr} + {max_arr} = {min_arr + max_arr}')



