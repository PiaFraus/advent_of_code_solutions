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
        letters = [c for c in line if c in "0123456789"]
        number = int(letters[0]+letters[-1])
        result += number
    return result

def solve_2(data):
    result = 0
    number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in data:
        positions_left = {line.find(word): i for i, word in enumerate(number_words) if word in line}
        positions_right = {line.rfind(word): i for i, word in enumerate(number_words) if word in line}
        positions_left.update({line.find(str(i)): i for i in range(10) if str(i) in line})
        positions_right.update({line.rfind(str(i)): i for i in range(10) if str(i) in line})
        number = positions_left[min(positions_left)] * 10 + positions_right[max(positions_right)]
        result += number
    return result

def red(data):
    result = 0
    for x in data:
        for i, s in enumerate(['one','two','three','four', 'five', 'six', 'seven', 'eight', 'nine']):
            x = x.replace(s, s[0] + str(i+1) + s[-1])
        z = re.findall(r'\d', x)
        number = int(z[0]+z[-1])
        print(x, number)
        result += number
    return result

test_data = '''one1two
two1two
313
'''

if __name__ == '__main__':
    with open('input/day_1.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
    # print(red(data))
