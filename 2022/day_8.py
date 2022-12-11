import itertools


def solve(data):
    result = 0
    for i, line in enumerate(data):
        if i == 0 or i == len(line) - 1:
            result += len(line)
            continue
        for j, c, in enumerate(line):
            if j == 0 or j == len(data) - 1:
                result += 1
                continue
            if all(data[ti][j] < c for ti in range(i)):
                result += 1
            elif all(data[ti][j] < c for ti in range(i + 1, len(data))):
                result += 1
            elif all(data[i][tj] < c for tj in range(j)):
                result += 1
            elif all(data[i][tj] < c for tj in range(j + 1, len(line))):
                result += 1
    return result

def find_higher(data, x, y, dx, dy):
    for t in itertools.count(1):
        nx, ny = x + t * dx, y + t * dy
        if not ((0 <= nx < len(data)) and (0 <= ny < len(data[nx]))):
            return t - 1
        if data[nx][ny] >= data[x][y]:
            return t

def solve_2(data):
    result, a, b = 0, 0, 0
    for i, line in enumerate(data):
        for j, c, in enumerate(line):
            up = find_higher(data, i, j, -1, 0)
            down = find_higher(data, i, j, 1, 0)
            left = find_higher(data, i, j, 0, -1)
            right = find_higher(data, i, j, 0, 1)
            result = max(result, up * down * left * right)
            print(f'{up * down * left * right:2}', end='')
        print()
    return result


test_data = '''30373
25512
65332
33549
35390'''

if __name__ == '__main__':
    with open('input/day_8.txt') as f:
        # data = [line.rstrip() for line in f]
        data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
