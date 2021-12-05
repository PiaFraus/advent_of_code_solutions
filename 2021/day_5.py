from collections import Counter


def solve(data, diagonals=False):
    counter = Counter()
    for line in data:
        left, right = line.split('->')
        x = list(map(int, left.split(',')))
        y = list(map(int, right.split(',')))
        step = [-1 if x[i] > y[i] else 0 if x[i] == y[i] else 1 for i in [0, 1]]
        if not diagonals and 0 not in step:
            continue
        while True:
            counter[x[0], x[1]] += 1
            if x == y:
                break
            x[0] += step[0]
            x[1] += step[1]
        pass
    return len([v for v in counter.values() if v > 1])


def solve_2(data, diagonals=True):
    return solve(data, diagonals=True)

test_data = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

if __name__ == '__main__':
    with open('input/day_5.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
