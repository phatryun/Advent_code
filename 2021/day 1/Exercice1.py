import os
import numpy as np

with open('day 1/input_1.txt') as f:
    lines = [int(line.rstrip()) for line in f]

array_lines = np.array(lines)

print('## Excercice 1')
nb_increase = 0
## Excercice 1
for i in range(len(array_lines) - 1):
    current = array_lines[i]
    next = array_lines[i+1]
    if next > current:
        nb_increase += 1
print(f"nb_increase: {nb_increase}")

print('## Excercice 2')
## Exercice 2
nb_increase = 0
for i in range(len(array_lines) - 1 - 2):

    first_windows = array_lines[i:i+3]
    second_windows = array_lines[(i+1):(i+1)+3]

    # print(f"{first_windows} vs {second_windows} -> {first_windows.sum()} vs {second_windows.sum()}")
    if second_windows.sum() > first_windows.sum():
        nb_increase += 1

print(f"nb_increase: {nb_increase}")