import os
import numpy as np
from collections import Counter


def split_data(str_file_path):

    with open(str_file_path) as f:
        lines = [line.rstrip() for line in f]

    grid_max = 1
    list_coord = []
    for line in lines:
        p1, p2 = line.split(' -> ')
        x1, y1 = (int(e) for e in p1.split(',')) #, x2, y2 = #((int(e) for e in elt.split(',')) fline.split(' -> ')or elt in line.split(' -> '))
        x2, y2 = (int(e) for e in p2.split(',')) #, x2, y2 = #((int(e) for e in elt.split(',')) fline.split(' -> ')or elt in line.split(' -> '))

        grid_max = max(grid_max, x1, y1, x2, y2)
        list_coord.append(((x1, y1), (x2, y2)))


    return grid_max, list_coord

    # return draw_numbers, list_bigo_grid


def get_points_diagonal(x1, y1, x2, y2):

    res = list()

    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    min_x, max_x = min(x1, x2), max(x1, x2)

    for x in range(min_x, max_x + 1):
        res.append((x, int(a * x + b)))

    return res

def get_points_line(x1, y1, x2, y2):

    res = list()
            
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    for x in range(min_x, max_x + 1):        
        for y in range(min_y, max_y + 1):
            res.append((x, y))

    return res

def part_1(data):
    """
    
    """
    grid_max, list_coord = data

    print(f'grid size: {grid_max}')

    grid = np.zeros(shape=(grid_max + 1, grid_max + 1))

    for set_coord in list_coord:
        (x1, y1), (x2, y2) = set_coord
        #print(f'x1 = {x1}, y1 = {y1}, x2 = {x2}, y2 = {y2}' )

        if (x1 == x2) or (y1 == y2): 
            points = get_points_line(x1, y1, x2, y2)
            for px, py in points:
                grid[py][px] += 1
            #print(points)

            #print(grid)
    print(grid)
    # count final result
    print(f"grid >= 2 : {sum(sum(grid >= 2))}")

    #for i in range(len(dataT)):

    

    return True


def part_2(data):
    """
    
    """
    grid_max, list_coord = data

    print(f'grid size: {grid_max}')

    grid = np.zeros(shape=(grid_max + 1, grid_max + 1))

    for set_coord in list_coord:
        (x1, y1), (x2, y2) = set_coord
        #print(f'x1 = {x1}, y1 = {y1}, x2 = {x2}, y2 = {y2}' )

        if (x1 == x2) or (y1 == y2): 
            points = get_points_line(x1, y1, x2, y2)
            for px, py in points:
                grid[py][px] += 1
            #print(points)
        else:
            points = get_points_diagonal(x1, y1, x2, y2)
            # print(f'x1 = {x1}, y1 = {y1}, x2 = {x2}, y2 = {y2}' )
            # print(points)
            for px, py in points:
                grid[py][px] += 1
            

            #print(grid)
    print(grid)
    # count final result
    print(f"grid >= 2 : {sum(sum(grid >= 2))}")


if __name__ == "__main__":

    day = 5
    ex = "" # "_ex" # "" #

    data = split_data(f'input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)


    # Exercice 2
    print('## Excercice 2')
    part_2(data)
