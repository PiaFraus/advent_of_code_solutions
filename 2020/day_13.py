from math import radians, sin, cos
from collections import Counter
from copy import copy, deepcopy
from functools import partial, reduce
from pprint import pprint
from timeit import timeit


def solve(data, *args, **kwargs):
    data = [(i, int(bus_id)) for i, bus_id in enumerate(data[1].split(',')) if bus_id != 'x']
    for i in range(100000000000000 // data[0][1], 100000000000000 // data[0][1] + 80000000000):
        time_stamp = i * data[0][1]
        for delta, bus_id in data:
            if (time_stamp + delta) % bus_id:
                break
        else:
            return time_stamp


def solve_2(data):
    data = [(i, int(bus_id)) for i, bus_id in enumerate(data[1].split(',')) if bus_id != 'x']
    jump = data[0][1]
    time_stamp = 0
    for delta, bus_id in data[1:]:
        while (time_stamp + delta) % bus_id != 0:
            time_stamp += jump
        jump *= bus_id
    return time_stamp

test_data = '''939
17,x,13,19'''

with open('input/day_13.txt') as f:
    data = [line.rstrip() for line in f]
print(solve_2(data))
