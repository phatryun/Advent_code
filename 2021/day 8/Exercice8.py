import os
import numpy as np
from tqdm import tqdm
from collections import Counter


def split_data(str_file_path):

    with open(str_file_path) as f:
        lines = [line.rstrip().split(' | ') for line in f]

    res = [[e.split(' ') for e in elt] for elt in lines]

    return res

    # return draw_numbers, list_bigo_grid


def part_1(data):
    """
    """

    # print(data)

    count_unique_seg = 0

    for i in range(len(data)):
        output_val = data[i][1]
        # print(output_val)
        output_val = Counter([len(elt) for elt in output_val])
        # print(output_val)

        if 2 in output_val:
            count_unique_seg += output_val[2]
        if 3 in output_val:
            count_unique_seg += output_val[3]
        if 4 in output_val:
            count_unique_seg += output_val[4]
        if 7 in output_val:
            count_unique_seg += output_val[7]
    #for i in range(len(dataT)):

    print(f"count_unique_seg : {count_unique_seg}")

    return True

def get_elt_of(list_num, len_search, list_to_remove):

    res = [elt for elt in list_num if (len(elt)==len_search) and (elt not in list_to_remove)]

    return res

def part_2(data):
    """
    """

    # 1 -> 2
    # 4 -> 4
    # 7 -> 3
    # 8 -> 7

    # 5 -> 5
    # 2 -> 5
    # 3 -> 5

    # 0 -> 6
    # 6 -> 6
    # 9 -> 6

    # 6 -> a qu'une seule lettre en commun avec le 1
    # 0 ->

    total_count = 0

    for i in range(len(data)):
        input_val = data[i][0]
        output_val = data[i][1]

        count_letter_input = [len(elt) for elt in input_val]

        dict_letters = {}

        one = input_val[count_letter_input.index(2)]
        seven = input_val[count_letter_input.index(3)]
        four = input_val[count_letter_input.index(4)]
        eight = input_val[count_letter_input.index(7)]

        # print(f"one: {one}, seven: {seven}, four: {four}, eight: {eight}")

        # get 6: only 1 letter in common with 1
        list_six = get_elt_of(input_val, 6, [])
        list_six = [elt for elt in list_six if len(set(one)&set(elt)) == 1]
        if len(list_six) > 1:
            print("six error")
        six = list_six[0]
        
        # get 9: include the 4
        list_nine = get_elt_of(input_val, 6, [six])
        list_nine = [elt for elt in list_nine if len(set(four)&set(elt)) == 4]
        if len(list_nine) > 1:
            print("nine error")
        nine = list_nine[0]
        
        # 0 is the left over 6 char
        list_zero = get_elt_of(input_val, 6, [six, nine])
        if len(list_zero) > 1:
            print("zero error")
        zero = list_zero[0]

        # print(f"six: {six}, nine: {nine}, zero: {zero}")

        # 3 as 3 letter in common with 7
        list_three = get_elt_of(input_val, 5, [])
        list_three = [elt for elt in list_three if len(set(seven)&set(elt)) == 3]
        if len(list_three) > 1:
            print("three error")
        three = list_three[0]

        
        # 5 has only 3 letter in common with 4 
        list_five = get_elt_of(input_val, 5, [three])
        list_five = [elt for elt in list_five if len(set(four)&set(elt)) == 3]
        if len(list_five) > 1:
            print("five error")
        five = list_five[0]

        
        # 2 is the left over 5 char
        list_two = get_elt_of(input_val, 5, [three, five])
        if len(list_two) > 1:
            print("two error")
        two = list_two[0]
        # print(f"three: {three}, five: {five}, two: {two}")

        dict_letters = {zero:0, one:1, two:2, three:3, four:4, five:5, six:6, seven: 7, eight: 8, nine: 9}

        str_number = ""
        for elt in output_val:
            # print(elt)
            for key, val in dict_letters.items():
                if set(elt) == set(key):
                    # print(f"{elt} : {val}")
                    str_number += f"{val}"

        # print(f"{dict_letters}")
        # print(int(str_number))

        total_count += int(str_number)


    print(f"total_count: {total_count}")
    return True


if __name__ == "__main__":

    day = 8
    ex = "" # "_ex" # "" #

    data = split_data(f'input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)


    # Exercice 2
    print('## Excercice 2')
    part_2(data)
