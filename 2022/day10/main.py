import numpy as np
from pathlib import Path


def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [line.rstrip() for line in f]

    return lines


def process_instruction(instruction):
    if instruction == "noop":
        return instruction, [1, 0]
    else:
        return instruction, [2, int(instruction.replace("addx ", ""))]


def get_X_position_per_cycle(data):
    """
    """
    last_cycle = 240
    X = 1

    _, cpu_instruction = process_instruction(data.pop(0))

    dict_X_val = dict()

    for i_cycle in range(1, last_cycle + 1):

        dict_X_val[i_cycle] = X

        if cpu_instruction[0] == 1:
            X += cpu_instruction[1]
            if data:
                _, cpu_instruction = process_instruction(data.pop(0))
            else:
                _, cpu_instruction = "END", [1, 0]
        else:
            cpu_instruction[0] -= 1

    return dict_X_val


def part_1(dict_X_val):
    """

    """

    dict_cycle_to_get = {
        20 + i*40: dict_X_val[20 + i*40] for i in range(6)
    }

    res = np.array([key*dict_cycle_to_get[key] for key in dict_cycle_to_get]).sum()
    print(f"{dict_cycle_to_get}: {res}")

    return True


def part_2(dict_X_val):
    """

    """

    image = [["0" for _ in range(40)] for _ in range(6)]

    for i_cycle in dict_X_val:

        line_image = (i_cycle - 1) // 40
        col_image = (i_cycle - 1) % 40

        X = dict_X_val[i_cycle]
        sprite = ["." if abs(X-i) > 1 else '#' for i in range(40)]

        if i_cycle <= 21:
            print(f"==== Cycle {i_cycle} ====")
            print(f"X: {X}")
            print(f"Sprite position: {''.join(sprite)}")
            print(f"line_image: {line_image} - col_image: {col_image}")
            print(f"val: {sprite[col_image]}")

        image[line_image][col_image] = sprite[col_image]

    res = "\n".join(["".join(line) for line in image])
    print(res)

    return True


if __name__ == "__main__":

    ex = ""  # "_ex"

    path = Path(__file__).parent.resolve()

    data = split_data(path / f"input{ex}.txt")

    dict_X_val = get_X_position_per_cycle(data)

    # Exercice 1
    print('## Excercice 1')
    part_1(dict_X_val)

    # Exercice 2
    print('## Excercice 2')
    part_2(dict_X_val)
