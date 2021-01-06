import itertools
import re
from itertools import product
from math import radians, sin, cos, sqrt
from collections import Counter, defaultdict, deque, namedtuple
from copy import copy, deepcopy
from functools import partial, reduce
from pprint import pprint
from timeit import timeit
from collections import Counter


def solve(data):
    results = set()
    for line in data:
        _, row, column = parse_line(line)
        if (row, column) in results:
            results.remove((row, column))
        else:
            results.add((row, column))
    return len(results)

def solve_2(data):
    results = set()
    for line in data:
        _, row, column = parse_line(line)
        if (row, column) in results:
            results.remove((row, column))
        else:
            results.add((row, column))
    for day in range(101):
        print(f'Day {day}: {len(results)}')
        tiles_counter = Counter()
        for x, y in results:
            for nx, ny in ((0, 2), (-1, 1), (-1, -1), (0, -2), (1, 1), (1, -1)):
                tiles_counter[x+nx, y+ny] += 1
        new_black_tiles = set()
        for tile, neighbours in tiles_counter.items():
            if tile in results and neighbours in (1, 2):
                new_black_tiles.add(tile)
            elif tile not in results and neighbours == 2:
                new_black_tiles.add(tile)
        results = new_black_tiles
    return len(results)


def parse_line(line: str):
    directions = {}
    for direction in 'se', 'sw', 'nw', 'ne', 'e', 'w':
        directions[direction] = line.count(direction)
        line = line.replace(direction, '')
    row, column = 0, 0
    for direction, count in directions.items():
        if direction.startswith('n'):
            row -= count
        elif direction.startswith('s'):
            row += count
        if direction.endswith('e'):
            column -= count * 2 if direction == 'e' else count
        elif direction.endswith('w'):
            column += count * 2 if direction == 'w' else count
    return directions, row, column


test_data = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''

with open('input/day_24.txt') as f:
    data = [line.rstrip() for line in f]
    # data = [line.rstrip() for line in test_data.splitlines()]
# data = [int(line) for line in data]
# print(solve(data))
print(solve_2(data))

# NOt 1957