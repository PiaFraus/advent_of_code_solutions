from copy import copy
from functools import partial


def solve(data, bag, *args, **kwargs):
    result = 0
    tree = {}
    for line in data:
        parent, children_to_numbers = parse(line)
        tree[parent] = children_to_numbers
    children = list(tree[bag].items())
    while children:
        child, number = children.pop()
        new_children = tree[child]
        children.extend((k, v * number) for k, v in new_children.items())
        result += number

    return result


def parse(line):
    parent, children = line.split(' bags contain ')
    children_bags = children.split(',')
    children_to_numbers = {}
    for cb in children_bags:
        if cb == 'no other bags.':
            continue
        number, first, second, _ = cb.strip().split(' ', 3)
        c = first + ' ' + second
        children_to_numbers[c] = int(number)
    return parent, children_to_numbers


def solve(code):
    ip, acc = 0, 0
    visited = set()
    while ip not in visited:
        if ip == len(code):
            return True, ip, acc
        visited.add(ip)
        op, arg = code[ip]
        if op == 'jmp':
            ip += arg
            continue
        if op == 'acc':
            acc += arg
        ip += 1
    return False, ip, acc


def better_complexity_solution(code):
    jmp_table = {ip: (ip + arg if op == 'jmp' else ip + 1) for ip, (op, arg) in enumerate(code)}
    reversed_jmp_table = {}
    for jmp_from, jmp_to in jmp_table.items():
        reversed_jmp_table.setdefault(jmp_to, []).append(jmp_from)

    finish_line_nodes = set()
    nodes_to_check = [len(code)]
    while nodes_to_check:  # always unique and less then n
        node = nodes_to_check.pop()
        if node in finish_line_nodes:
            continue
        finish_line_nodes.add(node)  # constant
        nodes_to_check.extend(reversed_jmp_table.get(node, ()))  # <- Strictly speaking this makes it O(n^2) but
        # it easily can be refactored to store list of list instead of extending and looping over them can still be O(n)
        # also I believe since at the end we are limited into the amount of nodes_to_check - we are still bound by O(n)

    ip, acc = 0, 0
    fixed = False
    visited = set()
    while ip not in visited:
        if ip == len(code):
            return True, ip, acc
        visited.add(ip)
        op, arg = code[ip]
        if op == 'jmp':
            if not fixed and ip + 1 in finish_line_nodes:
                fixed = True
                ip += 1
            else:
                ip += arg
            continue
        if op == 'nop' and not fixed and ip + arg in finish_line_nodes:
            ip += arg
            continue
        if op == 'acc':
            acc += arg
        ip += 1
    return False, ip, acc


def brute_force(code):
    attempts = 0
    for i, (op, arg) in enumerate(code):
        new_code = code[:]
        if op == 'jmp':
            new_code[i] = 'nop', arg
        elif op == 'nop':
            new_code[i] = 'jmp', arg
        else:
            continue
        attempts += 1
        solved, ip, acc = solve(new_code)
        if solved:
            return (i, ip, acc, attempts)


test_data = '''...'''

with open('input/day_8.txt') as f:
    data = [line.rstrip() for line in f]
    # data = [line.rstrip() for line in test_data.splitlines()]
code = [line.split() for line in data]
code = [(op, int(arg)) for op, arg in code]


print(brute_force(code))
print(better_complexity_solution(code))

import timeit
print(timeit.timeit(partial(brute_force, code), number=50))
print(timeit.timeit(partial(better_complexity_solution, code), number=50))