import os
import numpy as np


def createListFromField(str_field_ind) :
    if 'or' in str_field_ind :
        str_split = str_field_ind.split(' or ')
    else :
        str_split = [str_field_ind]

    res = []
    for elt in str_split :
        if '-' in elt :
            elt_split = [int(e) for e in elt.split('-')]
            for j in range(elt_split[0], elt_split[1] + 1):
                res.append(j)
        else :
            res.append(int(elt))
    return res

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

split = indices = [i for i, x in enumerate(lines) if x == ""]
#print(split)

#fields
dict_fields = dict()
for i in range(0,split[0]):
    field = lines[i].split(': ')
    dict_fields[field[0]] = createListFromField(field[1])

#print(dict_fields)

#my ticket
my_ticket = [int(elt) for elt in lines[split[0] + 2].split(',')]
#print(my_ticket)

#nearby ticket
list_nearby_ticket = []
for i in range(split[1] + 2, len(lines)):
    list_nearby_ticket.append([int(elt) for elt in lines[i].split(',')])

#print(list_nearby_ticket)

print('Part 1')

list_valid = []
for key in dict_fields.keys():
    list_valid += dict_fields[key]

list_valid = list(set(list_valid))


valid_ticket = []
for e in my_ticket :
    valid_ticket.append([])

#get valid and invalid tickets
invalid_number = []
for ticket in list_nearby_ticket :
    ticket_ok = True
    for val in ticket :
        if not val in list_valid :
            invalid_number.append(val)
            ticket_ok = False
    if ticket_ok :
        for i in range(len(ticket)):
            valid_ticket[i].append(ticket[i])

print(f'invalid_number {invalid_number} ==> {sum(invalid_number)}')

print(valid_ticket)


list_field_poss = []
for list_elt in valid_ticket :
    res = []
    for key in dict_fields.keys():
        list_elt_not_in_field = np.setdiff1d(list_elt, dict_fields[key])
        if len(list_elt_not_in_field) == 0:
            res.append(key)
    list_field_poss.append(res)

print(list_field_poss)

field_took = []

while len(field_took) < len(dict_fields.keys()) :
    #print(f'field_took : {field_took}')
    for list_elt in list_field_poss :
        if len(list_elt) == 1 :
            field_took.append(list_elt[0])
        elif len(list_elt) > 1 :
            for e in np.intersect1d(field_took, list_elt) :
                list_elt = list_elt.remove(e)
    field_took = list(set(field_took))

#print(field_took)
print(list_field_poss)

res = 1
for i in range(len(list_field_poss)):
    if list_field_poss[i][0].startswith('departure') :
        res *= my_ticket[i]

print(f'Part 2 : {res}')
