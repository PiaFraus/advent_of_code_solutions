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
    result = 0
    limits = {'red': 12, 'green': 13, 'blue': 14}
    for line in data:  # type: str
        game_part, sets_part = line.split(':')
        game_number = int(game_part.removeprefix('Game '))
        for s in sets_part.split(';'):
            set_counter = Counter()
            for cubes in s.split(','):
                number, color = cubes.strip().split(' ')
                set_counter[color] += int(number)
            if any(number > limits[color] for color, number in set_counter.items()):
                break
        else:
            result += game_number
    return result

def solve_2(data):
    result = 0
    for line in data:  # type: str
        game_part, sets_part = line.split(':')
        max_counter = Counter()
        for s in sets_part.split(';'):
            for cubes in s.split(','):
                number, color = cubes.strip().split(' ')
                max_counter[color] = max(max_counter[color], int(number))
        power = 1
        for v in max_counter.values():
            power *= v
        result += power
    return result


test_data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

if __name__ == '__main__':
    with open('input/day_2.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
