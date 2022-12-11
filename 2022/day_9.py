import bisect
import itertools
import math
import re
from itertools import product, tee
from math import radians, sin, cos, sqrt
from collections import Counter, defaultdict, deque, namedtuple
from copy import copy, deepcopy
from functools import partial, reduce
from pprint import pprint
from timeit import timeit
from collections import Counter


def solve(data):
    head = [0, 0]
    tail = [0, 0]
    visited = set(tuple(tail))
    for line in data:
        direction, steps = line.split()
        for _ in range(int(steps)):
            if direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1
            elif direction == 'U':
                head[1] += 1
            else:
                head[1] -= 1
            dx = head[0] - tail[0]
            dy = head[1] - tail[1]
            if abs(dx) < 2 and abs(dy) < 2:
                continue
            tail[0] += math.ceil(abs(dx) / 2) * (1 if dx >= 0 else -1)
            tail[1] += math.ceil(abs(dy) / 2) * (1 if dy >= 0 else -1)
            visited.add(tuple(tail))
    return len(visited)

def solve_2(data):
    rope = [[0, 0] for _ in range(10)]
    visited = {tuple(rope[-1])}
    for line in data:
        direction, steps = line.split()
        for _ in range(int(steps)):
            head = rope[0]
            if direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1
            elif direction == 'U':
                head[1] += 1
            else:
                head[1] -= 1
            for i, knot in enumerate(rope):
                if i == len(rope) - 1:
                    visited.add(tuple(knot))
                else:
                    dx = knot[0] - rope[i+1][0]
                    dy = knot[1] - rope[i+1][1]
                    if abs(dx) < 2 and abs(dy) < 2:
                        continue
                    rope[i+1][0] += math.ceil(abs(dx) / 2) * (1 if dx >= 0 else -1)
                    rope[i+1][1] += math.ceil(abs(dy) / 2) * (1 if dy >= 0 else -1)
    return len(visited)

test_data = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''

if __name__ == '__main__':
    with open('input/day_9.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
