import os
import numpy as np

import os
import numpy as np


def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [line.rstrip().split(" ") for line in f]

    return np.array(lines)


def part_1(data):
    """
    
    """
    detph = 0
    horizontal = 0

    for i in range(len(data)):
        if data[i][0] == 'down':
            detph += int(data[i][1])
        elif data[i][0] == 'up':
            detph -= int(data[i][1])
        elif data[i][0] == 'forward':
            horizontal += int(data[i][1])
    
    print(detph * horizontal)

    return True


def part_2(data):
    """
    
    """
    # for i in range(len(data)):
    detph = 0
    horizontal = 0
    aim = 0
    for i in range(len(data)):
        if data[i][0] == 'down':
            #detph += int(data[i][1])
            aim += int(data[i][1])
        elif data[i][0] == 'up':
            #detph -= int(data[i][1])
            aim -= int(data[i][1])
        elif data[i][0] == 'forward':
            horizontal += int(data[i][1])
            detph += aim * int(data[i][1])

    print(detph * horizontal)

    return True


if __name__ == "__main__":

    day = 2
    ex = ""# "_ex"

    data = split_data(f'day {day}/input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)


    # Exercice 2
    print('## Excercice 2')
    part_2(data)
