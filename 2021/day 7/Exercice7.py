import os
import numpy as np
from collections import Counter


def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [[int(elt) for elt in line.rstrip().split(',')] for line in f]

    return np.array(lines[0])

# def calulate_horizontal_move(list_elt, data):
    


def part_1(data):
    """
    
    """
    print(data)
    mean = data.mean()
    
    min_move = 9999999999999999
    i_min_move = -1

    for i in range(0, data.max()):
        moves = data - i
        max_move = np.absolute(moves).sum()
        # print(f"{i} -> {moves} : {max_move}")

        if min_move > max_move:
            min_move = max_move
            i_min_move = i
    
    print(f"{i_min_move} -> {min_move}")

    return True



def part_2(data):
    """
    
    """

    print(data)
    mean = data.mean()
    
    min_move = 9999999999999999
    i_min_move = -1

    for i in range(0, data.max()):
        moves = data - i
        moves = np.absolute(moves)
        # triangle suite
        moves = moves * (moves + 1) / 2
        max_move = np.absolute(moves).sum()
        # print(f"{i} -> {moves} : {max_move}")

        if min_move > max_move:
            min_move = max_move
            i_min_move = i
    
    print(f"{i_min_move} -> {min_move}")

    return True

if __name__ == "__main__":

    day = 7
    ex = "" # "_ex" # "" #

    data = split_data(f'day {day}/input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)


    # Exercice 2
    print('## Excercice 2')
    part_2(data)
