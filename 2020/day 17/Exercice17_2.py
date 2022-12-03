import os
from operator import itemgetter
from tqdm import tqdm

def printGridDict(grids) :
    for w in grids.keys():
        for z in grids[w].keys():
            print(f'\nz={z}, w={w}')
            for y in grids[w][z].keys() :
                print('|'.join(list(grids[w][z][y].values())))



def getvaluefromGrid(grid, x, y, z, w):
    if w in grid.keys() :
        if z in grid[w].keys() :
            if y in grid[w][z].keys():
                if x in grid[w][z][y].keys() :
                    return grid[w][z][y][x]

    return "."

def getNeighboursActives(grid, elt) :

    list_neighbours = neighboursFromDist(elt[0], elt[1], elt[2], elt[3], 1)

    cpt_active = 0
    for nei in list_neighbours :
        val_nei = getvaluefromGrid(grid, nei[0], nei[1], nei[2], nei[3])
        if val_nei == '#':
            cpt_active += 1

    return cpt_active

def neighboursFromDist(x, y, z, w, dist_max) :
    x_min, x_max = x - dist_max, x + dist_max
    y_min, y_max = y - dist_max, y + dist_max
    z_min, z_max = z - dist_max, z + dist_max
    w_min, w_max = w - dist_max, w + dist_max


    list_res = []
    for w_val in range(w_min, w_max + 1):
        for z_val in range(z_min, z_max + 1):
            for y_val in range(y_min, y_max + 1) :
                for x_val in range(x_min, x_max + 1) :
                    if not ((x_val == x) & (y_val == y) & (z_val == z) & (w_val == w)):
                        list_res.append((x_val, y_val, z_val, w_val))
    return list_res

def getAllNeighbour(grid):
    set_res = set()
    for k in tqdm(range(len(grid.keys()))):
        w = list(grid.keys())[k]
        for z in grid[w].keys():
            for y in grid[w][z].keys():
                for x in grid[w][z][y].keys() :
                    set_res = set(set_res | set(neighboursFromDist(x, y, z, w, 1)))

    return set_res

def createSpaceWithActivePoint(list_active_point) :
    x_min, x_max = min(list_active_point,key=itemgetter(0))[0], max(list_active_point,key=itemgetter(0))[0]
    y_min, y_max = min(list_active_point,key=itemgetter(1))[1], max(list_active_point,key=itemgetter(1))[1]
    z_min, z_max = min(list_active_point,key=itemgetter(2))[2], max(list_active_point,key=itemgetter(2))[2]
    w_min, w_max = min(list_active_point,key=itemgetter(3))[3], max(list_active_point,key=itemgetter(3))[3]

    dict_w = dict()
    for w in range(w_min, w_max + 1):
        dict_z = dict()
        for z in range(z_min, z_max + 1) :
            dict_y = dict()
            for y in range(y_min, y_max + 1) :
                dict_x = dict()
                for x in range(x_min, x_max + 1) :
                    if (x, y, z, w) in list_active_point :
                        dict_x[x] = "#"
                    else :
                        dict_x[x] = "."
                dict_y[y] = dict_x
            dict_z[z] = dict_y
        dict_w[w] = dict_z

    return dict_w

def cycle(list_active) :
    space = createSpaceWithActivePoint(list_active)
    #printGridDict(space)
    #print('#####################')

    list_all_nei = list(getAllNeighbour(space))
    list_new_actives = []
    for i in tqdm(range(len(list_all_nei))) :
        elt = list_all_nei[i]
        state = getvaluefromGrid(space, elt[0], elt[1], elt[2], elt[3])
        nb_active = getNeighboursActives(space, elt)
        if state == "." and nb_active == 3 :
            list_new_actives.append(elt)

        if state == "#" and (nb_active == 2 or nb_active == 3):
            list_new_actives.append(elt)

    #space = createSpaceWithActivePoint(list_new_actives)
    #printGridDict(space)
    return list_new_actives


list_active = []
with open('./input.txt') as f:
    y = 0
    for line in f :
        line = line.rstrip()
        for x in range(len(line)) :
            val = line[x]
            if val == "#" :
                list_active.append((x, y, 0, 0))
        y += 1
print(list_active)

for i in range(6):

    print(f'After {i+1} cycle:')
    list_active = cycle(list_active)
    #space = createSpaceWithActivePoint(list_active)
    #printGridDict(space)
    print("###################")

print(len(list_active))
