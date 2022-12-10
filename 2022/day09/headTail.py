import numpy as np


class HeadTail:
    def __init__(self, count_knot=2, verbose=False):
        self.start = np.array([0, 0])
        self.list_knots = list()
        for _ in range(count_knot):
            self.list_knots.append(np.array([0, 0]))

        self.verbose = verbose
        self.list_tail_position = list()

        self.mouvment_val = {
            'R': np.array([0, 1]), 'L': np.array([0, -1]),
            'U': np.array([1, 0]), 'D': np.array([-1, 0])
        }

    def move(self, indications):
        direction, count = indications
        if self.verbose:
            print(f"=== {indications} ===")
        for _ in range(int(count)):
            for i_knot in range(len(self.list_knots) - 1):
                head = self.list_knots[i_knot]
                tail = self.list_knots[i_knot + 1]

                if i_knot == 0:
                    head = head + self.mouvment_val[direction]

                distance_head_tail = head - tail

                sign_vector_head_tail = distance_head_tail // np.abs(distance_head_tail)

                if np.abs(distance_head_tail).sum() == 3:
                    tail_vector = np.array([1, 1]) * sign_vector_head_tail
                else:
                    tail_vector = np.array([0, 0])
                    for i_dist in range(len(distance_head_tail)):
                        if distance_head_tail[i_dist] > 1:
                            tail_vector[i_dist] = distance_head_tail[i_dist] - 1
                        elif distance_head_tail[i_dist] < -1:
                            tail_vector[i_dist] = distance_head_tail[i_dist] + 1

                tail = tail + tail_vector

                self.list_knots[i_knot] = head
                self.list_knots[i_knot + 1] = tail

            self.list_tail_position.append("-".join([str(i) for i in tail]))

            if self.verbose:
                print(self.print_grid())
                print()

    def print_grid(self):
        """ Imporvement: put the start as the center of the map
        """
        min = 10

        grid = []
        for _ in range(min):
            tmp = []
            for _ in range(min):
                tmp.append(".")
            grid.append(tmp)

        grid[(min-1) - self.start[0]][self.start[1]] = "s"

        for i_knot in range(len(self.list_knots)-1, 0, -1):
            knot = self.list_knots[i_knot]
            grid[(min-1) - knot[0]][knot[1]] = str(i_knot)

        head = self.list_knots[0]
        grid[(min-1) - head[0]][head[1]] = "H"

        res = "\n".join([" ".join(line) for line in grid])

        return res
