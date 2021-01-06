import itertools
import re
from itertools import product
from math import radians, sin, cos, sqrt
from collections import Counter, defaultdict, deque, namedtuple
from copy import copy, deepcopy
from functools import partial, reduce
from pprint import pprint
from timeit import timeit
from collections import Counter


def solve(data):
    cups = list(map(int, data[0]))
    max_cup = max(cups)
    current_cup = 0
    destination_cup = 0
    for m in range(100):
        print(f'Move {m+1}\ncups:{cups}')
        removed_cups, cups[1:4] = cups[1:4], []
        print(f'pickup:{removed_cups}')
        for i in range(1, 100):
            try:
                destination_cup = (cups[current_cup] - i) % max_cup or max_cup
                destination_cup_index = cups.index(destination_cup)
                break
            except ValueError:
                continue
        cups[destination_cup_index + 1:destination_cup_index+1] = removed_cups
        print(f'destination={destination_cup}')
        cups = cups[1:] + cups[:1]

    index_of_1 = cups.index(1)
    return ''.join(map(str, cups[index_of_1+1:] + cups[:index_of_1]))

linked_list = namedtuple('linked_list', 'value next')


def solve_2(data, number_of_cups):
    cups = list(map(int, data[0]))
    next_cups = {}
    current_cup = cups[0]
    prev_cup = cups[0]
    for cup in itertools.chain(cups, range(max(cups)+1, number_of_cups + 1)):
        next_cups[prev_cup] = cup
        prev_cup = cup
    next_cups[number_of_cups] = cups[0]
    for m in range(10000000):
        picked_cup0 = next_cups[current_cup]
        picked_cup1 = next_cups[picked_cup0]
        picked_cup2 = next_cups[picked_cup1]
        next_cups[current_cup] = next_cups[picked_cup2]
        for i in range(1, 5):
            destination_cup = (current_cup - i) % number_of_cups or number_of_cups
            if destination_cup not in (picked_cup0, picked_cup1, picked_cup2):
                break
        next_cups[picked_cup2] = next_cups[destination_cup]
        next_cups[destination_cup] = picked_cup0
        current_cup = next_cups[current_cup]
    first_star = next_cups[1]
    second_star = next_cups[first_star]
    return first_star, second_star, first_star * second_star

test_data = '''253149867'''

with open('input/day_23.txt') as f:
    # data = [line.rstrip() for line in f]
    data = [line.rstrip() for line in test_data.splitlines()]
# data = [list(line) for line in data]
# print(solve(data))
print(solve_2(data, 1000000))

# Not 86349527