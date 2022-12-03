import os

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]


time_arrived = int(lines[0])

shuttle_start = lines[1].split(',')

### Part 1 ####
#waiting_time = []
#bus_time = []
min_waiting = time_arrived
res = 0
bus_num = 0
for start in shuttle_start :
    if start != 'x':
        time_start = int(start)
        #bus_time.append(start)
        #waiting_time.append(time_start - (time_arrived % time_start))
        time_next_D = time_start - (time_arrived % time_start)
        if min_waiting > time_next_D :
            #print(f'{start} : {time_next_D}')
            min_waiting = time_next_D
            res = time_next_D * time_start
            bus_num = time_start


print(f'Part 1 : Bus num: {bus_num}, next_D : {min_waiting}, res : {res} ')


### Part 2 ####

# y * b - i = z * c - j
def isNumberOk(y, b, i, z, j) :
    c = -1
    if (y * b - i + j) % z == 0 :
        c = int((y * b - i + j) / z)

    return c


def GetBestTimeStamp(str_bus):

    shuttle_start = str_bus.split(',')

    shuttle_start =[int(elt) if elt != 'x' else 0 for elt in shuttle_start ]

    #print(shuttle_start)
    max_bus = max(shuttle_start)
    i_max_bus = shuttle_start.index(max_bus)
    #print(f'{max_bus} = {i_max_bus}')


    b = 1 #100000000000000 // max_bus
    while True :
        #if b % 10000 == 0 :
        #    print(b)
        #print(f'TimeStamp : {max_bus * b}')
        ok = True
        for i in range(len(shuttle_start)) :
            if shuttle_start[i] > 0 :
                c = isNumberOk(max_bus, b, i_max_bus,
                                shuttle_start[i], i)
                if c > 0 :
                    #print(c)
                    ok *= True
                else :
                    ok *= False
                    continue
        if ok :
            #print(f'TimeStamp : {max_bus * b - i_max_bus}')
            break

        b += 1

    return max_bus * b - i_max_bus

example_1 = '7,13,x,x,59,x,31,19'
example_2 = '17,x,13,19'
example_3 = '67,7,59,61'
example_4 = '67,x,7,59,61'
example_5 = '67,7,x,59,61'
example_6 = '1789,37,47,1889'

example = lines[1]

'''
res_2 = GetBestTimeStamp(example_2)
print(f'{example_2} : {res_2}')

res_3 = GetBestTimeStamp(example_3)
print(f'{example_3} : {res_3}')

res_4 = GetBestTimeStamp(example_4)
print(f'{example_4} : {res_4}')

res_5 = GetBestTimeStamp(example_5)
print(f'{example_5} : {res_5}')

res_6 = GetBestTimeStamp(example_6)
print(f'{example_6} : {res_6}')

print(example)
res = GetBestTimeStamp(example)
print(f'{example} : {res}')
'''

from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def part2(str_buses):
    buses = [(i, int(bus)) for i, bus in enumerate(str_buses.split(',')) if bus != 'x']
    dividers = [bus for _, bus in buses]
    remainders = [bus - i for i, bus in buses]

    return chinese_remainder(dividers, remainders)

print(f'Part 2: {part2(example_2)}')

