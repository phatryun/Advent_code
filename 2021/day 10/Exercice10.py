import os
import numpy as np
from tqdm import tqdm
from collections import Counter


def split_data(str_file_path):

    with open(str_file_path) as f:
        lines = [line.rstrip() for line in f]

    # res = [[e.split(' ') for e in elt] for elt in lines]

    return lines

    # return draw_numbers, list_bigo_grid


def part_1(data):
    """
    """

    # print(data)

    dict_char = {
        '}':'{',
        ']':'[',
        '>':'<',
        ')':'('
    }
    expected_char_dict = {value:key for key, value in dict_char.items()}                

    dict_point = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    list_syntax_error = []
    total_point = 0

    for line in data:
        list_elt = []
        # print(f"----> {line}")
        for char in line:
            # print(f"{list_elt} : {char}")
            if char in dict_char.keys():
                if list_elt[-1] != dict_char[char]:
                    # print(f"Problem: Expected {expected_char_dict[list_elt[-1]]}, but found {char} instead")
                    list_syntax_error.append(char)
                    total_point += dict_point[char]
                    break

                else:
                    del list_elt[-1]
            else:
                list_elt.append(char)

    # print(list_syntax_error)
    print(f"res: {total_point}")



    return True


def part_2(data):
    """
    """
    dict_char = {
        '}':'{',
        ']':'[',
        '>':'<',
        ')':'('
    }
    expected_char_dict = {value:key for key, value in dict_char.items()}                

    dict_point = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    list_syntax_error = []
    list_points = []

    for line in data:
        list_elt = []
        # print(f"----> {line}")
        incomplete = True
        for char in line:
            # print(f"{list_elt} : {char}")
            if char in dict_char.keys():
                if list_elt[-1] != dict_char[char]:
                    # print(f"Problem: Expected {expected_char_dict[list_elt[-1]]}, but found {char} instead")
                    list_syntax_error.append(char)
                    incomplete = False
                    break

                else:
                    del list_elt[-1]
            else:
                list_elt.append(char)
        if incomplete:
            missing_char = []
            total_points = 0 

            for i in range(1, len(list_elt)+1):
                char_tmp = expected_char_dict[list_elt[-i]]
                total_points *= 5
                total_points += dict_point[char_tmp]

                missing_char.append(char_tmp)


            # print(f"{line} -> {list_elt}")
            # print(f"{missing_char} -> {total_points}")
            list_points.append(total_points)


    print(f"res: {int(np.median(list_points))}")

    # print(list_syntax_error)
    # print(f"res : {total_point}")

    return True


if __name__ == "__main__":

    day = 10
    ex = "" # "_ex" # "" #

    data = split_data(f'input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)


    # Exercice 2
    print('## Excercice 2')
    part_2(data)
