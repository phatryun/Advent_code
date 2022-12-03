import sys
from itertools import permutations
import math

LINES = []
with open('./input.txt') as f:
    LINES = [i.strip() for i in f]

def gen_tiles():
    tiles = dict()
    tid = 0
    for line in LINES:
        if not line:
            continue
        if line.startswith("Tile"):
            tid = line[len("Tile "):-1]
            tiles[tid] = []

        else:
            tiles[tid] += [line]

    return tiles

def get_edges(tile):
    return [tile[0], "".join(x[-1] for x in tile), tile[-1], "".join(x[0] for x in tile)] + [tile]

def flip_tile(tile):
    return [x[::-1] for x in tile]

def rotate(tile, num):
    new_tile = tile
    for i in range(num % 4):
        new_tile = ["".join(t) for t in zip(*new_tile[::-1])]

    return new_tile

def gen_edges(tiles):
    edges = dict()
    for tid, tile in tiles.items():
        edges[tid] = []
        edges[tid] += [get_edges(tile)]
        edges[tid] += [get_edges(rotate(tile, 1))]
        edges[tid] += [get_edges(rotate(tile, 2))]
        edges[tid] += [get_edges(rotate(tile, 3))]
        edges[tid] += [get_edges(flip_tile(tile))]
        edges[tid] += [get_edges(flip_tile(rotate(tile, 1)))]
        edges[tid] += [get_edges(flip_tile(rotate(tile, 2)))]
        edges[tid] += [get_edges(flip_tile(rotate(tile, 3)))]

    return edges

def get_eligibles(curr, eligibles):
    return [e for e in eligibles if e[0] not in [c[0] for c in curr]]

def one():
    all_tiles = gen_tiles()
    all_edges = gen_edges(all_tiles)
    side_len = int(math.sqrt(len(all_tiles)))
    n_edges = dict()
    e_edges = dict()
    s_edges = dict()
    w_edges = dict()

    for tid, edges in all_edges.items():
        for edge in edges:
            e = n_edges.get(edge[0], [])
            e.append((tid, edge))
            n_edges[edge[0]] = e

            e = e_edges.get(edge[1], [])
            e.append((tid, edge))
            e_edges[edge[1]] = e

            e = s_edges.get(edge[2], [])
            e.append((tid, edge))
            s_edges[edge[2]] = e

            e = w_edges.get(edge[3], [])
            e.append((tid, edge))
            w_edges[edge[3]] = e

    solutions = []

    for i_tid, i_edges in all_edges.items():
        for i_edge in i_edges:
            eligibles = get_eligibles([(i_tid, i_edge)], w_edges.get(i_edge[1]) or [])
            stack = [([(i_tid, i_edge)], eligibles)]
            while stack:
                curr_edges, eligibles = stack.pop()

                if not eligibles:
                    continue

                curr_eligible = eligibles.pop()
                stack.append((curr_edges, eligibles))
                next_edges = curr_edges + [curr_eligible]
                if len(next_edges) == len(all_tiles):
                    # solutions += [next_edges]
                    return int(next_edges[0][0]) * int(next_edges[side_len-1][0]) * int(next_edges[len(all_tiles)-1][0]) * int(next_edges[len(all_tiles)-side_len][0]), next_edges
                    continue
                next_eligibles = []

                # first row
                if len(next_edges) < side_len:
                    # get tiles whose west edge matches current east edge
                    next_eligibles = get_eligibles(next_edges, w_edges.get(curr_eligible[1][1]) or [])

                # after first row, compare with row above
                else:
                    # get tiles whose north edge matches above tile's south edge
                    above = next_edges[len(next_edges) - side_len]
                    next_eligibles = get_eligibles(next_edges, n_edges.get(above[1][2]) or [])

                    # If this isn't the first tile in the row, compare against previous tile
                    if len(next_edges) % side_len > 1:
                        prev = next_edges[-1]
                        next_eligibles = [n for n in next_eligibles if n[1][3] == prev[1][1]]


                if next_eligibles:
                    stack.append((next_edges, next_eligibles))


    return None

def combine(tiles):
    side = int(math.sqrt(len(tiles)))
    lines = []
    for i in range(0, len(tiles), side):
        tls = tiles[i:i+side]
        for idx in range(len(tls[0])):
            lines.append("".join(x[idx] for x in tls))

    return lines

def find_monsters(image):
    """Start from the head and look for the rest of the body relative to the head"""
    side = len(image[0])
    num = 0
    # The body extends the head by one so we want to look as far as 1 less the overall size
    for i in range(18, side-1):
        # The body extends 2 rows
        for j in range(len(image)-2):
            # Find the head
            if image[j][i] == "#":
                # Find mid
                if all([image[j+1][i + k] == "#" for k in [-18, -13, -12, -7, -6, -1, 0, 1]]):
                    # Find lower
                    if all([image[j+2][i + k] == "#" for k in [-17, -14, -11, -8, -5, -2]]):
                        num += 1

    return num

def two():
    _, t = one()
    tiles = [i[1][4] for i in t]
    # remove borders from tiles
    nb_tiles = [[i[1:-1] for i in j[1:-1]] for j in tiles]
    # Assemble tiles to form image
    tiles = combine(tiles)
    nb_tiles = combine(nb_tiles)
    # print("\n".join(tiles))
    # print("-----------------")
    # print("\n".join(rotate(tiles, 1)))

    # Find the monsters
    num = find_monsters(nb_tiles) or \
    find_monsters(rotate(nb_tiles, 1)) or \
    find_monsters(rotate(nb_tiles, 2)) or \
    find_monsters(rotate(nb_tiles, 3)) or \
    find_monsters(flip_tile(nb_tiles)) or \
    find_monsters(flip_tile(rotate(nb_tiles, 1))) or \
    find_monsters(flip_tile(rotate(nb_tiles, 2))) or \
    find_monsters(flip_tile(rotate(nb_tiles, 3)))

    print("".join(nb_tiles).count("#") - num * 15)
    return None

def main():
    print(two())

if __name__ == '__main__':
    main()
