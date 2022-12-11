import itertools
from collections import Counter
from copy import deepcopy

def format_data(data):
    return "\n".join("".join(line) for line in data)

def solve(data):
    counter = Counter()
    result, a, b = 0, 0, 0
    data = list(map(list, data))
    moved = [None, None]
    for step in itertools.count():
        # print(f'After {step/2} step:\n{format_data(data)}')
        turn = step % 2
        moved[turn] = False
        next_data = deepcopy(data)
        for i, line in enumerate(data):
            for j, value in enumerate(line):
                next_i = (i + turn) % len(data)
                next_j = (j + 1 - turn) % len(data[0])
                if data[next_i][next_j] == '.' and data[i][j]=='>v'[turn]:
                    next_data[next_i][next_j] = data[i][j]
                    next_data[i][j] = '.'
                    moved[turn] = True
        data = next_data
        if moved[0] == moved[1] == False:
            return (step//2) + 1
    return result


def solve_2(data):
    counter = Counter()
    result, a, b = 0, 0, 0
    for line in data:
        pass
    return result


test_data = '''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>'''

if __name__ == '__main__':
    with open('input/day_25.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
