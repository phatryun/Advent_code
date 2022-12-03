import os
import numpy as np
from tqdm import tqdm
from collections import Counter


def split_data(str_file_path):

    with open(str_file_path) as f:
        lines = [[int(elt) for elt in line.rstrip()] for line in f]

    # res = [[e.split(' ') for e in elt] for elt in lines]

    return np.array(lines)

    # return draw_numbers, list_bigo_grid

def add_neighbors(data, x, y):

    if x >= 0 and x < len(data):
        if y >= 0 and y < len(data[x]):
            if data[x][y] > 0:            
                data[x][y] += 1

    return data


def flash_neighbors(data, x, y):

    data[x][y] = 0

    data = add_neighbors(data, x - 1, y - 1)
    data = add_neighbors(data, x, y - 1)
    data = add_neighbors(data, x + 1, y - 1)
    data = add_neighbors(data, x - 1, y)
    data = add_neighbors(data, x, y)
    data = add_neighbors(data, x + 1, y)
    data = add_neighbors(data, x - 1, y + 1)
    data = add_neighbors(data, x, y + 1)
    data = add_neighbors(data, x + 1, y + 1)

    return data


def part_1(data):
    """
    """

    # print("Before any steps:")
    # print(data)

    cpt_flash = 0

    for i in range(100):
        data = data + 1

        is_flash = len(data[data > 9]) > 0
        while is_flash:
            for x in range(len(data)):
                for y in range(len(data[x])):
                    if data[x][y] > 9:
                        cpt_flash += 1
                        data = flash_neighbors(data, x, y)
    
            is_flash = len(data[data > 9]) > 0

    print(f"\nAfter step {i+1}: -> {cpt_flash}")
    print(data)


    return True


def part_2(data):
    """
    """
    # print("Before any steps:")
    # print(data)

    cpt_flash = 0

    for i in range(1000):
        data = data + 1

        is_flash = len(data[data > 9]) > 0
        while is_flash:
            for x in range(len(data)):
                for y in range(len(data[x])):
                    if data[x][y] > 9:
                        cpt_flash += 1
                        data = flash_neighbors(data, x, y)
    
            is_flash = len(data[data > 9]) > 0

        nb_flash = len(data[data == 0])

        if nb_flash == 100:
            print(f"ALL flash at step : {i+1}")
            break
        #print(f"\nAfter step {i+1}: -> {cpt_flash} -> {nb_flash}")
        #print(data)


    return True


if __name__ == "__main__":

    day = 11
    ex = "" # "_ex" # "" #

    data = split_data(f'input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)


    # Exercice 2
    print('## Excercice 2')
    part_2(data)
