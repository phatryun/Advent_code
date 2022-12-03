import os
import numpy as np
from tqdm import tqdm
from collections import Counter


def split_data(str_file_path):

    with open(str_file_path) as f:
        lines = [line.rstrip() for line in f]

    res = [int(e) for e in lines[0].split(",")]

    return res

    # return draw_numbers, list_bigo_grid


def part_1(data):
    """
    """

    print(data)
    data_array = np.array(data)
    for day in range(80):

        data_array = data_array - 1
        nb_new = np.count_nonzero(data_array == -1)
        data_array = np.where(data_array == -1, 6, data_array)

        #print(f"nb new: {nb_new}")
        if nb_new > 0:
            data_new = np.array([8 for i in range(nb_new)])
            # print(f"data_new: {data_new}")
            data_array = np.append(data_array, data_new)
        if (day+1 == 18) or (day+1 == 80):
            print(f"day {day+1} -> {len(data_array)} : {data_array}")

    #for i in range(len(dataT)):

    

    return True


def part_2(data):
    """
    """
    
    print(data)
    data_array = np.array(data)

    dict_fish_old = {elt:0 for elt in range(9)}
    for i in range(9):
        dict_fish_old[i] = np.count_nonzero(data_array == i)
    print(dict_fish_old)

    for day in tqdm(range(256)):
        # each day we car counting fish that are in categories
        tmp = {elt:0 for elt in range(9)}
        for i in range(8, -1, -1):
            if i != 0:
                tmp[i-1] = tmp[i-1] + dict_fish_old[i]
            else:
                tmp[8] = dict_fish_old[i]
                tmp[6] = tmp[6] + dict_fish_old[i]

        dict_fish_old = tmp

        # print(dict_fish_old)
        if (day+1 == 18) or (day+1 == 80) or (day+1 == 256):
            print(f"day {day+1} -> {sum(dict_fish_old.values())}")

    # 26984457539
    # 26984457539

    return True


if __name__ == "__main__":

    day = 6
    ex = "" # "_ex" # "" #

    data = split_data(f'input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)


    # Exercice 2
    print('## Excercice 2')
    part_2(data)
