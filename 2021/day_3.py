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
    result = defaultdict(int)
    total = len(data)
    for line in data:
        for i, c in enumerate(line):
            result[i] += c == '1'
    g = ''
    for i in range(len(data[0])):
        g = g + str(int(result[i] > total / 2))
    g = int(g, 2)
    return g * (2**len(data[0]) + ~g)

def solve_2(data):
    counters = Counter()
    for line in data:
        for i, c in enumerate(line):
            counters[line[:i+1]] += 1
    a, b = '', ''
    for i in range(len(data[0])):
        a += '1' if counters[a + '1'] >= counters[a + '0'] else '0'
        b += '1' if counters[b + '1'] < counters[b + '0'] else '0'
    return int(a, 2) * int(b, 2)


test_data = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''

if __name__ == '__main__':
    with open('input/day_3.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
