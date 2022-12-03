from tqdm import tqdm

class Elt:
    def __init__(self, val, pred, succ) :
        self.val = val
        self.pred = pred
        self.succ = succ

str_clock = '389125467'
#str_clock = '974618352'
list_clock = [int(elt) for elt in str_clock]

#for i in range(max(list_clock)+1, 1000001):
#    list_clock.append(i)


def buildLinkArray(list_elt):
    elt = Elt(list_elt[0], None, None)
    first = elt

    for i in list_elt[1:] :
        next_elt = Elt(i, elt, None)
        elt.succ = next_elt
        elt = next_elt

    elt.succ = first
    first.pred = elt

    return first

def findDestination(list_elt, current) :
    destination = current - 1
    while True :
        try :
            if destination < min(list_elt) :
                destination = max(list_elt)
            i_destination = list_elt.index(destination)
            break
        except :
            destination -= 1
    return i_destination

current = buildLinkArray(list_clock)

for i in tqdm(range(1, 2)) :
    print(f'######## move {i} ##############')
    next_1 = current.succ
    next_2 = next_1.succ
    next_3 = next_2.succ
    next_4 = next_3.succ

    current.succ = next_3.succ
    next_4.pred = current
    

# for i in tqdm(range(1, 10000001)):
#     #print(f'######## move {i} ##############')
#     #print(f'list_clock : {list_clock}')
#     new_clock = list_clock[i_current:] + list_clock[:i_current]
#     s1 = ",".join([str(c) for c in new_clock])
#     if s1 in previous_clock :
#         print('loop !')
#         break
#     previous_clock.add(s1)

#     current = new_clock[0]
#     #print(f'current : {current}')
#     pick_up = [new_clock.pop(1), new_clock.pop(1), new_clock.pop(1)]
#     #print(f'pick_up : {pick_up}')
#     i_destination = findDestination(new_clock, current)
#     #print(f'i_destination : {i_destination}')
#     new_clock[i_destination+1:i_destination+1] = pick_up

#     list_clock = new_clock
#     i_current = 1#(i_current + 1) % len(list_clock)

# if i != 10000000 :
#     list_clock = previous_clock[10000000 % i]

# one_position = list_clock.index(1)
# list_res = list_clock[one_position:] + list_clock[:one_position]
# #print(f'Part I : {"".join([str(e) for e in list_res[1:]])}')

# print(f'Part II : {list_res[1] * list_res[2]}')
