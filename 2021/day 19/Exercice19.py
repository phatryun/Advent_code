import os
import re
import math
import numpy as np
from tqdm import tqdm
import time
from collections import Counter
import nltk

def split_data(str_file_path):
    list_scan_beacons = []
    with open(str_file_path) as f:
        res = []
        for line in f:
            # print(line.rstrip()[:3])
            if line.rstrip()[:3] == '---': # scanner'):
                print("new scanner")
                list_scan_beacons.append(res)
                res = []
            elif line.rstrip() == '':
                print("next")
            else:
                #print(line.rstrip()[:3] == '---')
                res.append([int(e) for e in line.rstrip().split(",")])
        list_scan_beacons.append(res)

    return list_scan_beacons[1:]


def nb_beacon_in_common(list_i_beacon, list_j_beacon):

    max_common = 0
    max_i_beacon = -1
    max_j_beacon = -1
    max_position = []

    for i_beacon in range(len(list_i_beacon)):
        for j_beacon in range(len(list_j_beacon)):
            # can be optiize
            nb_common = 0
            position = []
            for elt in list_i_beacon[i_beacon]:
                if elt in list_j_beacon[j_beacon]:
                    nb_common += 1
                    position.append(list_j_beacon[j_beacon].index(elt))
            if nb_common > max_common:
                max_common = nb_common
                max_i_beacon = i_beacon
                max_j_beacon = j_beacon
                max_position = position


    # print(f"{list_i_beacon} vs {list_j_beacon}")
    # print(f"{max_common}, {max_i_beacon}, {max_j_beacon}")
    # print(f"{position}")

    return max_common, max_i_beacon, max_j_beacon, position

def part_1(data):
    """
    """
    # print(data)
    res_point = []
    for i_scanner in range(len(data)):
        list_conversion = []
        for i_beacon in range(len(data[i_scanner])):
            list_e = []
            for j_beacon in range(len(data[i_scanner])):
                coord_i = data[i_scanner][i_beacon]
                coord_j = data[i_scanner][j_beacon]
                list_e.append(list(np.array(coord_j) - np.array(coord_i)))

            list_conversion.append(list_e)
        res_point.append(list_conversion)

    for i_scanner in range(len(res_point)):
        for j_scanner in range(i_scanner+1, len(res_point)):
            if i_scanner != j_scanner:

                nb_common, max_i_beacon, max_j_beacon, position = nb_beacon_in_common(res_point[i_scanner], res_point[j_scanner])

                print(f"{i_scanner} vs {j_scanner} -> {nb_common}")

                if nb_common > 2:
                    list_point = res_point
                # print(cpt)


    # print(res_point)
    return True

class Grid():


    def __init__(self, list_point):
        max_x = max([elt[0] for elt in list_point])
        max_y = max([elt[1] for elt in list_point])
        # max_z = max([elt[2] for elt in list_point])

        self.grid = np.zeros((max_x, max_y))
        for elt in list_point:
            self.grid[elt[1], elt[0]] = 1


    def merge(self, grid2):
        return self.grid

    def print_grid(self):
        print(self.grid)


def part_1(data):

    #sgrid = Grid()

    for i in range(1): #len(data)):
        g = Grid(data[i])
        g.print_grid()



def part_2(data):
    """
    """

    return True


if __name__ == "__main__":

    day = 19
    ex = "_ex_1" # "_ex" # "" #

    data = split_data(f'input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)

    # Exercice 2
    print('## Excercice 2')
    part_2(data)
