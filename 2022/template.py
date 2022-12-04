import numpy as np
from pathlib import Path

def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [line.rstrip() for line in f]

    return np.array(lines)


def part_1(data):
    """
    
    """
    # for i in range(len(data)):

    return True


def part_2(data):
    """
    
    """
    # for i in range(len(data)):

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