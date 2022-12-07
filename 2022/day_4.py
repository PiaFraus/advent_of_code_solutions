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
    counter = Counter()
    result, a, b = 0, 0, 0
    for line in data:
        first, second = line.split(',')
        ff, ft = map(int, first.split('-'))
        first = set(range(ff, ft+1))
        ff, ft = map(int, second.split('-'))
        second = set(range(ff, ft+1))
        if first.issubset(second) or second.issubset(first):
            result += 1

    return result


def solve_2(data):
    counter = Counter()
    result, a, b = 0, 0, 0
    for line in data:
        first, second = line.split(',')
        ff, ft = map(int, first.split('-'))
        first = set(range(ff, ft+1))
        ff, ft = map(int, second.split('-'))
        second = set(range(ff, ft+1))
        if first.intersection(second):
            result += 1

    return result


test_data = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

if __name__ == '__main__':
    with open('input/day_4.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
