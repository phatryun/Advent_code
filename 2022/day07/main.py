import re
import numpy as np
from pathlib import Path

from fileSystem import FileSystem


def split_data(str_file_path):

    with open(str_file_path) as f:
        lines = [cmd.split('\n') for cmd in f.read().split("$ ")]

    return lines


def create_filesystem(data):

    dict_file_system = {"/": FileSystem("/")}

    actual_path = ""
    for cmd in data:
        if cmd[0].startswith("cd"):
            regex = r'cd (\w+|..|\/)'
            dir = re.findall(regex, cmd[0])[0]
            if dir == "/":
                actual_path = "/"
            elif dir == "..":
                actual_path = "/".join(actual_path.split('/')[:-1])
            else:
                actual_path += f"/{dir}"

        elif cmd[0].startswith("ls"):
            actual_file_system = dict_file_system[actual_path]
            list_children = list()
            for elt in cmd[1:]:
                if elt.startswith('dir'):
                    regex = r'dir (\w+)'
                    dir_name = re.findall(regex, elt)[0]
                    new_file_system = FileSystem(f"{actual_path}/{dir_name}")
                    dict_file_system[f"{actual_path}/{dir_name}"] = new_file_system
                    list_children.append(new_file_system)
                elif elt:
                    regex = r'(\d+) (\w+.*\w*)'
                    file_size, file_name = re.findall(regex, elt)[0]
                    new_file_system = FileSystem(f"{actual_path}/{file_name}", int(file_size))
                    list_children.append(new_file_system)

            actual_file_system.set_children(list_children)
            dict_file_system[actual_path] = actual_file_system

        else:
            # do nothing
            continue

    return dict_file_system


def part_1(dict_file_system):
    """

    """
    res = 0

    for folder in dict_file_system:
        dir_size = dict_file_system[folder].calculate_dir_size()
        if dir_size <= 100000:
            res += dir_size

    print(res)

    return True


def part_2(dict_file_system):
    """
    """
    disk_size = 70000000
    min_space_needed = 30000000
    root_size = dict_file_system["/"].calculate_dir_size()

    space_needed = min_space_needed-(disk_size-root_size)

    print(f"unused space: {disk_size-root_size} -- {space_needed} needed")

    list_dir_candidate = list()

    for folder in dict_file_system:
        dir_size = dict_file_system[folder].calculate_dir_size()
        if dir_size > space_needed:
            list_dir_candidate.append(dir_size)

    list_dir_candidate.sort()
    print(f"{list_dir_candidate[0]}")

    return True


if __name__ == "__main__":

    ex = ""  # "_ex"

    path = Path(__file__).parent.resolve()

    data = split_data(path / f"input{ex}.txt")

    dict_file_system = create_filesystem(data)

    # Exercice 1
    print('## Excercice 1')
    part_1(dict_file_system)

    # Exercice 2
    print('## Excercice 2')
    part_2(dict_file_system)
