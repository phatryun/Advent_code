import os
import numpy as np
import pandas as pd

col_names = ['pwd_policy', 'letter', 'pwd']
df = pd.read_csv('./day 2/input.txt', sep=' ', header=None, names=col_names)

def pwd_ok_1(row):
    min_l, max_l = row['pwd_policy'].split('-')
    letter = row['letter'][:1]
    count_l = row['pwd'].count(letter)
    if (count_l >= int(min_l)) & (count_l <= int(max_l)) :
        return 1
    return 0

def pwd_ok_2(row):
    min_l, max_l = row['pwd_policy'].split('-')
    letter = row['letter'][:1]
    pwd = row['pwd']
    cpt = 0
    if pwd[int(min_l) - 1 ] == letter : cpt += 1
    if pwd[int(max_l) - 1 ] == letter : cpt += 1

    if cpt == 1 :
        return 1
    return 0



df['pwd_is_ok_1'] = df.apply(pwd_ok_1, axis=1)
df['pwd_is_ok_2'] = df.apply(pwd_ok_2, axis=1)



print(df.head())

print(f'1 : nb password ok : {df.pwd_is_ok_1.sum()}')
print(f'2 : nb password ok : {df.pwd_is_ok_2.sum()}')
