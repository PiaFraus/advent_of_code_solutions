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


test_data = ''''''

with open('input/day_9.txt') as f:
    data = [line.rstrip() for line in f]
    # data = [line.rstrip() for line in test_data.splitlines()]
# code = [line.split() for line in data]
# code = [(op, int(arg)) for op, arg in code]

data = list(map(int, data))
# print(solve(data, pa=25))
print(solve2(data,))
