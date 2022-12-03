

list_ingre = []
list_aller = []
dict_aller_possibilities = dict()
dict_ingre = dict()
y = 0
with open('./input.txt') as f:
    for line in f :
        line = line.rstrip()
        if '(contains' in line:
            ingre, aller = line.split('(contains ')
            tmp_ingre = ingre.split(' ')[:-1]
            for elt in tmp_ingre:
                if elt in dict_ingre.keys():
                    tmp = dict_ingre[elt]
                    tmp['occurence'] += 1
                    dict_ingre[elt] = tmp
                else :
                    tmp = {'occurence':1, 'aller':[]}
                    dict_ingre[elt] = tmp

            tmp_aller = aller[:-1].split(', ')
            list_ingre.append(tmp_ingre)
            list_aller.append(tmp_aller)
            for elt in tmp_aller :
                if elt in dict_aller_possibilities.keys():
                    dict_aller_possibilities[elt] = dict_aller_possibilities[elt] + tmp_ingre
                else :
                    dict_aller_possibilities[elt] = tmp_ingre
        else :
            list_ingre.append(line.split(' ')[:-1])
            list_aller.append([])

#print(list_ingre)
#print(dict_ingre)
#print(dict_aller_possibilities)

def countEltInList(allergen, list_elt):
    count_ing = [(x,list_elt.count(x)) for x in set(list_elt)]
    count_ing = sorted(count_ing, key = lambda x: x[1], reverse=True)
    max_ing = max(count_ing, key= lambda x: x[1])[1]
    res = []
    for e in count_ing :
        if e[1] == max_ing:
            if len(dict_ingre[e[0]]['aller']) == 0 :
                dict_ingre[e[0]]['aller'] = [allergen]
            res.append(e[0])
                #break

    ##print(max_res)
    return res

dict_allergene = dict()
for allergen in dict_aller_possibilities.keys():
    list_elt = countEltInList(allergen, dict_aller_possibilities[allergen])
    dict_allergene[allergen] = list_elt
    print(f'{allergen} : {list_elt}')

cpt = 0
list_res = []
for elt in dict_ingre.keys() :
    if len(dict_ingre[elt]['aller']) == 0 :
        cpt += dict_ingre[elt]['occurence']
    else :
        list_res.append((elt, dict_ingre[elt]['aller'][0]))

#should be 1679
print(f'Part I : {cpt}')


def getProductAllergene(dict_allergene):
    res = 1
    sort_list_key = []
    for key, val in dict_allergene.items() :
        res *= len(val)
        sort_list_key.append((key, len(val)))
    sort_list_key = sorted(sort_list_key, key = lambda x: x[1])
    return res, sort_list_key

def deleteIngrFormList(list_ingr, list_ingr_ok):
    list_res = []
    for elt in list_ingr :
        if not elt in list_ingr_ok :
            list_res.append(elt)

    return list_res

list_ingr_ok = []

nb_ingr_per_aller, list_nb_ingr_aller = getProductAllergene(dict_allergene)

i=1
while nb_ingr_per_aller > 1:
    for elt, nb in list_nb_ingr_aller :
        if nb > 1 :
            dict_allergene[elt] = deleteIngrFormList(dict_allergene[elt], list_ingr_ok)

        if nb == 1 :
            list_ingr_ok.append(dict_allergene[elt][0])

        nb_ingr_per_aller, list_nb_ingr_aller = getProductAllergene(dict_allergene)

    list_ingr_ok = list(set(list_ingr_ok))
    i += 1

ist_res = [(key, val[0]) for key, val in dict_allergene.items()]
list_res = sorted(list_res, key = lambda x: x[0])
list_res = [elt[1] for elt in list_res]
print(f"Part II : {','.join(list_res)}")

