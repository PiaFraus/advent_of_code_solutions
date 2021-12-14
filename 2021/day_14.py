from collections import Counter
from itertools import pairwise


def solve(data):
    polymer = data[0]
    pairs = {}
    for line in data[2:]:
        left, right = line.split(' -> ')
        pairs[left] = right
    for step in range(1, 11):
        new = []
        last_c = None
        for c in polymer:
            if last_c:
                if last_c + c in pairs:
                    new.append(pairs[last_c + c])
            last_c = c
            new.append(c)
        polymer = ''.join(new)
        # print(f'After step {step}: {len(polymer)}')
    counter = Counter(polymer)
    return max(counter.values()) - min(counter.values())


def solve_2(data):
    polymer = data[0]
    rules = {}
    for line in data[2:]:
        left, right = line.split(' -> ')
        rules[tuple(left)] = (left[0], right), (right, left[1])
    counter = Counter(list(pairwise(polymer)))
    for step in range(1, 41):
        new = counter.copy()
        for pair, value in counter.items():
            if value and pair in rules:
                new[pair] -= value
                for new_pair in rules[pair]:
                    new[new_pair] += value
        counter = new

    letter_counter = Counter()
    for (a, b), value in counter.items():
        letter_counter[a] += value
        letter_counter[b] += value
    letter_counter[polymer[0]] += 1
    letter_counter[polymer[-1]] += 1
    return (max(letter_counter.values()) - min(letter_counter.values())) // 2


test_data = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''

if __name__ == '__main__':
    with open('input/day_14.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
# Not the 2959788056212
