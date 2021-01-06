from collections import Counter
from copy import copy, deepcopy
from functools import partial
from pprint import pprint
from timeit import timeit


def solve(data, *args, **kwargs):
    prev_data, new_data = None, data
    while prev_data != new_data:
        prev_data, new_data = new_data, round(new_data)
    return sum(line.count('#') for line in new_data)

def round(data):
    new_data = deepcopy(data)
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char == '.':
                continue
            if char == 'L' and not any(seat == '#' for seat in neighbours(data, x, y)):
                new_data[x][y] = '#'
            if char == '#' and sum(seat == '#' for seat in neighbours(data, x, y)) >= 4:
                new_data[x][y] = 'L'
    return new_data

def neighbours(data, x, y):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if j == i == 0:
                continue
            if 0 <= x + i < len(data) and 0 <= y + j < len(data[0]):
                yield data[x + i][y + j]


def solve_2(data, *args, **kwargs):
    prev_data, new_data = None, data
    while prev_data != new_data:
        prev_data, new_data = new_data, round_2(new_data)
    return sum(line.count('#') for line in new_data)


def round_2(data):
    new_data = deepcopy(data)
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char == '.':
                continue
            if char == 'L' and not any(seat == '#' for seat in neighbours_rays(data, x, y)):
                new_data[x][y] = '#'
            if char == '#' and sum(seat == '#' for seat in neighbours_rays(data, x, y)) >= 5:
                new_data[x][y] = 'L'
    return new_data


def neighbours_rays(data, x, y):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if j == i == 0:
                continue
            for ray_length in range(1, int(1e100)):
                nx, ny = x + ray_length * i, y + ray_length * j
                if not (0 <= nx < len(data) and 0 <= ny < len(data[0])):
                    break
                if data[nx][ny] == '.':
                    continue
                yield data[nx][ny]
                break



test_data = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

with open('input/day_11.txt') as f:
    data = [list(line.rstrip()) for line in f]
    # data = [list(line.rstrip()) for line in test_data.splitlines()]

print(timeit(partial(solve, data), number=1))
print(timeit(partial(solve_2, data), number=1))
