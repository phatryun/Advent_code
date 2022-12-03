
# dict_rules = dict()
# dict_overide = dict()
# rules = True
# list_message = []
# with open('./input_example_2.txt') as f:
#     for line in f :
#         if line.rstrip() == "" :
#             rules = False
#         else :
#             if rules :
#                 index, val = line.rstrip().split(': ')
#                 dict_rules[index] = val.replace('"','')
#                 dict_overide[index] = 0
#             else :
#                 list_message.append(line.rstrip().replace('"',''))

# #dict_rules['8'] = '42 | 42 8'
# #dict_rules['11'] = '42 31 | 42 11 31'


# #print(dict_rules)
# print('read message')

# def getpossibilities(dict_rules, val, list_res) :
#     # #print(f'{val} : {list_res}')
#     # for xx in list_val :
#     #     if val in xx :
#     #         list_res = [elt + '*' for elt in list_res]
#     #         print(f'oups : {val}')
#     #         return list_res, list_val

#     # list_val = [elt + " " + val for elt in list_val]

#     if dict_rules[val] == 'a' or dict_rules[val] == 'b' :
#         list_res = [elt + dict_rules[val] for elt in list_res]
#         #print(f'### {list_res} ')

#     else :
#         list_pipe = dict_rules[val].split(' | ')
#         #if len(list_pipe) > 1 :
#         #    print(f'{val}')
#         s = ''
#         list_tmp = list_res[:]
#         # list_tmp_val = list_val[:]
#         list_res = []
#         # list_val = []
#         for pipe in list_pipe :
#             list_tmp_2 = list_tmp[:]
#             # list_tmp_val_2 = list_tmp_val
#             list_value = pipe.split(' ')
#             for v in list_value :
#                 list_tmp_2 = getpossibilities(dict_rules, v, list_tmp_2)

#             list_res += list_tmp_2
#             # list_val += list_tmp_val_2


#     return list_res

# res = ['']
# val = ['']
# res = getpossibilities(dict_rules, '0', res)
# print(res[:5])
# print(val[:5])
# print('get all possibilities')

# dict_possibilities = dict()

# from tqdm import tqdm

# for i in tqdm(range(len(dict_rules.keys()))) :
#     key = list(dict_rules.keys())[i]
#     res = ['']
#     dict_possibilities[key] = getpossibilities(dict_rules, key, res)

# print(f"42 : {dict_possibilities['42']}")
# print(f"31 : {dict_possibilities['31']}")
# print(f'list_message : {len(list_message)}')

# not_ok = []
# cpt_match = 0
# for message in list_message:
#     if message in dict_possibilities['0'] :
#         cpt_match += 1
#         print(f'{message}')
#     else :
#         not_ok.append(message)

# print(cpt_match)
# print(f'not_ok : {len(not_ok)}')

# # # 8 = 42 * 42 * 42
# not_ok_2 = []
# case_42 = dict_possibilities['42']
# for message in not_ok :
#     message_split = [message[index : index + 5] for index in range(0, len(message), 5)]
#     ok = True
#     for m in message_split :
#         if not m in dict_possibilities['42'] :
#             ok = False

#     if ok :
#         cpt_match += 1
#         print(f'{message}')
#     else :
#         not_ok_2.append(message)


# print(cpt_match)
# print(f'not_ok_2 : {len(not_ok_2)}')
# # 11 : 42 11 31 = 42 * (42 * 11 * 31) * 31
# for message in not_ok_2 :
#     message_split = [message[index : index + 5] for index in range(0, len(message), 5)]
#     ok = True
#     if len(message_split) % 2 == 0 :
#         for i in range(1, len(message_split) // 2):
#             if not (message_split[i] in dict_possibilities['42'] and message_split[i*-1] in dict_possibilities['31']) :
#                 ok = False
#     else :
#         ok = False

#     if ok :
#         cpt_match += 1
#         print(f'{message}')

# 11 : 42 11 31 = 42 * (42 * 31 (42 * 31)) * 31
# for message in list_message :
#     for elt_42 in dict_possibilities['42'] :
#         for elt_31 in dict_possibilities['31'] :
#             if len(message) % (len(elt_42)+len(elt_31)) == 0 :
#                 nb_42_31 = len(message) // (len(elt_42)+len(elt_31))
#                 test = ''.join([elt_42 for i in range(nb_42_31)]) + ''.join([elt_31 for i in range(nb_42_31)])
#                 print(f'Assert : {message} == {test}')
#                 if message == test :
#                     print('couhette')
#                     cpt_match += 1
#                     break

# print(cpt_match)
### retourner une liste des toutes les possibilités

# class Rules :

#     def __init__(self, val, dict_rules):
#         if dict_rules[val] == 'a' or dict_rules[val] == 'b' :
#             self.node  = val
#             self.type = 'leaf'
#             self.left = dict_rules[val]
#         else :
#             list_pipe = dict_rules[val].split(' | ')
#             self


def test(s,seq): # can we produce string s using rules list seq?
    if s == '' or seq == []: return s == '' and seq == [] # if both empty, True; if one, False
    r = rules[seq[0]]
    if '"' in r:
        return test(s[1:], seq[1:]) if s[0] in r else False # strip first character, False if cannot
    else:
        return any(test(s, t + seq[1:]) for t in r) # expand first term in seq rules list

def parse(s): # return rule pair (n,e) e.g. (2, [[2,3],[3,2]]) or (42,'"a"')
    n,e = s.split(": ")
    return (int(n),e) if '"' in e else (int(n), [[int(r) for r in t.split()] for t in e.split("|")])

rule_text, messages = [x.splitlines() for x in open("input.txt").read().split("\n\n")]
rules = dict(parse(s) for s in rule_text)
print("Part 1:", sum(test(m,[0]) for m in messages))

rule_text += ["8: 42 | 42 8","11: 42 31 | 42 11 31"]
rules = dict(parse(s) for s in rule_text)
print("Part 2:", sum(test(m,[0]) for m in messages))
