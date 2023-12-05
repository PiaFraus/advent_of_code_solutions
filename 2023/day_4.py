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
    for line in data:
        card_number, numbers = line.removeprefix('Card ').split(': ')
        winning_numbers, card_numbers = numbers.split('|')
        winning_numbers = set(map(int, filter(bool, winning_numbers.strip().split(' '))))
        card_numbers = list(map(int, filter(bool, card_numbers.strip().split(' '))))
        won = sum(n in winning_numbers for n in card_numbers)
        if won:
            result += 1 << (won - 1)
    return result

def solve_2(data):
    c = Counter()
    max_card = len(data)
    for line in data:
        card_number, numbers = line.removeprefix('Card ').split(': ')
        card_number = int(card_number)
        c[card_number] += 1
        winning_numbers, card_numbers = numbers.split('|')
        winning_numbers = set(map(int, filter(bool, winning_numbers.strip().split(' '))))
        card_numbers = set(map(int, filter(bool, card_numbers.strip().split(' '))))
        won = sum(n in winning_numbers for n in card_numbers)
        for i in range(card_number + 1, min(card_number + won + 1, max_card + 1)):
            c[i] += c[card_number]
    return sum(c.values())


test_data = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

if __name__ == '__main__':
    with open('input/day_4.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
