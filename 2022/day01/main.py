import numpy as np
from pathlib import Path


def split_data(str_file_path):
    """
        Function that get data
    """
    with open(str_file_path) as f:
        lines = [line.rstrip() for line in f]

    return np.array(lines)


def get_list_cal_elves(data):
    """
    """
    list_elves_Calories = list()
    i_elve = 1
    cal = 0
    for i in range(len(data)):
        val = data[i]
        if val == "":
            list_elves_Calories.append((i_elve, cal))
            i_elve += 1
            cal = 0
            continue

        cal += int(val)
    list_elves_Calories.append((i_elve, cal))

    list_elves_Calories.sort(key=lambda x: -x[1])
    return list_elves_Calories


def part_1(data):
    """

    """
    list_elves_Calories = get_list_cal_elves(data)
    # print(list_elves_Calories)

    print(f"list_elves_Calories[0] : {list_elves_Calories[0]}")

    return True


def part_2(data):
    """

    """
    list_elves_Calories = get_list_cal_elves(data)
    print(list_elves_Calories[:3])

    res = list_elves_Calories[0][1] + list_elves_Calories[1][1] + list_elves_Calories[2][1]
    print(f"{list_elves_Calories[0][1]} + {list_elves_Calories[1][1]} + {list_elves_Calories[2][1]} = {res}")

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
