import numpy as np
from pathlib import Path


def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [[int(e) for e in line.rstrip()] for line in f]

    return np.array(lines)


def part_1(data):
    """

    """
    nb_line = len(data)
    nb_col = len(data[1, :])
    print(f"nb_line: {nb_line} - nb_col: {nb_col}")

    res = 2 * nb_line + 2 * (nb_col - 2)

    for i_line in range(1, nb_line - 1):
        for i_col in range(1, nb_col - 1):
            tree_height = data[i_line, i_col]

            min_height_neiourgh = np.array([
                data[i_line, 0:i_col].max(),  # left
                data[i_line, i_col+1:].max(),  # right
                data[0:i_line, i_col].max(),  # Top
                data[i_line+1:, i_col].max()  # bottom
            ]).min()

            if tree_height > min_height_neiourgh:
                res += 1

    print(res)

    return True


def count_viewed_tree(x, array):
    tmp = [0 if x > e else 1 for e in array]
    tmp = np.cumsum(tmp)

    tmp = tmp[tmp == 0]
    res = len(tmp)
    # the view has been stop
    if len(tmp) < len(array):
        res += 1

    return res


def part_2(data):
    """
    """
    nb_line = len(data)
    nb_col = len(data[1, :])

    list_scenic_score = list()

    for i_line in range(0, nb_line):
        for i_col in range(1, nb_col):
            tree_height = data[i_line, i_col]

            tree_score = 1
            # Left
            tree_score *= count_viewed_tree(tree_height, np.flip(data[i_line, 0:i_col]))
            # Right
            tree_score *= count_viewed_tree(tree_height, data[i_line, i_col+1:])
            # Top
            tree_score *= count_viewed_tree(tree_height, np.flip(data[0:i_line, i_col]))
            # bottom
            tree_score *= count_viewed_tree(tree_height, data[i_line+1:, i_col])

            list_scenic_score.append(tree_score)

    print(np.array(list_scenic_score).max())

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
