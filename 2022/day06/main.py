import numpy as np
from pathlib import Path

def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [line.rstrip() for line in f]

    return np.array(lines)


def extract_unique_str(str_signal, int_length):

    res = 0

    for i_char in range(len(str_signal) - int_length):
        set_char = set([char for char in str_signal[i_char: i_char+int_length]])

        if len(set_char) == int_length: 
            res = i_char + int_length
            break

    return res

def part_1(data):
    """
    
    """

    for i_line in range(len(data)):
        res = extract_unique_str(data[i_line], 4)
        print(f"{data[i_line][res-4: res]} : {res}")

    return True


def part_2(data):
    """
    
    """
    for i_line in range(len(data)):
        res = extract_unique_str(data[i_line], 14)
        print(f"{data[i_line][res-14: res]} : {res}")
    
    return True


if __name__ == "__main__":

    ex = "_ex"  # "_ex"

    path = Path(__file__).parent.resolve()

    data = split_data(path / f"input{ex}.txt")

    # Exercice 1
    print('## Excercice 1')
    part_1(data)

    # Exercice 2
    print('## Excercice 2')
    part_2(data)