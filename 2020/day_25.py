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


def solve(door_key, key_key):
    value = 1
    for i in itertools.count():
        value *= 7
        value %= 20201227
        if value == door_key:
            return handshake(key_key, i+1)

def handshake(subject, secret):
    value = 1
    for _ in range(secret):
        value *= subject
        value = value % 20201227
    return value

test_data = ''''''

print(solve(14788856, 19316454))
# print(solve_2(data))

# Not 5764801