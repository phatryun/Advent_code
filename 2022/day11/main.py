import re
import numpy as np
from tqdm import tqdm
from pathlib import Path


def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = f.read()

    return lines


def processMonkeyInput(data):

    dict_monkeys = dict()

    regex = r"""Monkey (\d+):
  Starting items: (\d+[, \d+]*)
  Operation: new = old ([*|+] [\d+|old]+)
  Test: divisible by (\d+)
    If true: throw to monkey (\d)
    If false: throw to monkey (\d)"""
    groups = re.findall(regex, data)

    for group in groups:
        i_monkey = group[0]
        starting_items = list()
        for elt in group[1].split(", "):
            starting_items.append(int(elt))

        operation = group[2]
        test = int(group[3])
        result_true = group[4]
        result_false = group[5]

        dict_monkeys[i_monkey] = {
            "i_monkey": i_monkey,
            "items": starting_items,
            "operation": operation,
            "test": test,
            "monkey_true": result_true,
            "monkey_false": result_false,
            "inspect_item": 0
        }

    return dict_monkeys


def play_monkey_round(dict_monkeys, verbose=False, calmdown=None):

    for monkey_key in dict_monkeys.keys():
        op, val = dict_monkeys[monkey_key]["operation"].split(" ")
        if verbose:
            print(f"Monkey {monkey_key}: ---> {op} {val}")

        while dict_monkeys[monkey_key]["items"]:
            item = dict_monkeys[monkey_key]["items"].pop(0)
            if verbose:
                print(f"  Monkey inspects an item with a worry level of {item}.")

            res = item
            if val == "old":
                val_1 = item
            else:
                val_1 = int(val)

            if op == "+":
                res += val_1
            elif op == "*":
                res *= val_1
            elif op == "-":
                res -= val_1
            elif op == "/":
                res /= val_1

            if verbose:
                print(f"    Worry level is {op} by {val_1} to {res}.")

            if calmdown:
                res = res % calmdown
                if verbose:
                    print(f"    Monkey gets bored with item. Worry level is mod to calmdown to {res}.")

            else:
                res = int(res / 3)
                if verbose:
                    print(f"    Monkey gets bored with item. Worry level is divided by 3 to {res}.")

            # test
            test = res % dict_monkeys[monkey_key]["test"]
            if verbose:
                print(f"    Apply the test, divide by {dict_monkeys[monkey_key]['test']} -> {test}")

            monkey_to_send = dict_monkeys[monkey_key]["monkey_false"]
            if test == 0:
                if verbose:
                    print(f"    Current worry level is divisible by {dict_monkeys[monkey_key]['test']}.")
                monkey_to_send = dict_monkeys[monkey_key]["monkey_true"]

            if verbose:
                print(f"    Item with worry level {res} is thrown to monkey {monkey_to_send}.")

            dict_monkeys[monkey_to_send]["items"].append(res)
            dict_monkeys[monkey_key]["inspect_item"] += 1

    return dict_monkeys


def print_monkeys_item(dict_monkeys):

    str_res = ""
    for monkey_key in dict_monkeys.keys():
        str_items = [str(item) for item in dict_monkeys[monkey_key]['items']]
        str_res += f"Monkey {monkey_key}: {', '.join(str_items)} \n"

    return str_res


def part_1(data):
    """

    """
    dict_monkeys = processMonkeyInput(data)

    for i in range(20):
        dict_monkeys = play_monkey_round(dict_monkeys, verbose=False)
        # pprint(f"After round {i+1}, the monkeys are holding items with these worry levels:")
        # print(print_monkeys_item(dict_monkeys))

    list_inspection = list()
    for monkey_key in dict_monkeys.keys():
        list_inspection.append(dict_monkeys[monkey_key]["inspect_item"])
        # print(f"Monkey {monkey_key} inspected items {dict_monkeys[monkey_key]['inspect_item']} times.")

    list_inspection.sort()
    print(f"Monkey business leve: {list_inspection[-1] * list_inspection[-2]}")

    return True


def part_2(data):
    """

    """
    dict_monkeys = processMonkeyInput(data)

    round_to_print = []  # 1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    # numpy is returning a long and not in integer, we need to parse it if we want it to works
    monkey_LCM = int(np.prod(
        np.array([dict_monkeys[monkey_key]["test"] for monkey_key in dict_monkeys.keys()])
        ))
    print(f"monkey_LCM: {monkey_LCM}")

    for i in tqdm(range(10000)):
        dict_monkeys = play_monkey_round(dict_monkeys, verbose=False, calmdown=monkey_LCM)

        if i+1 in round_to_print:
            print(f"\nAfter round {i+1}, the monkeys are holding items with these worry levels:")
            for monkey_key in dict_monkeys.keys():
                print(f"Monkey {monkey_key} inspected items {dict_monkeys[monkey_key]['inspect_item']} times.")

    list_inspection = [dict_monkeys[monkey_key]["inspect_item"] for monkey_key in dict_monkeys.keys()]
    list_inspection.sort()
    print(f"Monkey business leve: {list_inspection[-1] * list_inspection[-2]}")

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
