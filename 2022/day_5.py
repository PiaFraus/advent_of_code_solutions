import bisect
import itertools
import re
from itertools import product, tee
from math import radians, sin, cos, sqrt
from collections import Counter, defaultdict, deque, namedtuple
from copy import copy, deepcopy
from functools import partial, reduce
from pprint import pprint
from timeit import timeit
from collections import Counter


def solve(data, reverse_buffer=True):
    stacks = defaultdict(list)
    data_iter = iter(data)
    for line in data_iter:
        for i, c in enumerate(line):
            if c not in "[] ":
                stacks[i//4 + 1].append(c)
        if not line:
            break
    for line in data_iter:
        n, fr, to = map(int, re.match('move (\d+) from (\d+) to (\d+)', line).groups())
        buffer = stacks[fr][:n]
        del stacks[fr][:n]
        stacks[to][:0] = reversed(buffer) if reverse_buffer else buffer
    return ''.join(stacks[k][0] for k in range(1, max(stacks)+1))

def solve_2(data):
    return solve(data, r=False)


test_data = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

if __name__ == '__main__':
    with open('input/day_5.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
