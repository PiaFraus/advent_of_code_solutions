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

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def solve(data):
    result = 0
    for line in data:
        left, right = line[:len(line)//2], line[len(line)//2:]
        common = set(left) & set(right)
        result += priority.index(common.pop()) + 1
    return result

def solve_2(data):
    result = 0
    group_set = None
    for i, line in enumerate(data):
        if i % 3 == 0:
            group_set = set(line)
        else:
            group_set &= set(line)
        if i % 3 == 2:
            result += priority.index(group_set.pop()) + 1
    return result


test_data = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

if __name__ == '__main__':
    with open('input/day_3.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
