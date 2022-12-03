import os
import numpy as np
from collections import Counter


def split_data(str_file_path):
    with open(str_file_path) as f:
        lines = [line.rstrip() for line in f]

    #print(lines)
    draw_numbers = [int(elt) for elt in lines[0].split(',')]

    list_bigo_grid = []
    
    #print((len(lines) - 1))

    for i in range(int((len(lines) - 1) / 6)):
    	grid = lines[6 * i + 2:6 * i + 7]
    	grid = np.array([[int(line[i:i+2]) for i in range(0, len(line), 3)] for line in grid])

    	list_bigo_grid.append(grid)

    #print(list_bigo_grid)
    #print(list_bigo_grid)
    #print(list_bigo_grid[0][0][0])

    return draw_numbers, list_bigo_grid

def checkGrid(grid):
	for line in grid:
		if set(line) == {'x'}:
			return True

	return False

def markGrid(grid, number):

	#for i in range(len(grid)):
	#		grid.replace(number, "x")

	grid = [['x' if x==number else x for x in line] for line in grid]

	gridT = np.array(list(map(list, zip(*grid))))
	#print(gridT)
	#print(checkGrid(grid))
	#print(checkGrid(gridT))

	return grid, bool(checkGrid(grid) + checkGrid(gridT))

def getSum(grid):

	cpt = 0
	for line in grid:
		for elt in line:
			if elt != "x":
				cpt += elt

	return cpt

def part_1(data):
    """
    
    """
    draw_numbers, list_bigo_grid = data
    
    for number in draw_numbers:
    	#print(number)
    	for i in range(len(list_bigo_grid)):
    		
    		grid, bingo = markGrid(list_bigo_grid[i], number)

    		list_bigo_grid[i] = grid
    		#print(grid)
    		if bingo:
    			print("BINGO!!")
    			sum_remaining = getSum(grid)
    			print(f"sum_remaining:{sum_remaining}, number: {number}-> {number * sum_remaining}")
    			return True


    
    #for i in range(len(dataT)):
    

    return True


def part_2(data):
    """
    
    """
    
    draw_numbers, list_bigo_grid = data
    
    for number in draw_numbers:
    	#print(number)
    	#for i in range(len(list_bigo_grid)):
    	i = 0
    	while i < len(list_bigo_grid):	
    		grid, bingo = markGrid(list_bigo_grid[i], number)

    		list_bigo_grid[i] = grid
    		#print(grid)
    		if bingo:
    			print("BINGO!!")
    			if len(list_bigo_grid) > 1:
    				print('not the last one, continue')
    				del list_bigo_grid[i]
    				i -= 1
    			else:
	    			sum_remaining = getSum(grid)
	    			print(f"sum_remaining:{sum_remaining}, number: {number}-> {number * sum_remaining}")
    				return True

    		i += 1

    return True


if __name__ == "__main__":

    day = 4
    ex = "" # "_ex" # "" #

    data = split_data(f'input{ex}_{day}.txt')

    # Exercice 1
    print('## Excercice 1')
    part_1(data)


    # Exercice 2
    print('## Excercice 2')
    part_2(data)
