import os
import numpy as np
from collections import Counter

from numpy.core.fromnumeric import reshape
from numpy.core.function_base import _linspace_dispatcher


def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [[int(elt) for elt in line.rstrip()] for line in f]

    return np.array(lines)

def get_neighbors(data, i, j):

    tmp = 0
    res = []
    if i - 1 >= 0:
        res.append(((i-1, j), data[i - 1][j]))
    
    if i + 1 <= len(data) - 1:
        res.append(((i+1, j), data[i + 1][j]))
        #print(f"data[i + 1][j] : {data[i + 1][j]}")

    if j - 1 >= 0:
        res.append(((i, j-1), data[i][j - 1]))
        # print(f"data[i][j - 1] : {data[i][j - 1]}")

    if j + 1 <= len(data[i]) - 1:
        res.append(((i, j+1), data[i][j + 1]))
        # print(f"data[i][j + 1] : {data[i][j + 1]}")
    
    return res

def part_1(data, print_res=True):
    """
    
    """
    # print(data)

    res = np.array([])
    lower_start = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            # print(f"i: {i}, j: {j}, data[i][j]: {data[i][j]}")
            list_neighbors = get_neighbors(data, i, j)
            list_neighbors = np.array([elt[1] for elt in list_neighbors])
            # print(list_neighbors)

            nb_lower = (list_neighbors <= data[i][j]).sum()
            # print(nb_lower)
            if nb_lower == 0:
                # print(data[i])
                res = np.append(res, data[i][j])
                lower_start.append((i,j))

    res = res + 1
    if print_res:
        # print(res)
        print(f"res: {res.sum()}")

    return lower_start

def get_higher_neighbors(data, i, j):

    lower_point = data[i][j]
    list_neighbors = get_neighbors(data, i, j)
    # get higher neighbors and remove 9
    higher_neighbors = [elt for elt in list_neighbors if (elt[1] > lower_point) and (elt[1] < 9)]
    # remove already known 

    if len(higher_neighbors) == 0:
        return [((i, j), lower_point)]

    res = [((i, j), lower_point)]
    for elt in higher_neighbors:
        new_i, new_j = elt[0]
        res += get_higher_neighbors(data, new_i, new_j)
    
    return res

def part_2(data):
    """
    
    """
    # print(data)
    lower_start = part_1(data, print_res=False)

    list_bassin = []

    for i in range(len(lower_start)):
        i, j = lower_start[i]
        basins = set(get_higher_neighbors(data, i, j))
        list_bassin.append(basins)
        # print(f"{[elt[1] for elt in basins]} : {len(basins)}")    
        #print(basins)
    
    size_bassins = [len(x) for x in list_bassin]
    size_bassins.sort()

    print(f"res: {size_bassins[-3] * size_bassins[-2] * size_bassins[-1]}")

    return True

if __name__ == "__main__":

    import sys
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(1500)


    day = 9
    ex = "" # "_ex" # "" #
    
    data = split_data(f'day {day}/input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)


    # Exercice 2
    print('## Excercice 2')
    part_2(data)
