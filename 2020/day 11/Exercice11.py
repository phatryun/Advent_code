import os
import numpy as np

def get_adjacent_seat(grid, x, y):

    x_min = max(0, x - 1)
    x_max = min(len(grid[0]) - 1, x + 1)

    y_min = max(0, y - 1)
    y_max = min(len(grid) - 1, y + 1)

    #print(x_min, x_max)
    #print(y_min, y_max)
    res_adj_seat = []

    for j in range(y_min, y_max + 1) :
        for i in  range(x_min, x_max+ + 1) :
            if (i != x) or (j != y) :
                if grid[j][i] == '#' or grid[j][i] == 'L' :
                    res_adj_seat.append(grid[j][i])

    return res_adj_seat

def getFirstSeatFromList(grid, list_x, list_y) :
    res = "."
    for iter_x in range(len(list_x)) :
        i = list_x[iter_x]
        j = list_y[iter_x]

        print(f'x : {i}, y : {j}  ==> {grid[j][i]}')
        if grid[j][i] == '#' or grid[j][i] == 'L' :
            res = grid[j][i]
            break
    return res

def getFirstSeatFromAdd(grid, x, y, add_x, add_y) :
    res = "."
    i = x
    j = y
    max_i = len(grid[0])
    max_j = len(grid)

    while (0 <= i + add_x < max_i) and (0 <= j + add_y < max_j) :
        i += add_x
        j += add_y
        #print(f'x : {i}, y : {j}  ==> {grid[j][i]}')
        if grid[j][i] == '#' or grid[j][i] == 'L' :
            res = grid[j][i]
            break

    return res

def get_adjacent_seat_2(grid, x, y):

    res_adj_seat = []

    list_x = [-1, 0, 1]
    list_y = [-1, 0, 1]

    for add_x in list_x :
        for add_y in list_y :
            if not (add_x == 0 and add_y == 0) :
                #print(f'add_x : {add_x}, add_y : {add_y}')
                res_adj_seat.append(getFirstSeatFromAdd(grid, x, y, add_x, add_y))

    return res_adj_seat

def listCopy(list_input) :
    res_input = []
    for y in range(len(list_input)) :
        line = []
        for x in range(len(list_input[y])) :
            line.append(list_input[y][x])
        res_input.append(line)
    return res_input

def lifePlaySeat(grid, m=1) :
    new_grid = listCopy(grid)

    for j in range(len(grid)) :
        for i in range(len(grid[j])) :
            if m == 1 :
                adj_seats = get_adjacent_seat(grid, i, j)
            else :
                adj_seats = get_adjacent_seat_2(grid, i, j)
            occupied_seat = adj_seats.count('#')

            #if j == 1 :
                #print(f'{j} --> {adj_seats} : {occupied_seat}')


            if (grid[j][i] == 'L') and (occupied_seat == 0) :
                new_grid[j][i] = '#'

            if m == 1 :
                if (grid[j][i] == '#') and (occupied_seat >= 4) :
                    new_grid[j][i] = 'L'
            else :
                if (grid[j][i] == '#') and (occupied_seat >= 5) :
                    new_grid[j][i] = 'L'

    grid_are_eq = GridsEquals(grid, new_grid)

    return new_grid, grid_are_eq

def printGrid(grid) :
    for y in range(len(grid)) :
        print('|'.join(grid[y]))

def GridsEquals(grid_1, grid_2) :
    res = True
    for y in range(len(grid_1)) :
        for x in range(len(grid_1[y])) :
            res *= grid_1[y][x] == grid_2[y][x]

    return res


with open('./input.txt') as f:
    lines = [[l for l in line.rstrip()] for line in f]


grid = listCopy(lines)

'''
grid_are_eq = 0
i = 1
while i < 100 and grid_are_eq == 0 :
    grid, grid_are_eq = lifePlaySeat(grid)
    print(f'after iteration {i} ==> {grid_are_eq}')
    #printGrid(grid)
    i += 1

#printGrid(grid)
cpt_seat_occ = 0
for y in range(len(grid)) :
    cpt_seat_occ += grid[y].count('#')

print(f'Part 1 : {cpt_seat_occ}')
'''
grid_are_eq = 0
i = 1
while i < 100 and grid_are_eq == 0 :
    grid, grid_are_eq = lifePlaySeat(grid, m=2)
    print(f'after iteration {i} ==> {grid_are_eq}')
    #printGrid(grid)
    i += 1

cpt_seat_occ = 0
for y in range(len(grid)) :
    cpt_seat_occ += grid[y].count('#')

print(f'Part 2 : {cpt_seat_occ}')
