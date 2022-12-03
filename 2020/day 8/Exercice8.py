import os

with open('day 8/input.txt') as f:
    lines = [line.rstrip() for line in f]

list_iter = [0] * (len(lines)+1)

def runCode(list_instruction, list_loop) :
    i = 0
    acc = 0
    while (i >= 0) & (i < len(list_instruction)) :
        if list_loop[i] == 1 :
            break
        #get action
        act, num = list_instruction[i].split(' ')

        # save iteration
        list_loop[i] = 1

        if act == 'nop' :
            i += 1
        elif act == 'acc' :
            i += 1
            acc += int(num)
        elif act == 'jmp' :
            i += int(num)

    return {'i':i, 'acc':acc}

## first part
print(f'part 1 {runCode(lines, list_iter)}')


## Second part
j_iter = 0
res = dict()
while j_iter < len(lines) :

    code = lines[:]
    list_iter = [0] * (len(lines)+1)

    act, num = code[j_iter].split(' ')
    if act == 'acc' :
        j_iter += 1
        continue
    if act == 'nop' :
        code[j_iter] = f'jmp {num}'
    elif act == 'jmp' :
        code[j_iter] = f'nop {num}'

    res = runCode(code, list_iter)
    #print(f'j_iter = {j_iter} ## {res}')
    if res['i'] == len(code) :
        #print('super')
        break

    j_iter += 1

print(f'part 2 {res}')
