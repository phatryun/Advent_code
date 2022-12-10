import numpy as np
from pathlib import Path
from headTail import HeadTail


def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [
            line.rstrip().split(" ")
            for line in f
        ]

    return np.array(lines)


def part_1(data):
    """

    """
    head_tail = HeadTail(verbose=False)

    for i_step in range(len(data)):
        head_tail.move(data[i_step])

    unique_list_tail_position = set(head_tail.list_tail_position)

    print(f"len(unique_list_tail_position): {len(unique_list_tail_position)}")

    return True


def part_2(data):
    """

    """
    head_tail = HeadTail(count_knot=10, verbose=False)

    for i_step in range(len(data)):
        head_tail.move(data[i_step])

    unique_list_tail_position = set(head_tail.list_tail_position)

    print(f"len(unique_list_tail_position): {len(unique_list_tail_position)}")

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
