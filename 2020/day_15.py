import itertools
from math import radians, sin, cos
from collections import Counter
from copy import copy, deepcopy
from functools import partial, reduce
from pprint import pprint
from timeit import timeit


def solve(data, num):
    data = data[0]
    data =list(map(int,data.split(',')))
    memory = {v: i+1 for i, v in enumerate(data[:-1])}
    last_number = data[-1]
    for i in range(len(data)+1, num+1):
        if last_number not in memory:
            new_number = 0
        else:
            new_number = i - 1 - memory[last_number]
        memory[last_number] = i - 1
        last_number = new_number
        print(i,  last_number)
    return last_number

test_data = '''9,3,1,0,8,4'''

with open('input/day_15.txt') as f:
    # data = [line.rstrip() for line in f]
    data = [line.rstrip() for line in test_data.splitlines()]
print(timeit(partial(solve, data, 2020), number=1))
