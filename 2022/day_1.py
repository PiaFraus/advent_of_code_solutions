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


def solve(data):
    groups = [[]]
    for line in data:
        if not line:
            groups.append([])
            continue
        groups[-1].append(int(line))
    return max(sum(g) for g in groups)

def solve_2(data):
    counter = Counter()
    elf_n = 0
    for line in data:
        if not line:
            elf_n += 1
            continue
        counter[elf_n] += int(line)
    return sum(x[1] for x in counter.most_common(3))


test_data = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

if __name__ == '__main__':
    with open('input/day_1.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
