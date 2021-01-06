import itertools
import re
from itertools import product
from math import radians, sin, cos
from collections import Counter, defaultdict
from copy import copy, deepcopy
from functools import partial, reduce
from pprint import pprint
from timeit import timeit


def solve(data):
    lines = iter(data)
    rules = {}
    for line in lines:
        if not line:
            break
        rule_number, rule = line.split(': ')
        rules[int(rule_number)] = rule
    messages = list(lines)
    return len(parse_rules("0", rules).intersection(messages))

def solve_2(data):
    lines = iter(data)
    rules = {}
    for line in lines:
        if not line:
            break
        rule_number, rule = line.split(': ')
        rules[int(rule_number)] = rule
    messages = list(lines)
    rules[8] = "42 | 42 8"
    rules[11] = "42 31 | 42 11 31"
    rule_42 = parse_rules("42",  rules)
    rule_31 = parse_rules("31",  rules)
    result = 0
    for message in messages:
        m = message
        c = 0
        while any(m.endswith(r) for r in rule_31):
            m = m[:-8]
            c += 1
        if not c:
            continue
        while any(m.endswith(r) for r in rule_42):
            m = m[:-8]
            c -= 1
        if c >= 0 or m:
            continue
        result += 1
    return result

def solve(data):
    lines = iter(data)
    rules = {}
    for line in lines:
        if not line:
            break
        rule_number, rule = line.split(': ')
        rules[int(rule_number)] = rule
    messages = list(lines)
    return len(parse_rules("0", rules).intersection(messages))

_cache = {}
def parse_rules(rules: str, all_rules):
    if rules in _cache:
        return _cache[rules]
    if rules.startswith('"'):
        _cache[rules] = {rules[1]}
    elif ' | ' in rules:
        choices = rules.split(' | ')
        _cache[rules] = {y for x in product(*(parse_rules(c, all_rules) for c in choices)) for y in x}
    elif ' ' in rules:
        sequentials = rules.split(' ')
        _cache[rules] = set(''.join(x) for x in product(*(parse_rules(s, all_rules) for s in sequentials)))
    else:
        _cache[rules] = parse_rules(all_rules[int(rules)], all_rules)
    return _cache[rules]






test_data = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
'''

with open('input/day_19.txt') as f:
    data = [line.rstrip() for line in f]
    # data = [line.rstrip() for line in test_data.splitlines()]
# data = [list(line) for line in data]
print(solve(data))
