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
        pass
    return result

def solve_2(data):
    counter = Counter()
    result, a, b = 0, 0, 0
    for line in data:
        pass
    return result


test_data = '''replace'''

if __name__ == '__main__':
    with open('input/day_x.txt') as f:
        # data = [line.rstrip() for line in f]
        data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
