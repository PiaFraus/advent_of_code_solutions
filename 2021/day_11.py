import itertools
from copy import deepcopy


def neighbours(x, y, min_x=0, min_y=0, max_x=float('+inf'), max_y=float('+inf')):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if min_x <= dx + x <= max_x and min_y <= dy + y <= max_y and not (dx == dy == 0):
                yield x + dx, y + dy


def step(data):
    next_step = deepcopy(data)
    unprocessed_flashes = set()
    processed_flashes = set()
    for i, row in enumerate(data):
        for j, _ in enumerate(row):
            next_step[i][j] += 1
            if next_step[i][j] == 10:
                unprocessed_flashes.add((i, j))
    while unprocessed_flashes:
        i, j = unprocessed_flashes.pop()
        for ni, nj in neighbours(i, j, 0, 0, len(data) - 1, len(data[0]) - 1):
            next_step[ni][nj] += 1
            if next_step[ni][nj] == 10:
                unprocessed_flashes.add((ni, nj))
        processed_flashes.add((i, j))
    for i, j in processed_flashes:
        next_step[i][j] = 0
    return next_step, len(processed_flashes)


def solve(data, n=100):
    data = [list(map(int, line)) for line in data]
    result = 0
    for i in range(n):
        data, flashes = step(data)
        print(f'Step {i}. Flashes={flashes}')
        result += flashes
    return result


def solve_2(data):
    data = [list(map(int, line)) for line in data]
    for i in itertools.count():
        data, flashes = step(data)
        print(f'Step {i}. Flashes={flashes}')
        if flashes == len(data) * len(data[0]):
            return i + 1


test_data = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''

if __name__ == '__main__':
    with open('input/day_11.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
