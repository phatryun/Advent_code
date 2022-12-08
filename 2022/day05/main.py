import re
from pathlib import Path
from copy import deepcopy


def split_data(str_file_path):

    crates_stacks_raw = []
    rearrg_process = []

    rearrangement = False
    with open(str_file_path) as f:

        for line in f:
            line_val = line.rstrip()
            # the empty line delimit stacks than process
            if not line_val:
                rearrangement = True
                continue

            if rearrangement:
                rearrg_process.append(line_val)
            else:
                crates_stacks_raw.append(line_val)

    # handle stacks
    # Get the position of each stack accorting to last raw: number
    dict_position = {
        int(stack_position): crates_stacks_raw[-1].index(stack_position)
        for stack_position in crates_stacks_raw[-1] if stack_position != " "
    }
    # create a fake empty list
    dict_crates_stacks = {
        key: list() for key in dict_position.keys()
    }
    # fill stacks
    for i_stack in range(len(crates_stacks_raw) - 2, -1, -1):
        for key in dict_position:
            if dict_position[key] < len(crates_stacks_raw[i_stack]):
                val = crates_stacks_raw[i_stack][dict_position[key]]
                if val != " ":
                    dict_crates_stacks[key].append(val)

    # print(dict_crates_stacks)

    # handle rearranging process
    list_process = []
    regex = r'move (\d+) from (\d+) to (\d+)'
    for process in rearrg_process:
        all_val = [int(x) for x in re.findall(regex, process)[0]]
        list_process.append(all_val)

    return dict_crates_stacks, list_process


def part_1(data):
    """

    """
    dict_crates_stacks, list_process = data
    # print(dict_crates_stacks)

    for process in list_process:
        count_crates, from_stack, to_stact = process
        # print(f"move {count_crates} from {from_stack} to {to_stact}")
        for _ in range(count_crates):
            dict_crates_stacks[to_stact].append(dict_crates_stacks[from_stack].pop())
        # print(dict_crates_stacks)

    res = [dict_crates_stacks[key][-1] for key in dict_crates_stacks]
    print(f"solution: {''.join(res)}")

    return True


def part_2(data):
    """

    """
    dict_crates_stacks, list_process = data

    for process in list_process:
        count_crates, from_stack, to_stact = process
        # print(f"move {count_crates} from {from_stack} to {to_stact}")
        temp_stack = list()
        for _ in range(count_crates):
            temp_stack.append(dict_crates_stacks[from_stack].pop())

        for _ in range(count_crates):
            dict_crates_stacks[to_stact].append(temp_stack.pop())

        # print(dict_crates_stacks)

    res = [dict_crates_stacks[key][-1] for key in dict_crates_stacks]
    print(f"solution: {''.join(res)}")

    return True


if __name__ == "__main__":

    ex = ""  # "_ex"

    path = Path(__file__).parent.resolve()

    data = split_data(path / f"input{ex}.txt")

    # Exercice 1
    print('## Excercice 1')
    part_1(deepcopy(data))

    # Exercice 2
    print('## Excercice 2')
    part_2(deepcopy(data))
