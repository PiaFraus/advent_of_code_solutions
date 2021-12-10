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

PAIRS = dict(zip('[{<(', ']}>)'))

def solve(data):
    counter = Counter()
    for line in data:
        stack = deque()
        for c in line:
            if c in '[{<(':
                stack.append(c)
            elif c != PAIRS[stack.pop()]:
                counter[c] += 1
                break
    return counter[')']*3 + counter[']']*57+counter['}']*1197+counter['>']*25137

def solve_2(data):
    result = []
    for line in data:
        stack = deque()
        for c in line:
            if c in '[{<(':
                stack.append(c)
            elif c != PAIRS[stack.pop()]:
                break
        else:
            score = 0
            for c in reversed(stack):
                score = 5 * score + ')]}>'.index(PAIRS[c]) + 1
            result.append(score)
    return sorted(result)[len(result)//2]


test_data = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''

if __name__ == '__main__':
    with open('input/day_10.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
