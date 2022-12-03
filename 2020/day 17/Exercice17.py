import os
from operator import itemgetter


# def listCopy(list_input) :
#     res_input = []
#     for y in range(len(list_input)) :
#         line = []
#         for x in range(len(list_input[y])) :
#             line.append(list_input[y][x])
#         res_input.append(line)
#     return res_input

def printGridDict(grids) :
    for elt in grids.keys():
        print(f'\nz={elt}')
        grid = grids[elt]
        for y in grid.keys() :
            print('|'.join(list(grid[y].values())))

j = 0
dict_y = dict()
list_active = []
with open('./input.txt') as f:
    y = 0
    for line in f :
        line = line.rstrip()
        for x in range(len(line)) :
            val = line[x]
            if val == "#" :
                list_active.append((x, y, 0))
        y += 1
print(list_active)
#grids = dict()
#grids[0] = dict_y
#printGridDict(grids)

def neighboursFromDist(x, y, z, dist_max) :
    x_min, x_max = x - dist_max, x + dist_max
    y_min, y_max = y - dist_max, y + dist_max
    z_min, z_max = z - dist_max, z + dist_max

    list_res = []
    for z_val in range(z_min, z_max + 1):
        for y_val in range(y_min, y_max + 1) :
            for x_val in range(x_min, x_max + 1) :
                if not ((x_val == x) & (y_val == y) & (z_val == z)):
                    list_res.append((x_val, y_val, z_val))
    return list_res

def getvaluefromGrid(grid, x, y, z):
    if z in grid.keys() :
        if y in grid[z].keys():
            if x in grid[z][y].keys() :
                return grid[z][y][x]

    return "."

def getNeighboursActives(grid, elt) :

    list_neighbours = neighboursFromDist(elt[0], elt[1], elt[2], 1)

    cpt_active = 0
    for nei in list_neighbours :
        val_nei = getvaluefromGrid(grid, nei[0], nei[1], nei[2])
        if val_nei == '#':
            cpt_active += 1

    return cpt_active

#getNeighboursActives(grids, 0, 0, 0)

def createSpaceWithActivePoint(list_active_point) :
    x_min, x_max = min(list_active_point,key=itemgetter(0))[0], max(list_active_point,key=itemgetter(0))[0]
    y_min, y_max = min(list_active_point,key=itemgetter(1))[1], max(list_active_point,key=itemgetter(1))[1]
    z_min, z_max = min(list_active_point,key=itemgetter(2))[2], max(list_active_point,key=itemgetter(2))[2]

    dict_z = dict()
    for z in range(z_min, z_max + 1) :
        dict_y = dict()
        for y in range(y_min, y_max + 1) :
            dict_x = dict()
            for x in range(x_min, x_max + 1) :
                if (x, y, z) in list_active_point :
                    dict_x[x] = "#"
                else :
                    dict_x[x] = "."
            dict_y[y] = dict_x
        dict_z[z] = dict_y

    return dict_z

def getAllNeighbour(grid):
    set_res = set()
    for z in grid.keys():
        for y in grid[z].keys():
            for x in grid[z][y].keys() :
                set_res = set(set_res | set(neighboursFromDist(x, y, z, 1)))

    return set_res

def cycle(list_active) :
    space = createSpaceWithActivePoint(list_active)
    #printGridDict(space)
    #print('#####################')
    list_all_nei = getAllNeighbour(space)
    list_new_actives = []
    for elt in list_all_nei :
        state = getvaluefromGrid(space, elt[0], elt[1], elt[2])
        nb_active = getNeighboursActives(space, elt)
        if state == "." and nb_active == 3 :
            list_new_actives.append(elt)

        if state == "#" and (nb_active == 2 or nb_active == 3):
            list_new_actives.append(elt)

    #space = createSpaceWithActivePoint(list_new_actives)
    #printGridDict(space)
    return list_new_actives

for i in range(6):

    print(f'After {i+1} cycle:')
    list_active = cycle(list_active)
    #space = createSpaceWithActivePoint(list_active)
    #printGridDict(space)
    print("###################")

print(len(list_active))
