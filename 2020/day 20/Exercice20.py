
class Tules :
    def __init__(self, grid) :
        self.id = grid[0].replace('Tile ', '').replace(':', '')

        self.grid = [list(elt) for elt in grid[1:]]

    def printGridParam(self):
        print(self.id)
        for line in self.grid :
            print(''.join(line))

        print(f'N : {self.grid[0][:]}')
        print(f'S : {self.grid[-1][:]}')
        print(f'W : {[elt[0] for elt in self.grid]}')
        print(f'E : {[elt[-1] for elt in self.grid]}')

    def getborders(self, orientation, reverse=False):
        res = []
        if orientation == '-1':
            return (self.grid[0][:],
                    self.grid[-1][:],
                    [elt[0] for elt in self.grid],
                    [elt[-1] for elt in self.grid])
        elif orientation == 'N':
            res = self.grid[0][:]
        elif orientation == 'S':
            res = self.grid[-1][:]
        elif orientation == 'W':
            res = [elt[0] for elt in self.grid]
        elif orientation == 'E':
            res = [elt[-1] for elt in self.grid]

        if reverse :
            res.reverse()

        return res

    def getborderEqual(self, grid_2) :
        orientation = ['N', 'S', 'E', 'W']
        for o1 in orientation :
            # if self.id == '2311' :
            #             print('######')
            #             print(f' -{o1} : {self.getborders(o1, reverse=True)}')
            for o2 in orientation :
                # if self.id == '2311' :
                #         print(f' -{o2} : {grid_2.getborders(o2)}')

                if self.getborders(o1) == grid_2.getborders(o2) :
                    return (self.id, o1), (grid_2.id, o2)
                elif self.getborders(o1, reverse=True) == grid_2.getborders(o2) :
                    #print('vouvou')
                    return (self.id, f'-{o1}'), (grid_2.id, f'{o2}')

        return -1, -1

    def gridRotation(self, nb_quart):
        for i in range(nb_quart):
            res = []
            x_max = len(self.grid)
            for y in range(0, x_max) :
                row = []
                for x in range(x_max-1, -1, -1) :
                    row.append(self.grid[x][y])
                res.append(row)

            self.grid = res


tules = dict()
with open('./input.txt') as f:

    grid = []
    for line in f :
        if line.rstrip() == '':
            tule = Tules(grid)
            tules[tule.id] = tule
            grid = []
        else :
            grid.append(line.rstrip())

tule = Tules(grid)
tules[tule.id] = tule

def findCloseGrid(grid, tules):
    cpt = 0
    list_close_tule = []
    neg_bord = 0
    for id in tules.keys() :
        tule = tules[id]
        if tule.id != grid.id :
            border_eq = grid.getborderEqual(tule)
            if border_eq[0] != -1 :
                 cpt += 1
                 list_close_tule.append(border_eq)
                 if border_eq[0][1][0] == '-':
                    neg_bord += 1

    return cpt, list_close_tule, neg_bord

res = 1
dict_close_tule = dict()
for id in tules.keys() :
    elt = tules[id]
    cpt_elt, list_close_tule, neg_bord = findCloseGrid(elt, tules)
    dict_close_tule[elt.id] = list_close_tule
    #print(f'{elt.id} : {cpt_elt}')
    if cpt_elt == 2 :
        res *= int(elt.id)


print(f'Part 1 : {res}')
#print(dict_close_tule)

# passer le tule en dict
# constuire la grid
# 1951    2311    3079
# 2729    1427    2473
# 2971    1489    1171
'''res_2 = []
for id in dict_close_tule.keys() :
    list_nei = dict_close_tule[id]
    t = tules[id]
    res = []
    for rot in range(0,3) :
        t.gridRotation(rot)
        #t.printGridParam()
        cpt_elt, list_close_tule, neg_bord = findCloseGrid(t, tules)
        #print(f'neg_bord : {neg_bord}')
        #print(f'list_close_tule : {list_close_tule}')
        if neg_bord == 0 :
            res.append(t)
    res_2.append(res)
    #print(len(res))'''

#getborderEqual(self, grid_2

list_res = []
for id in tules.keys() :
    t = tules[id]
    cpt = 0
    for y in range(1,len(t.grid)-1):
        for x in range(1, len(t.grid[y])-1):
            if t.grid[y][x] == '#' :
                cpt += 1

    list_res.append(cpt)

print(list_res)
monster = 15

for i in range(10,20):
    print(f'{i} monster : {sum(list_res) - i * monster}')


# 2 monster : 2392 -> to high
# 9 monster : 2287 -> to high

