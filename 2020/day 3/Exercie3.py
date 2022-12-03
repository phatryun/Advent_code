import os
import math
import numpy as np

with open('day 3/input.txt') as f:
    lines = [line.rstrip() for line in f]


#construct grid

x_grid = len(lines[0])
y_grid = len(lines)
print(f'x -> {len(lines[0])}')
print(f'y -> {len(lines)}')

x_max = 1#math.ceil((7 * y_grid + 1) / x_grid)
grid = []
for j in range(y_grid) :
    line = []
    for i in range(x_max) :
        line += list(lines[j])
    grid.append(line)

moves = [(1,1), (3,1), (5,1), (7,1), (1,2)]

cpt_global = 1

for right, down in moves :
    position_x = 0
    position_y = 0
    cpt_good = 0
    cpt_tree = 0
    while (position_y < y_grid -1):
        position_x =(position_x + right) % x_grid
        position_y += down
        val_grid = grid[position_y][position_x]

        if val_grid == '.' :
            cpt_good += 1
        elif val_grid == '#' :
            cpt_tree += 1
        else : print('problem varme ! ')

        #print(grid[position_y][position_x])

    print(f'cpt_tree : {cpt_tree}')
    cpt_global *= cpt_tree

print(f'cpt_global : {cpt_global}')
