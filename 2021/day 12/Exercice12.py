import os
import numpy as np
from tqdm import tqdm
from collections import Counter

def add_path(dict_path, _from, _where):

    if _from != 'end' and _where != 'start':
        if _from in dict_path.keys():
            dict_path[_from].append(_where)
        else:
            dict_path[_from] = [_where]

    return dict_path

def split_data(str_file_path):

    with open(str_file_path) as f:
        lines = [ line.rstrip().split('-') for line in f]

    # res = [[e.split(' ') for e in elt] for elt in lines]

    # print(lines)

    dict_links = {}

    for _from, _where in lines:
        dict_links = add_path(dict_links, _from, _where)
        dict_links = add_path(dict_links, _where, _from)

    return dict_links

    # return draw_numbers, list_bigo_grid


def get_path(dict_links, start, actual_path, dict_visit, limit=1):

    # print(f"{start}, {dict_links} -- {actual_path}")

    dict_links2 = dict_links.copy()
    tmp_dict_visit = dict_visit.copy()

    tmp_dict_visit[start] += 1
    actual_path.append(start)

    if start not in dict_links2.keys():
        return [actual_path]

    paths = dict_links2[start]
 
    next_limit = limit
    max_small = max([val for key, val in tmp_dict_visit.items() if (key.islower()) and (key not in ['start', 'end'])])
    if max_small == limit:
        next_limit = 1

    res = []
    for elt in paths:
        if elt.islower():
            # print(f"start {start}: {tmp_dict_visit}")
            if tmp_dict_visit[elt] < next_limit:
                tmp = actual_path.copy()
                res += get_path(dict_links2, elt, tmp, tmp_dict_visit, limit=next_limit)
        else:
            tmp = actual_path.copy()
            res += get_path(dict_links2, elt, tmp, tmp_dict_visit, limit=next_limit)
    return res



def part_1(data):
    """
    """

    print(data)

    visits = {e:0 for e in data.keys()}# if e.islower()}
    visits['end'] = 0
    print(visits)
        
    res = get_path(data, 'start', [], visits)
    #print(len(res))
    res = [elt for elt in res if elt[0] == 'start' and elt[-1] == 'end']

    print(len(res))
    # for elt in res:
    #     print(elt)
    return True


def part_2(data):
    """
    """

    print(data)
    visits = {e:0 for e in data.keys()}# if e.islower()}
    visits['end'] = 0
    print(visits)

    res = get_path(data, 'start', [], visits, limit=2)
    #print(len(res))

    res = [elt for elt in res if elt[0] == 'start' and elt[-1] == 'end']
    #for elt in res:
    #    print(elt)
    print(len(res))
    
    return True


if __name__ == "__main__":

    day = 12
    ex = "" # "_ex" # "" #

    data = split_data(f'input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)
    
    # Exercice 2
    print('## Excercice 2')
    part_2(data)
