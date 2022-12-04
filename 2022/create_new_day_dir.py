import os
import sys
import getopt
import shutil
from pathlib import Path
from aocd import get_data

if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:],"d:")
    except getopt.GetoptError:
        print('Please provide -d <day> args to create the right directory')
        sys.exit(2)

    dict_opt = {elt[0]: elt[1] for elt in opts}
    
    if "-d" not in dict_opt.keys():
        print("Please provide -d <day> args to create the right directory")
        sys.exit(2)
    elif not dict_opt['-d'].isdigit():
        print("Please provide -d <day> args where day is an integer")
        sys.exit(2)

    int_day = int(dict_opt['-d'])
    str_day = f"{int_day:02}"    
    print(f"day: {str_day}")

    path = Path(__file__).parent.resolve()

    try:
        # create a new folder
        os.mkdir(path / f"day{str_day}")

        # copy template and rename it
        original = path / "template.py"
        target = path / f"day{str_day}" / "main.py" 
        shutil.copyfile(original, target)

        # create input.txt input_ex.txt
        f_ex = open(path / f"day{str_day}" / "input_ex.txt", "w")
        f_ex.close()
        f = open(path / f"day{str_day}" / "input.txt", "w")
        f.close()
        
        # fill input.txt --> https://github.com/wimglenn/advent-of-code-data
        data = get_data(day=int_day, year=2022)
        with open(path / f"day{str_day}" / "input.txt", "w") as f:
            f.write(data)

    except FileExistsError:
        print("Impossible to create a day that already exist to avoid deleting works.")
        sys.exit(2)
