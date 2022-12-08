import numpy as np
from pathlib import Path


def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [line.rstrip() for line in f]

    return np.array(lines)


def part_1(data):
    """

    """

    count_overlap = 0

    for pair in data:
        elves_1, elves_2 = [
            set(range(int(elt.split('-')[0]), int(elt.split('-')[1]) + 1))
            for elt in pair.split(",")
        ]
        itersection = set(elves_1).intersection(elves_2)

        if itersection == elves_1 or itersection == elves_2:
            count_overlap += 1

    print(f"count_overlap: {count_overlap}")

    return True


def part_2(data):
    """

    """
    count_overlap = 0

    for pair in data:
        elves_1, elves_2 = [
            set(range(int(elt.split('-')[0]), int(elt.split('-')[1]) + 1))
            for elt in pair.split(",")
        ]
        itersection = set(elves_1).intersection(elves_2)

        if itersection:
            count_overlap += 1

    print(f"count_overlap: {count_overlap}")

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
