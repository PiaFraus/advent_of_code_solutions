import itertools
import re
from itertools import product
from math import radians, sin, cos, sqrt
from collections import Counter, defaultdict, deque
from copy import copy, deepcopy
from functools import partial, reduce
from pprint import pprint
from timeit import timeit
from collections import Counter


def solve(data):
    decks = {}
    player = 1
    for line in data:
        if line.startswith('Player '):
            player = int(line[len('Player '):-1])
            continue
        if not line:
            continue
        decks.setdefault(player, []).append(int(line))
    while decks[1] and decks[2]:
        round(decks)
    winning_deck = decks[1] or decks[2]
    return sum((i+1)*c for i, c in enumerate(reversed(winning_deck)))

def round(decks):
    c1 = decks[1].pop(0)
    c2 = decks[2].pop(0)
    if c1 > c2:
        decks[1].extend([c1, c2])
    else:
        decks[2].extend([c2, c1])


def solve_2(data):
    decks = {}
    player = 1
    for line in data:
        if line.startswith('Player '):
            player = int(line[len('Player '):-1])
            continue
        if not line:
            continue
        decks.setdefault(player, []).append(int(line))
    game(decks[1], decks[2])
    winning_deck = decks[1] or decks[2]
    return sum((i+1)*c for i, c in enumerate(reversed(winning_deck)))

def game(deck1, deck2):
    _existing_states = set()
    while deck1 and deck2:
        game_state = (tuple(deck1), tuple(deck2))
        if game_state in _existing_states:
            return True
        _existing_states.add(game_state)
        c1, c2 = deck1.pop(0), deck2.pop(0)
        if c1 > len(deck1) or c2 > len(deck2):
            winner = c1 > c2
        else:
            winner = game(deck1[:c1], deck2[:c2])
        if winner:
            deck1.extend((c1, c2))
        else:
            deck2.extend((c2, c1))
    return bool(deck1)

test_data = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''

with open('input/day_22.txt') as f:
    data = [line.rstrip() for line in f]
    # data = [line.rstrip() for line in test_data.splitlines()]
# data = [list(line) for line in data]
print(solve_2(data))
