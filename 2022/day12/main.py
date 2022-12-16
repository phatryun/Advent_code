import time
import numpy as np
from pathlib import Path
from hillClimbing import HillClimbing


def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [[e for e in line.rstrip()] for line in f]

    return np.array(lines)


def part_1(map):
    """

    """
    start_time = time.time()
    positions_from_end = map.bfs_algorithm()
    end_time = time.time()
    print(f"Finsih in: {(end_time-start_time)/60:.2f}")

    if positions_from_end:
        print(f"{positions_from_end[tuple(map.start_position.tolist())]}")
    else:
        print("No solutions")

    return True


def part_2(map):
    """

    """
    start_time = time.time()
    positions_from_end = map.bfs_algorithm()
    end_time = time.time()
    print(f"Finsih in: {(end_time-start_time)/60:.2f}")

    min_step = positions_from_end[tuple(map.start_position.tolist())]
    best_start_position = tuple(map.start_position.tolist())

    for elt in positions_from_end:
        if map.grid[elt[0]][elt[1]] == 'a':
            if min_step > positions_from_end[elt]:
                min_step = positions_from_end[elt]
                best_start_position = elt

    print(f"best_start_position: {best_start_position} --> {min_step}")

    return True


if __name__ == "__main__":

    ex = ""  # "_ex"

    path = Path(__file__).parent.resolve()

    data = split_data(path / f"input{ex}.txt")

    map = HillClimbing(data)

    # Exercice 1
    print('## Excercice 1')
    part_1(map)

    # Exercice 2
    print('## Excercice 2')
    part_2(map)
