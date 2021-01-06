import itertools
from math import radians, sin, cos
from collections import Counter
from copy import copy, deepcopy
from functools import partial, reduce
from pprint import pprint
from timeit import timeit


def solve(data, *args, **kwargs):
    mem = {}
    mask_1, mask_0 = None, None
    for line in data:
        if line.startswith('mask = '):
            mask = line[len('mask = '):]
            mask_1 = int(mask.replace('X', '0'), 2) 
            mask_0 = int(mask.replace('X', '1'), 2)
        else:
            start, end = line.split('] = ')
            mem_pos = int(start[4:])
            value = int(end)
            result = (value | mask_1) & mask_0
            mem[mem_pos] = result
            print(bin(result))
    return sum(mem.values())

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))

def solve_2(data, *args, **kwargs):
    mem = {}
    mask = None
    for line in data:
        if line.startswith('mask = '):
            mask = line[len('mask = '):]
        else:
            start, end = line.split('] = ')
            value = int(end)
            mem_pos_initial = int(start[4:])
            ones = int(mask.replace('X', '0'), 2)
            resets = int(mask.replace('0', '1').replace('X', '0'), 2)
            mem_pos_result = (mem_pos_initial & resets) | ones
            positions_of_x = [i for i, c in enumerate(mask) if c == 'X']
            for bits in powerset(positions_of_x):
                mem_pos = mem_pos_result
                for bit_pos in bits:
                    mem_pos |= 2**(len(mask) - 1 - bit_pos)
                print(mem_pos, bin(mem_pos))
                mem[mem_pos] = value
    return sum(mem.values())


test_data = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
'''

with open('input/day_14.txt') as f:
    data = [line.rstrip() for line in f]
    # data = [line.rstrip() for line in test_data.splitlines()]
print(solve_2(data))
