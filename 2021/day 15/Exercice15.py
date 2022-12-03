import os
import re
import math
import numpy as np
from tqdm import tqdm
import time
from collections import Counter
import nltk

def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [[int(elt) for elt in line.rstrip()] for line in f]

    return np.array(lines)


def get_neighbors(data, position, previous):
    i, j = position
    tmp = 0
    res = []
    if i - 1 >= 0:
        res.append(((i - 1, j), data[j][i - 1]))

    if i + 1 <= len(data) - 1:
        res.append(((i + 1, j), data[j][i + 1]))
        # print(f"data[i + 1][j] : {data[i + 1][j]}")

    if j - 1 >= 0:
        res.append(((i, j - 1), data[j - 1][i]))
        # print(f"data[i][j - 1] : {data[i][j - 1]}")

    if j + 1 <= len(data[i]) - 1:
        res.append(((i, j + 1), data[j + 1][i]))
        # print(f"data[i][j + 1] : {data[i][j + 1]}")

    res = [e for e in res if e[0] not in previous]

    return res


def get_best_path(data, x, y, path, current_cost):

    print(f"x: {x}, y:{y} -> {data[y][x]} ===> {current_cost} ")
    tmp_path = path.copy()
    tmp_current_cost = current_cost


    if y == len(data) and x == len(data[y]):
        print('Goal reach')
        return True

    list_neighbours = get_neighbors(data, x, y, path)
    list_neighbours = sorted(list_neighbours, key=lambda x: -x[1])
    for neighbors, score in list_neighbours:
        print(neighbors, score)

    # get_best_path(data, neighbors[0], neighbors[1], tmp_path, tmp_current_cost)

def distance(point, goal):
    (x1, y1) = point
    (x2, y2) = goal
    # return math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
    return (x2 + y2 - x1 - y1) * 4

    # return abs(x1 - x2) + abs(y1 - y2)
def part_1(data):
    """
    """
    print(data)
    x, y = 0, 0
    path = []
    max_iter = 0
    goal = len(data)-1, len(data[len(data) - 1 ]) - 1
    start = (0, 0)
    first_dist = distance((0, 0), goal)
    print(first_dist)
    print(f"goal: {goal}")
    #f; h; g; path
    list_possibilities = [(0, 0, 0, [start])]
    cpt = 0
    goal_acheive = True
    res = ()
    while goal_acheive :# and cpt < 2000:
        cpt += 1
        list_possibilities = sorted(list_possibilities, key=lambda x: (x[0], x[1], x[2], len(x[3])))
        # print(list_possibilities)
        f, dist_to_goal, risk_level_path, path = list_possibilities.pop(0)

        if cpt % 100 == 0:
            print(f"{cpt} -> risk: {risk_level_path}, dist: {dist_to_goal}, f: {f}")

        list_neighbors = get_neighbors(data, path[-1], path[:-1])
        for neighbor, risk_level in list_neighbors:
            x, y = neighbor
            tmp_path = path.copy()
            #print(neighbor)
            tmp_path.append(neighbor)
            dist_end = distance(neighbor, goal)
            dist_start = distance(neighbor, start)

            new_risk_level = risk_level_path + risk_level
            #new_risk_level = dist_end + new_risk_level  # (best_risk_level + risk_level)  # (best_risk_level + 1) * dist / first_dist
            res = (dist_end + new_risk_level, dist_end, new_risk_level, tmp_path)
            list_possibilities.append(res)
            if neighbor == goal :
                print(f"goal acheive !")
                goal_acheive = False
        # print(list_possibilities)

    # for i_print in range(len(list_possibilities)):
    #     print(list_possibilities[i_print])
    # get_best_path(data, 0, 0, [], 0)
    # list_possibilities = sorted(list_possibilities, key=lambda x: x[0])
    # print(list_possibilities)
    print(f"Done in {cpt} iterations")
    _, dist_goal, risk_level, path = res
    # print(f"####{path}")
    # path_point = [((i, j), data[j, i]) for i, j in path]
    # path_risk_level = [data[j, i] for i, j in path if i != ]
    data_tmp = data.copy()
    for y_tmp in range(len(data_tmp)):
        for x_tmp in range(len(data_tmp[y_tmp])):
            if (x_tmp, y_tmp) in path:
                data_tmp[y_tmp][x_tmp] = data_tmp[y_tmp][x_tmp]
            else:
                data_tmp[y_tmp][x_tmp] = 0

    #print print(data)
    print(data_tmp)
    print(f"{risk_level} -> {path}")

    return True




def part_2(data):
    """
    """

    return True


if __name__ == "__main__":

    day = 15
    ex = "_ex" # "_ex" # "" #

    data = split_data(f'input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)

    # Exercice 2
    print('## Excercice 2')
    part_2(data)
