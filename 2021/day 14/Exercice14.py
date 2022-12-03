import os
import re
import numpy as np
from tqdm import tqdm
import time
from collections import Counter
import nltk

def split_data(str_file_path):

    with open(str_file_path) as f:
        lines = [line.rstrip() for line in f]

    polymer_template = lines[0]

    insertion_rules = [elt.split(" -> ") for elt in lines[2:]]

    return polymer_template, insertion_rules


def part_1(data):
    """
    """
    polymer_template, insertion_rules = data

    array_polymer = [elt for elt in polymer_template]
    # transform polymer_template as np.array

    # print(polymer_template)
    # print(insertion_rules)

    for i in range(10):
        list_instertions = []
        # print(f"{i+1} ")# : {array_polymer}")
        t = time.time()

        for rule, insertion in insertion_rules:
            positions = [i for i in range(len(array_polymer) -1) if "".join(array_polymer[i:i+2]) == rule]
            # positions = re.finditer(rule, polymer_template)
            for p in positions:
                list_instertions.append((insertion, p+1))

        list_instertions = sorted(list_instertions, key=lambda x: -x[1])
        # print(list_instertions)
        # print(len(array_polymer))
        # print(f"find insertion in {time.time() - t:.2f} seconds")
        t = time.time()
        for insertion, position in list_instertions:
            #polymer_template = polymer_template[:position] + insertion + polymer_template[position:]
            array_polymer.insert(position, insertion)

        # print(f"did insertion in {time.time() - t:.2f} seconds")
        # print(f"{i} -> {len(polymer_template)}")

        # if i == 0: assert polymer_template == "NCNBCHB"
        # if i == 1: assert polymer_template == "NBCCNBBBCBHCB"
        # if i == 2: assert polymer_template == "NBBBCNCCNBBNBNBBCHBHHBCHB"
        # if i == 3: assert polymer_template == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    
        # print("".join(array_polymer))

        c = Counter(array_polymer).most_common()
        list_c = sorted(c, key=lambda x: x[1])
        # print(list_c)
    
    print(f"most({list_c[-1][0]}) - least({list_c[0][1]}) = {list_c[-1][1]} - {list_c[0][1]} = {list_c[-1][1] - list_c[0][1]}")


    return True




def part_2(data):
    """
    """
    polymer_template, insertion_rules = data
    # print(polymer_template)

    list_polymer = [polymer_template[i:i+2] for i in range(len(polymer_template)-1)]

    dict_part_polymer = {elt[0]:elt[1] for elt in Counter(list_polymer).most_common()}

    # print(dict_part_polymer)
    # transform polymer_template as np.array
    dict_rules = {elt[0]:elt[1] for elt in insertion_rules}
    # print(dict_rules)

    for i in range(40):
        list_part_polymer = [key for key, val in dict_part_polymer.items() if val > 0]
        tmp_dict_part_polymer = dict_part_polymer.copy()

        for part_polymer in list_part_polymer:
            
            if part_polymer in dict_rules:
                val = dict_rules[part_polymer]
                nb_part_polymer = tmp_dict_part_polymer[part_polymer]
                # print(part_polymer, val, nb_part_polymer)
                
                new_part_1, new_part_2 = f"{part_polymer[0]}{val}", f"{val}{part_polymer[1]}"
                # add new_part_1
                if new_part_1 in dict_part_polymer:
                    dict_part_polymer[new_part_1] += nb_part_polymer
                else:
                    dict_part_polymer[new_part_1] = nb_part_polymer

                # add new_part_2
                if new_part_2 in dict_part_polymer:
                    dict_part_polymer[new_part_2] += nb_part_polymer
                else:
                    dict_part_polymer[new_part_2] = nb_part_polymer

                dict_part_polymer[part_polymer] -= nb_part_polymer

            # print(dict_part_polymer)
    dict_res = {}
    for elt, val in  dict_part_polymer.items():
        for i in range(2):
            if elt[i] in dict_res:
                dict_res[elt[i]] += val
            else:
                dict_res[elt[i]] = val

    # print(dict_part_polymer)
    dict_res[polymer_template[0]] += 1
    dict_res[polymer_template[-1]] += 1

    list_c = {(e, int(val/2)) for e,val in dict_res.items()}
    list_c = sorted(list_c, key=lambda x: x[1])
    # print(i, len(list_part_polymer), list_c)

    # 2188189693529
    # 2188189693529
    # 722030768103
    # 3689857240399
    
    print(f"most({list_c[-1][0]}) - least({list_c[0][1]}) = {list_c[-1][1]} - {list_c[0][1]} = {list_c[-1][1] - list_c[0][1]}")


    return True


if __name__ == "__main__":

    day = 14
    ex = "" # "_ex" # "" #


    data = split_data(f'input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)

    # Exercice 2
    print('## Excercice 2')
    part_2(data)
