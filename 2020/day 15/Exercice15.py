import os
from tqdm import tqdm


def getXvalFromElvesGame(list_start, x_max):

    list_move = list_start[:]
    dict_last_spoke = dict()

    #initialisation
    for i in range(len(list_move)-1) :
        dict_last_spoke[list_move[i]] = i + 1


    for i in tqdm(range(len(list_move), x_max)):
        val = list_move[i-1]
        val_to_append = 0
        if val in dict_last_spoke.keys() :
            previous = dict_last_spoke[val]
            #print(f' i - previous = {i} - {previous} = {i - previous}')
            val_to_append = i - previous

        list_move.append(val_to_append)
        dict_last_spoke[val] = i
        #print(f'{i+1}, -> {val} -> {val_to_append}')

    return list_move, dict_last_spoke

l =[0,3,6]

#res, dict_last_spoke = getXvalFromElvesGame(l, 30000000)
#print(f'{l} = {res[-1]}')

'''print(res)
print('###')
print(dict_last_spoke)
print('###')
print(dict_last_spoke.keys())


dict_test = dict()
i = 1
for elt in res :
    if elt in dict_test.keys() :
        dict_test[elt] = dict_test[elt] + [i]
    else:
        dict_test[elt] = [i]
    i += 1


print('####')
print(dict_test)'''

'''
l =[1,3,2]
print(f'{l} = {getXvalFromElvesGame(l, 2020)}')

l =[2,1,3]
print(f'{l} = {getXvalFromElvesGame(l, 2020)}')

l =[1,2,3]
print(f'{l} = {getXvalFromElvesGame(l, 2020)}')

l =[2,3,1]
print(f'{l} = {getXvalFromElvesGame(l, 2020)}')

l =[3,2,1]
print(f'{l} = {getXvalFromElvesGame(l, 2020)}')

l =[3,1,2]
print(f'{l} = {getXvalFromElvesGame(l, 2020)}')

l = [11,18,0,20,1,7,16]
print(f'{l} = {getXvalFromElvesGame(l, 2020)}')
'''

l = [11,18,0,20,1,7,16]

res, dict_last_spoke = getXvalFromElvesGame(l, 2020) #30000000)
print(f'{l} = {res[-1]}')
