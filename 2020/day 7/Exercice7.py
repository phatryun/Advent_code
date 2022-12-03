import os

def getColorValue(str_input, node=True) :
    return_value = str_input[:]

    return_value = str_input.replace(' bags', '')
    return_value = return_value.replace(' bag', '')

    return_value = return_value.replace('.', '')

    if return_value == 'no other' :
        return None
    i_blank = return_value.find(' ')
    nb_bag = 1
    if return_value[:i_blank].isnumeric() :
        nb_bag = int(return_value[:i_blank])
        return_value = return_value[i_blank + 1:]

    if node :
        return return_value #, nb_bag
    else :
        return return_value , nb_bag


def getNodeFromColor(bags, color):
    if not color in bags.keys() :
        return []
    else :
        res = []#[color]
        for c in bags[color] :
            res += [c] + getNodeFromColor(bags, c)
        return res

with open('day 7/input.txt') as f:
    lines = [line.rstrip() for line in f]

dict_bags = dict()
dict_bags_contains = dict()
for line in lines :
    #print(line)
    node, leafs = line.split(' contain ')

    #Node value
    node = getColorValue(node)

    #contains
    list_leaf = leafs.split(', ')
    list_sub_bags = []
    for elt in list_leaf :
        #1st part
        bag_color = getColorValue(elt)
        if bag_color != None :
            if bag_color in dict_bags.keys() :
                #list_node = dict_bags[bag_color]
                #list_node.append(node)
                #dict_bags[bag_color] = list_node
                dict_bags[bag_color].append(node)
            else :
                dict_bags[bag_color] = [node]

        #2nd part
        bag_tuple = getColorValue(elt, node=False)
        if bag_tuple != None :
            list_sub_bags.append(bag_tuple)
    if node in dict_bags_contains.keys():
        print('hey problem varme!!')
    dict_bags_contains[node] = list_sub_bags

shiny_gold_bags = set(getNodeFromColor(dict_bags, 'shiny gold'))
print(f'Part 1 : {len(shiny_gold_bags)} ') #-> {shiny_gold_bags}')

def getNbBagInside(dict_bags_contains, color, weight):
    #print(f'{color} -> {weight}')
    #print(f'## { dict_bags_contains[color]}')

    bags = dict_bags_contains[color]
    if len(bags) == 0 :
        return weight
    else :
        res = weight
        for c, w in bags :
            res += weight * getNbBagInside(dict_bags_contains, c, w)
            #print(res)
        return res

print(f'Part 2 : {getNbBagInside(dict_bags_contains, "shiny gold", 1) - 1}')
