import itertools
import re
from itertools import product
from math import radians, sin, cos, sqrt
from collections import Counter, defaultdict
from copy import copy, deepcopy
from functools import partial, reduce
from pprint import pprint
from timeit import timeit
from collections import Counter


def solve(data):
    allergens_to_ingrediens = {}
    all_ingredients = set()
    ingredients_counter = Counter()
    for line in data:
        food, allergens = line.split(' (contains ')
        ingredients = set(food.split(' '))
        for i in ingredients:
            ingredients_counter[i] += 1
        all_ingredients.update(ingredients)
        allergens = allergens[:-1].split(', ')
        for a in allergens:
            allergens_to_ingrediens.setdefault(a, copy(ingredients)).intersection_update(ingredients)
    clean_ingredients = all_ingredients - set.union(*allergens_to_ingrediens.values())
    return sum(ingredients_counter[i] for i in clean_ingredients)

def solve_2(data):
    allergens_to_ingrediens = {}
    all_ingredients = set()
    ingredients_counter = Counter()
    for line in data:
        food, allergens = line.split(' (contains ')
        ingredients = set(food.split(' '))
        for i in ingredients:
            ingredients_counter[i] += 1
        all_ingredients.update(ingredients)
        allergens = allergens[:-1].split(', ')
        for a in allergens:
            allergens_to_ingrediens.setdefault(a, copy(ingredients)).intersection_update(ingredients)
    defined = {}
    unsolved = copy(allergens_to_ingrediens)
    found = set()
    while unsolved:
        found_a, found_i = None, None
        for a, i in unsolved.items():
            if len(i) == 1:
                found_a, found_i = a, i.pop()
                break
        defined[found_a] = found_i
        found.add(found_i)
        unsolved.pop(found_a)
        unsolved = {a: (i-found) for a, i in unsolved.items()}
    return ','.join((x[1] for x in sorted(defined.items(), key=lambda x: x[0])))



test_data = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''

with open('input/day_21.txt') as f:
    data = [line.rstrip() for line in f]
    # data = [line.rstrip() for line in test_data.splitlines()]
# data = [list(line) for line in data]
print(solve_2(data))
