import itertools
from math import radians, sin, cos
from collections import Counter, defaultdict
from copy import copy, deepcopy
from functools import partial, reduce
from pprint import pprint
from timeit import timeit


def solve(data, dimensions):
    actives = set()
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == '#':
                actives.add((i, j) + (0,) * (dimensions - 2))
    print_space(actives)
    prev_actives, new_actives = None, actives
    for _ in range(6):
        prev_actives, new_actives = new_actives, round(new_actives)
        print_space(new_actives)

    return len(new_actives)


def print_space(actives):
    x_range, y_range, *others = ((min(dimension), max(dimension)) for dimension in zip(*actives))
    for layer in itertools.product(*(range(l, r+1) for l, r in others)):
        print(f'layer={layer}')
        for x in range(x_range[0], x_range[1] + 1):
            for y in range(y_range[0], y_range[1] + 1):
                print('#' if ((x, y) + layer) in actives else '.', end='')
            print()


def round(actives):
    neighbours_counter = Counter()
    for x in actives:
        for neighbour in neighbours(x):
            neighbours_counter[neighbour] += 1
    new_actives = set()
    for x, count in neighbours_counter.items():
        if x not in actives and count == 3:
            new_actives.add(x)
        elif x in actives and count in (2, 3):
            new_actives.add(x)
    return new_actives


def neighbours(coordinates):
    for shift_coordinate in itertools.product((-1, 0, 1), repeat=len(coordinates)):
        if all(x == 0 for x in shift_coordinate):
            continue
        yield tuple(x + y for x, y in zip(coordinates, shift_coordinate))


test_data = '''.#.
..#
###
'''

with open('input/day_17.txt') as f:
    # data = [line.rstrip() for line in f]
    data = [line.rstrip() for line in test_data.splitlines()]
data = [list(line) for line in data]
print(solve(data, 4))
