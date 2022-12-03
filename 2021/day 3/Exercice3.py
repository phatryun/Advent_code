import os
import numpy as np
from collections import Counter


def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [[int(elt) for elt in line.rstrip()] for line in f]

    return np.array(lines)



def part_1(data):
    """
    
    """
    dataT = np.transpose(data)

    res_gamma_rate = ""
    res_epsilon_rate = "" 

    for i in range(len(dataT)):
        list_data = dataT[i]
        occurrence = list(Counter(list_data).most_common())
        res_gamma_rate += f"{occurrence[0][0]}"
        res_epsilon_rate += f"{occurrence[1][0]}"
    
    gamma_rate = int(res_gamma_rate, 2)
    epsilon_rate = int(res_epsilon_rate, 2)

    print(f"{gamma_rate} * {epsilon_rate} = {gamma_rate * epsilon_rate}")

    return True

def select_list(list_data, elt, position):

    res = list()

    for i in range(len(list_data)):
        if list_data[i][position] == elt:
            res.append(list_data[i]) 
    
    return res

def part_2(data):
    """
    
    """
    data_tmp = data.copy()
    # oxygen generator rating
    for i in range(len(data_tmp[0])):
        
        data_tmpT = np.transpose(data_tmp)
        list_data = data_tmpT[i]
        occurrence = list(Counter(list_data).most_common())
        occurrence = sorted(occurrence, key=lambda x: (x[1], x[0]), reverse=True)
        # print(occurrence)
        data_tmp = select_list(data_tmp, occurrence[0][0], i)
        # print(data_tmp)
        if len(data_tmp) == 1:
            break
    
    oxygen = "".join([f"{e}" for e in data_tmp[0]])
    print(f"oxygen generator rating: {oxygen} -> {int(oxygen, 2)}")

    data_tmp = data.copy()
    # CO2 scrubber rating
    for i in range(len(data_tmp[0])):
        
        data_tmpT = np.transpose(data_tmp)
        list_data = data_tmpT[i]
        occurrence = list(Counter(list_data).most_common())
        occurrence = sorted(occurrence, key=lambda x: (x[1], x[0]), reverse=False)
        # print(occurrence)
        data_tmp = select_list(data_tmp, occurrence[0][0], i)
        # print(data_tmp)
        if len(data_tmp) == 1:
            break
    
    co2 = "".join([f"{e}" for e in data_tmp[0]])
    print(f"CO2 scrubber rating: {co2} -> {int(co2, 2)}")

    print(f"{int(oxygen, 2)} * {int(co2, 2)} = {int(oxygen, 2) * int(co2, 2)}")

    return True


if __name__ == "__main__":

    day = 3
    ex = "" # "_ex" # "" #

    data = split_data(f'day {day}/input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)


    # Exercice 2
    print('## Excercice 2')
    part_2(data)
