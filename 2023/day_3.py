import re
from collections import Counter, defaultdict


def solve(data):
    counter = Counter()
    result, a, b = 0, 0, 0
    for i, line in enumerate(data):
        for re_iter in re.finditer('\d+', line):
            left, right = re_iter.span()
            hit = False
            for ny in range(max(i - 1, 0), min(i + 2, len(data))):
                for nx in range(max(left - 1, 0), min(right + 1, len(line))):
                    if ny == i and left <= nx < right:
                        continue
                    if data[ny][nx] != '.':
                        result += int(re_iter.group())
                        hit = True
                        break
                if hit:
                    break
    return result


def solve_2(data):
    star_neighbouring_numbers = defaultdict(list)
    result = 0
    for i, line in enumerate(data):
        for re_iter in re.finditer('\d+', line):
            left, right = re_iter.span()
            for ny in range(max(i - 1, 0), min(i + 2, len(data))):
                for nx in range(max(left - 1, 0), min(right + 1, len(line))):
                    if ny == i and left <= nx < right:
                        continue
                    if data[ny][nx] == '*':
                        star_neighbouring_numbers[ny, nx].append(int(re_iter.group()))
    for values in star_neighbouring_numbers.values():
        if len(values) == 2:
            result += values[0] * values[1]
    return result


test_data = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

if __name__ == '__main__':
    with open('input/day_3.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
