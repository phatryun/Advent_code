import os
import numpy as np

with open('day 10/input.txt') as f:
    lines = [int(line.rstrip()) for line in f]


jolts = 0
jolts_array = np.array(lines)
jolts_max = jolts_array.max()

cpt = [0, 0, 0]
print(f'end : {jolts_max}')

list_add = []
while jolts < jolts_max:
    jolts_tmp = jolts_array[(jolts_array <= jolts + 3) & (jolts_array > jolts)]

    jolts_add = jolts_tmp.min() - jolts
    cpt[jolts_add-1] = cpt[jolts_add-1] + 1

    list_add.append(jolts_add)

    jolts = jolts_tmp.min()

#add last max + 3
cpt[3-1] = cpt[3-1] + 1

print(f'Part 1 : {cpt} -> {cpt[0] * cpt[2]}')

#print(list_add)
cpt_1 = 0
res = 1

tribonacci = [1, 1, 2, 4, 7, 13, 24, 44, 81]

for elt in list_add :
    if elt == 1 :
        cpt_1 += 1
    else :
        res *= tribonacci[cpt_1]
        cpt_1 = 0

res *= tribonacci[cpt_1]

print(f'Part 2 : {res}')
