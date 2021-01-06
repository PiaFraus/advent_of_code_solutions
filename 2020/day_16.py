import itertools
from math import radians, sin, cos
from collections import Counter
from copy import copy, deepcopy
from functools import partial, reduce
from pprint import pprint
from timeit import timeit


def solve(data, num):
    stage = 0
    validators = {}
    global_ticket_validation = {}
    for line in data:
        if stage == 0:
            if not line:
                stage = 1
                continue
            kw, ranges = process_line(line)
            validators[kw] = list(ranges)
        elif stage == 1:
            if not line:
                stage = 2
                continue
            if line == 'your ticket:':
                continue
            your_ticket = list(map(int, line.split(',')))
        else:
            if line == 'nearby tickets:':
                continue
            ticket = list(map(int, line.split(',')))
            ticket_validation = {}
            for field_num, value in enumerate(ticket):
                valid = False
                for kw, validator in validators.items():
                    valids = [min_r <= value <= max_r for min_r, max_r in validator]
                    if any(valids):
                        valid = True
                        ticket_validation.setdefault(kw, set()).add(field_num)
                if not valid:
                    break
            else:
                if not global_ticket_validation:
                    global_ticket_validation = ticket_validation
                else:
                    for kw, valid_fields in ticket_validation.items():
                        global_ticket_validation[kw] &= valid_fields
    result_validator = {}
    while True:
        for kw, potentials in global_ticket_validation.items():
            if len(potentials) == 1:
                found = potentials.pop()
                result_validator[kw] = found
                break
        else:
            break
        for kw, potentials in global_ticket_validation.items():
            if found in potentials:
                potentials.remove(found)
    result = 1
    for kw, field_num in result_validator.items():
        if kw.startswith('departure'):
            result *= your_ticket[field_num]
    return result


def process_line(line):
    kw, values = line.split(':')
    ranges = values.split(' or ')
    return kw, [tuple(map(int, r.split('-'))) for r in ranges]


test_data = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''

with open('input/day_16.txt') as f:
    data = [line.rstrip() for line in f]
    # data = [line.rstrip() for line in test_data.splitlines()]
data = [line for line in data]
print(solve(data, None))
print(timeit(partial(solve, data, None), number=1))
