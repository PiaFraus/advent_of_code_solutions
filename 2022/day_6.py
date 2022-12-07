import itertools
from collections import Counter


def solve(data, n=4):
    for i in range(len(data) - n):
        if len(set(data[i:i + n])) == n:
            return i + n


def solve_2(data):
    return solve(data, n=14)

test_data = '''nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'''

if __name__ == '__main__':
    with open('input/day_6.txt') as f:
        data = f.read()
        # data = test_data
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
