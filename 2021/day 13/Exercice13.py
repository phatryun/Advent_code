import os
import numpy as np
from tqdm import tqdm
from collections import Counter


def split_data(str_file_path):

    with open(str_file_path) as f:
        lines = [line.rstrip() for line in f]

    i = lines.index("")

    max_x = 0
    max_y = 0
    
    fold_instructions = lines[i + 1:]
    res_instruction = []
    for instruction in fold_instructions:
        i_instruction = instruction.index('=')
        ax = instruction[i_instruction - 1]
        position = int(instruction[i_instruction + 1:])
        res_instruction.append((ax, position))
        if ax == 'x':
            max_x = max(max_x, position * 2 + 1)
        if ax == 'y':
            max_y = max(max_y, position * 2 + 1)

    dots = lines[:i]
    dots = [[int(e) for e in elt.split(',')] for elt in dots]
    
    paper = np.zeros(shape=(max_y, max_x))
    for x, y in dots:
        paper[y][x] = 1

    return paper, res_instruction


def fold(paper, way, position):

    res_paper = []
    if way == 'x':
        paper = np.transpose(paper)
    
    # Fold
    max_y = max(len(paper)-position, position)
    for i in range(1, max_y):
        res = np.zeros(shape=len(paper[0]))
        if position - i >= 0:
            res += paper[position - i]
        if position + i <= len(paper):
            res += paper[position + i]

        res_paper.insert(0, res)

    res_paper = np.array(res_paper)

    if way == 'x':
        res_paper = np.transpose(res_paper)

    return res_paper


def part_1(data):
    """
    """

    paper, fold_instructions = data

    for ax, position in fold_instructions[:1]:

        paper = fold(paper, ax, position)
        
    print((paper > 0).sum())

    return True


def part_2(data):
    """
    """

    paper, fold_instructions = data

    print(len(paper))
    print(len(paper[0]))
    print(655 * 2 + 1)
    print(447 * 2 + 1 )

    paper_print = [["#" if e > 0 else "." for e in elt] for elt in paper]
    
    for ax, position in fold_instructions:

        paper = fold(paper, ax, position)
    
    paper_print = [["#" if e > 0 else " " for e in elt] for elt in paper]
    print("\n")
    print("\n".join(["".join(elt) for elt in paper_print]))
    

    return True


if __name__ == "__main__":

    day = 13
    ex = "" # "_ex" # "" #

    data = split_data(f'input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)


    # Exercice 2
    print('## Excercice 2')
    part_2(data)
