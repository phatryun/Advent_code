import os

def positionOpenBracket(str_exp):
    nb_close_bracket = 1
    for i in range(len(str_exp)-2, 0, -1) :
        e = str_exp[i]
        if e == ')' :
            nb_close_bracket += 1
        elif e == '(':
            nb_close_bracket -= 1
        if nb_close_bracket == 0 :
            break
    return i+1

def positionCloseBracket(str_exp):
    nb_open_bracket = 1
    for i in range(1, len(str_exp)) :
        e = str_exp[i]
        if e == '(' :
            nb_open_bracket += 1
        elif e == ')':
            nb_open_bracket -= 1
        if nb_open_bracket == 0 :
            break
    return i

def getFreeOp(str_exp) :
    list_op = [i for i in range(len(str_exp)) if str_exp[i] == '+' or str_exp[i] == '*']

    list_bra = [(i,str_exp[i]) for i in range(len(str_exp)) if str_exp[i] == '(' or str_exp[i] == ')' ]

    l_open_bra = []
    res_2 = []
    for elt in list_bra :
        if elt[1] == '(':
            l_open_bra.append(elt[0])
        else :
            res_2.append((l_open_bra[-1], elt[0]))
            del l_open_bra[-1]

    list_free_op = []
    for op in list_op :
        free_op = True
        for bra in res_2 :
            if bra[0] < op < bra[1]:
                free_op = False

        if free_op :
            list_free_op.append(op)

    return list_free_op

class Expression :

    def __init__(self, str_exp):
        #print(f'{str_exp}')
        if str_exp.isnumeric() :
            self.op = '='
            self.left = int(str_exp)
        else :
            free_op = getFreeOp(str_exp)
            if len(free_op) > 0 :
                self.op = str_exp[max(free_op)]
                self.left = Expression(str_exp[:max(free_op) - 1])
                self.right = Expression(str_exp[max(free_op) + 2:])
            else :
                self.op = '()'
                self.left = Expression(str_exp[1:-1])


    def printPreFix(self) :
        if self.op == '=' :
            return f'{self.left}'
        elif self.op == '()' :
            return f' ( {self.left.printPreFix()} )'
        else :
            return f'{self.op} {self.left.printPreFix()} {self.right.printPreFix()}'

    def eval(self):
        if self.op == '=' :
            return self.left
        elif self.op == '()' :
            return self.left.eval()
        elif self.op == '+' :
            return self.left.eval() + self.right.eval()
        elif self.op == '*' :
            return self.left.eval() * self.right.eval()


with open('./input.txt') as f:
    list_e = [line.rstrip() for line in f]


'''list_e = [
    '1 + 2 * 3 + 4 * 5 + 6',
    '1 + (2 * 3) + (4 * (5 + 6))',
    '2 * 3 + (4 * 5)',
    '5 + (8 * 3 + 9 + 3 * 4 * 3)',
    '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
    '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
]
'''

cpt = 0
for str_e in list_e:
    e = Expression(str_e)
    #print(f'{e.printPreFix()}')
    #print(f'{str_e} = {e.eval()}')
    cpt += e.eval()

print(cpt)

'''
next_op = [i for i in range(len(str_exp)) if str_exp[i] == '+' or str_exp[i] == '*']
print(next_op)
if str_exp[-1] == ')' :
    i = positionOpenBracket(str_exp)
    print(str_exp[i])
    next_op = [x for x in next_op if x < i]
    print(next_op)
    if len(next_op) == 0 :
        print(f'op : ()')
        print(f'left : {str_exp[i-1:-1]}')
    else :
        y = max(next_op)
        print(f'op : {str_exp[y]}')
        print(f'left : {str_exp[:max(next_op) - 1]}')
        print(f'left : {str_exp[max(next_op) + 2:]}')
'''

"""
            next_op = [i for i in range(len(str_exp)) if str_exp[i] == '+' or str_exp[i] == '*']

            if str_exp[0] == '(' :
                i_close_bra = positionCloseBracket(str_exp)
                if i_close_bra > max(next_op) :
                    self.op = '()'
                    self.left = Expression(str_exp[1:i_close_bra])
                else :
                    self.op = str_exp[max(next_op)]
                    self.left = Expression(str_exp[:max(next_op) - 1])
                    self.right = Expression(str_exp[max(next_op) + 2:])
            elif str_exp[-1] == ')' :
                i_open_bra = positionOpenBracket(str_exp)
                next_op = [x for x in next_op if x < i_open_bra]
                if len(next_op) == 0 :
                    self.op = '()'
                    self.left = Expression(str_exp[1:-1])
                else :
                    self.op = str_exp[max(next_op)]
                    self.left = Expression(str_exp[:max(next_op) - 1])
                    self.right = Expression(str_exp[max(next_op) + 2:])

            else :
                self.op = str_exp[max(next_op)]
                self.left = Expression(str_exp[:max(next_op) - 1])
                self.right = Expression(str_exp[max(next_op) + 2:])

"""
