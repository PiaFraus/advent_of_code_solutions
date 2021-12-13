from collections import defaultdict

def traverse(paths, current, lower_caves_max=1):
    if current[-1] == 'end':
        return 1
    result = 0
    options = paths[current[-1]]
    for o in options:
        if o.islower() and o in current:
            if lower_caves_max > 1:
                result += traverse(paths, current + [o], lower_caves_max - 1)
            continue
        result += traverse(paths, current + [o], lower_caves_max)
    return result


def solve(data, lower_caves_max=1):
    paths = defaultdict(list)
    for line in data:
        a, b = line.split('-')
        paths[a].append(b)
        if a != 'start':
            paths[b].append(a)
    paths.pop('end')
    current = ['start']
    return traverse(paths, current, lower_caves_max)


def solve_2(data):
    return solve(data, lower_caves_max=2)


test_data = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

if __name__ == '__main__':
    with open('input/day_12.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    # print(solve(data))
    print(solve_2(data))
