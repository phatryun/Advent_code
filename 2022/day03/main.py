import string
import numpy as np
from pathlib import Path

def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [line.rstrip() for line in f]

    return np.array(lines)


def split_half(rucksack):
    half = len(rucksack) // 2
    return rucksack[:half], rucksack[half:]

def part_1(data):
    """
    
    """
    sum_priorities = 0
    for i in range(len(data)):
        first_comp, second_compartment = split_half(data[i])
        duplicate_obj = set(first_comp).intersection(second_compartment).pop()
        # print(f"{data[i]}: {duplicate_obj}")
        priority = 1 if duplicate_obj.islower() else 27
        priority += string.ascii_lowercase.index(duplicate_obj.lower())
        # print(f"{duplicate_obj} -> {string.ascii_lowercase.index(duplicate_obj.lower())}  == {priority}")

        sum_priorities += priority

    print(sum_priorities)

    return True


def part_2(data):
    """
    
    """
    sum_priorities = 0
    i = 0
    while i + 2 < len(data):
        first_elve = data[i]
        secon_elve = data[i+1]
        third_elve = data[i+2]

        set_duplicates = set(first_elve).intersection(secon_elve)
        set_duplicates = set(set_duplicates).intersection(third_elve)
        
        badge = set_duplicates.pop()

        # print(f"{first_elve}, {secon_elve}, {third_elve} == {duplicates}")
        priority = 1 if badge.islower() else 27
        priority += string.ascii_lowercase.index(badge.lower())

        sum_priorities += priority

        i += 3

    print(sum_priorities)



    return True


if __name__ == "__main__":

    ex = ""  # "_ex"

    path = Path(__file__).parent.resolve()

    data = split_data(path / f"input{ex}.txt")

    # Exercice 1
    print('## Excercice 1')
    part_1(data)

    # Exercice 2
    print('## Excercice 2')
    part_2(data)
