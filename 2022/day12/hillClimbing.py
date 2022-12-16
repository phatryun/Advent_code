import numpy as np


class HillClimbing:
    def __init__(self, grid) -> None:

        self.original_grid = grid.copy()

        self.grid = grid.copy()
        for i_line in range(len(self.grid)):
            for i_column in range(len(self.grid[i_line])):
                if self.grid[i_line][i_column] == "S":
                    self.start_position = np.array([i_line, i_column])
                    self.grid[i_line][i_column] = "a"
                elif self.grid[i_line][i_column] == "E":
                    self.exit_position = np.array([i_line, i_column])
                    self.grid[i_line][i_column] = "z"

        self.len_grid_line = len(self.grid)
        self.len_grid_col = len(self.grid[0])

        self.actual_position = self.start_position.copy()
        self.count_move = 0
        self.moves_list = list()
        self.old_position = list()
        self.list_position_deadend = list()

    def get_possible_move(self):

        actual_line, actual_col = self.actual_position

        moves_possible = [
            (np.array([1, 0]), 'D'), (np.array([0, -1]), 'L'), (np.array([-1, 0]), 'U'), (np.array([0, 1]), 'R')
        ]
        res = list()
        for next_position, _ in moves_possible:
            next_line, next_col = self.actual_position + next_position
            if ((next_line) >= 0) and ((next_line) < self.len_grid_line) and \
               ((next_col) >= 0) and ((next_col) < self.len_grid_col):

                if -1 <= ord(self.grid[next_line][next_col]) - ord(self.grid[actual_line][actual_col]) <= 2:
                    res.append(np.array([next_line, next_col]))

        return res

    def to_str(self, position_from_end):

        print_grid = self.grid.copy()

        for move in position_from_end.keys():
            print_grid[move[0]][move[1]] = "-"

        print_grid[self.exit_position[0]][self.exit_position[1]] = "E"
        print_grid[self.actual_position[0]][self.actual_position[1]] = "@"

        return "\n".join(["".join(line) for line in print_grid])

    def bfs_algorithm(self):
        end = tuple(self.exit_position.tolist())
        moves = [end]
        positions_from_end = dict()
        positions_from_end[end] = 0

        cpt = 0

        while moves:  # and cpt < 2:
            actual = moves.pop(0)
            self.actual_position = np.array(actual)
            next_positions = [tuple(next.tolist()) for next in self.get_possible_move()]

            # print(f"self.actual_position: {self.actual_position} -> {next_positions}")
            # print(self.to_str(positions_from_end))

            for next in next_positions:
                if next not in positions_from_end:
                    positions_from_end[next] = positions_from_end[actual] + 1
                    moves.append(next)

            cpt += 1

        return positions_from_end
