from collections import Counter
from copy import copy
from functools import partial


def solve(data, preamble=25, *args, **kwargs):
    numbers = data[:preamble]
    for number in data[preamble:]:
        if not validate(numbers, number):
            return number
        numbers.pop(0)
        numbers.append(number)
    return None

def validate(numbers, value):
    sn = set(numbers)
    for n in numbers:
        if value - n in sn:
            return True
    return False

def solve2(data, search_sum, *args, **kwargs):
    for i, number in enumerate(data):
        s = number
        for j, value in enumerate(data[i+1:]):
            s += value
            if s == search_sum:
                search_list = data[i:i+j+2]
                return search_list, min(search_list), max(search_list), min(search_list) + max(search_list)
            if s > search_sum:
                break
    return None


test_data = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''

with open('input/day_10.txt') as f:
    # data = [line.rstrip() for line in f]
    data = [line.rstrip() for line in test_data.splitlines()]

data = list(map(int, data))
data = sorted(data)
c = {}
previous = data[0]
for x in data[1:]:
    c[x-previous] = c.get(x-previous, 0) + 1
    previous = x
print((c[1]+1)*(c[3]+1))
data = [0] + data + [max(data) + 3]
available = {}
for x in data:
    for y in data:
        if 0 < y - x < 4:
            available.setdefault(x, []).append(y)
cache = {}
def rec(value):
    if value in cache:
        return cache[value]
    if value == data[-1]:
        return 1
    cache[value] = sum(rec(x) for x in available[value])
    return cache[value]
print(rec(0))

# results = solve(data)
print(f'{c} {(c[1])*(c[3])}')
# print(solve2(data, results))
