from copy import copy

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

test_data = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

with open('input/day_7.txt') as f:
    data = [line.rstrip() for line in f]
    # data = [line.rstrip() for line in test_data.splitlines()]
results = solve(data, 'shiny gold')
print(results)
