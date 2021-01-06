from math import radians, sin, cos
from collections import Counter
from copy import copy, deepcopy
from functools import partial
from pprint import pprint
from timeit import timeit

op_to_delta = {
    'N': (0, 0, 1),
    'S': (0, 0, -1),
    'E': (0, 1, 0),
    'W': (0, -1, 0),
    'L': (1, 0, 0),
    'R': (-1, 0, 0),
}

def solve(data, *args, **kwargs):
    direction, x, y = 0, 0, 0
    for line in data:
        op, arg = line[0], int(line[1:])
        if op == 'F':
            x, y = x + arg * sin(radians(direction)), y + arg * cos(radians(direction))
        else:
            direction, x, y = (direction, x, y) + arg * op_to_delta[op]
    return abs(x) + abs(y)

def solve_2(data, *args, **kwargs):
    wx, wy, x, y = 0, 0, 0, 0
    for line in data:
        op, arg = line[0], int(line[1:])
        if op == 'F':
            x, y = (x, y) + arg * (wx, wy)
        elif op in 'LR':
            wx = wx * cos(radians(arg)) - wy * sin(radians(arg))
            wy = wx * sin(radians(arg)) + wy * cos(radians(arg))
        else:
            wx, wy = (wx, wy) + arg * op_to_delta[op][1:]
    return abs(x) + abs(y)

test_data = '''F10
N3
F7
R90
F11'''

with open('input/day_12.txt') as f:
    # data = [line.rstrip() for line in f]
    data = [line.rstrip() for line in test_data.splitlines()]

# data = [line for line in data]
# data.sort()
print(solve(data))
print(solve_2(data))
# print(timeit(partial(solve_2, data), number=1))
