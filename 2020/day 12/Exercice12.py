import os
import math

def GetCardinalFromCoord(boat_dir):
    x = boat_dir[0]
    y = boat_dir[1]
    if x == 1 and y == 0 :
        return 'E'
    elif x == -1 and y == 0 :
        return 'W'
    elif x == 0 and y == 1:
        return 'N'
    elif x == 0 and y == -1 :
        return 'S'
    else :
        return 'errror'


def GetCoodAfterRotation(cood, dir_rot, val_rot):
    Pi_quot = val_rot / 180
    if dir_rot == 'R':
        Pi_quot *= -1
    #print(Pi_quot)
    x = round(cood[0] * math.cos(math.pi * Pi_quot) - cood[1] * math.sin(math.pi * Pi_quot),0)
    y = round(cood[1] * math.cos(math.pi * Pi_quot) + cood[0] * math.sin(math.pi * Pi_quot),0)

    return (x, y)

def rotationWayPoint(waypoint, rotation) :
    res = waypoint.copy()
    wise = rotation[0]
    nb_rotation = int(rotation[1:]) // 90
    #print(f'wize {wise}')
    #print(f'nb_rotation {nb_rotation}')
    #print(f'res : {res}')

    if wise == 'R':
        for i in range(nb_rotation):
            #print(f'#### {i} #####')
            res['S'] = waypoint['E']
            res['W'] = waypoint['S']
            res['N'] = waypoint['W']
            res['E'] = waypoint['N']

            waypoint = res.copy()
            #print(f' res : {res}')
            #print(f' waypoint : {waypoint}')

    else :
        for i in range(nb_rotation):
            res['E'] = waypoint['S']
            res['N'] = waypoint['E']
            res['W'] = waypoint['N']
            res['S'] = waypoint['W']
            waypoint = res.copy()

    return res

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

#Part 1
print(lines[:10])
boat_dir = (1,0) #East
dict_direction = {'E':0,
                  'N':0,
                  'W':0,
                  'S':0}

for line in lines :
    inst_dir = line[0]
    inst_val = int(line[1:])
    if inst_dir in ['E','N','W','S'] :
        dict_direction[inst_dir] += inst_val
    elif inst_dir == 'F' :
        cardinal_dir = GetCardinalFromCoord(boat_dir)
        dict_direction[cardinal_dir] += inst_val
    elif inst_dir == 'R' or inst_dir == 'L' :
        boat_dir = GetCoodAfterRotation(boat_dir, inst_dir, inst_val)
        #print(f'{line} => {boat_dir} : {GetCardinalFromCoord(boat_dir)}')
    else :
        print(line)

print(dict_direction)
res = abs(dict_direction['N'] - dict_direction['S']) + abs(dict_direction['E'] - dict_direction['W'])
print(f'Part 1 : {res}')

### Part 2
print(lines[:10])
boat_waypoint = {'E':10,
                  'N':1,
                  'W':0,
                  'S':0}

boat_position = {'E':0,
                  'N':0,
                  'W':0,
                  'S':0}

for line in lines :
    inst_dir = line[0]
    inst_val = int(line[1:])
    if inst_dir in ['E','N','W','S'] :
        boat_waypoint[inst_dir] += inst_val
        #print(f'{line} => boat_waypoint : {boat_waypoint} ')
    elif inst_dir == 'F' :
        for dir_boat in boat_position.keys() :
            boat_position[dir_boat] += boat_waypoint[dir_boat] * inst_val
        #print(f'{line} => boat_position : {boat_position} ')
    elif inst_dir == 'R' or inst_dir == 'L' :
        boat_waypoint = rotationWayPoint(boat_waypoint, line)
        #print(f'{line} => boat_waypoint : {boat_waypoint} ')
    else :
        print(line)

print(boat_position)
res = abs(boat_position['N'] - boat_position['S']) + abs(boat_position['E'] - boat_position['W'])
print(f'Part 2 : {res}')
