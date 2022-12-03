import os

def GetValueWithInitialisation(mask, binval) :
    res = []
    for x in range(len(mask)):
        mask_char = mask[x]
        if mask_char == 'X' :
            res.append(binval[x])
        else:
            res.append(mask[x])

    res = ''.join(res)
    return int(res, 2)

dict_mask = dict()
list_mem = []
i_mask = 0
with open('./input.txt') as f:
    for line in f :
        l = line.rstrip().split(' = ')
        if l[0] == "mask" :
            i_mask += 1
            dict_mask[i_mask] = l[1]
        else :
            list_mem.append((i_mask, int(l[0][4:-1]), int(l[1])))


#print(dict_mask)
#print(list_mem)

dict_mem = dict()
for i_mask, mem_addr, mem_val in list_mem :
    mem_bin = "{0:036b}".format(mem_val)
    res = GetValueWithInitialisation(dict_mask[i_mask], mem_bin)
    dict_mem[mem_addr] = res

#print(dict_mem)
print(f'Part 1 : {sum(dict_mem.values())}')

def getFirstXforStr(str_val):
    res = -1
    for i in range(0, len(str_val)) :
        if str_val[i] == 'X' :
            return i

    return res

def replaceXinBin(mask):
    i_x = getFirstXforStr(mask)
    if i_x < 0 :
        return [mask]
    else :
        mask_1, mask_0 = mask[:], mask[:]
        mask_1[i_x] = '1'
        mask_0[i_x] = '0'
        #print(f'mask_1 : {mask_1}')
        #print(f'mask_0 : {mask_0}')
        return replaceXinBin(mask_1) + replaceXinBin(mask_0)


def GetValueWithInitialisation2(mask, binval) :
    res = []
    for x in range(len(mask)):
        mask_char = mask[x]
        if mask_char == '0' :
            res.append(binval[x])
        elif mask_char == '1' :
            res.append('1')
        else:
            res.append('X')

    res = ''.join(res)
    return res

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

dict_mem = dict()
for i_mask, mem_addr, mem_val in list_mem :
    mem_addr_bin = "{0:036b}".format(mem_addr)
    mem_addr_floating = Convert(GetValueWithInitialisation2(
                                    dict_mask[i_mask],
                                    mem_addr_bin))
    #print(''.join(mem_addr_floating))
    list_mem_addr = replaceXinBin(mem_addr_floating)
    for elt in list_mem_addr :
        int_addr = int(''.join(elt), 2)
        #print(int_addr)
        dict_mem[int_addr] = mem_val


#print(dict_mem)
print(f'Part 2 : {sum(dict_mem.values())}')
