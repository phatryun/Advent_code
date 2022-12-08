import numpy as np
from pathlib import Path


def split_data(str_file_path):
    """
        Function that get data
    """
    with open(str_file_path) as f:
        lines = [line.rstrip().split(" ") for line in f]

    return np.array(lines)


RPS_points = {
    "val": {
        'A': 1,
        'B': 2,
        'C': 3
    },
    'res': {
        'win': 6,
        'draw': 3,
        'loose': 0
    }
}

RPS_rules = {
    "trad": {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    },
    "win": {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }
}

RPS_rules_2 = {
    "trad": {
        'X': 'loose',
        'Y': 'draw',
        'Z': 'win'
    },
    "win": {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    },
    "draw": {
        'A': 'A',
        'B': 'B',
        'C': 'C'
    },
    "loose": {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }
}


def part_1(data):
    """

    """
    total_scrore = 0
    for match in data:
        elve = match[0]
        mine = match[1]
        mine_trad = RPS_rules['trad'][mine]
        # add result score
        match_result = "loose"
        if mine_trad == elve:
            match_result = "draw"
        elif mine_trad == RPS_rules['win'][elve]:
            match_result = "win"

        match_score = RPS_points['res'][match_result] + RPS_points['val'][mine_trad]
        total_scrore += match_score

    print(f"total_scrore: {total_scrore}")

    return True


def part_2(data):
    """

    """
    total_scrore = 0
    for match in data:
        elve = match[0]
        match_outcome = RPS_rules_2['trad'][match[1]]
        my_move = RPS_rules_2[match_outcome][elve]
        match_score = RPS_points['res'][match_outcome] + RPS_points['val'][my_move]
        total_scrore += match_score

    print(f"total_scrore: {total_scrore}")

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
