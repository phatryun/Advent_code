import os


with open('day 6/input.txt') as f:
    lines = [line.rstrip() for line in f]

dict_group = dict()
i = 1
list_answer = []
cpt_anyone = 0
cpt_evryone = 0

for line in lines :
    if line == "":
        #distinct answer
        set_answer = set([j for i in list_answer for j in i])
        nb_anyone_answer = len(set_answer)
        cpt_anyone += nb_anyone_answer

        #intersection answer
        set_intersetion = set.intersection(*[set(x) for x in list_answer])
        nb_evryone_answer = len(set_intersetion)
        cpt_evryone += nb_evryone_answer

        dict_group[f'group_{i}'] = (list_answer, nb_anyone_answer, nb_evryone_answer)

        i += 1
        list_answer = []
    else :
        list_tmp = []
        list_tmp[:0]=line
        list_answer.append(list_tmp)

print(dict_group['group_1'])
print(dict_group['group_2'])

print(f'cpt_anyone : {cpt_anyone}')
print(f'cpt_evryone : {cpt_evryone}')



test = [['a'], ['x', 'f', 'k', 'j'], ['x', 'f', 'b']]
res = set.intersection(*[set(x) for x in test])
print(len(res))
