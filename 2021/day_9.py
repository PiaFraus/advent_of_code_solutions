import heapq
from functools import reduce


def neighbours(x, y, limit_x, limit_y):
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        if 0 <= dx + x < limit_x and 0 <= dy + y < limit_y:
            yield x + dx, y + dy

def solve(data):
    result = []
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if all(data[nx][ny] > value for nx, ny in neighbours(i, j, len(data), len(row))):
                result.append(value)
    return sum(result) + len(result)


def solve_2(data):
    result = []
    processed = set()
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            if value == 9 or (i, j) in processed:
                continue
            unprocessed_basin = [(i, j)]
            processed_basin = set()
            while unprocessed_basin:
                explore = unprocessed_basin.pop()
                for nx, ny in neighbours(*explore, len(data), len(row)):
                    if data[nx][ny] == 9 or (nx, ny) in processed_basin:
                        continue
                    unprocessed_basin.append((nx, ny))
                processed_basin.add(explore)
            processed |= processed_basin
            result.append(len(processed_basin))
    result = heapq.nlargest(3, result)
    return reduce(lambda x, y: x*y, result, 1)


test_data = '''2199943210
3987894921
9856789892
8767896789
9899965678'''

if __name__ == '__main__':
    with open('input/day_9.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]
    data = [list(map(int, line)) for line in data]

    print(solve(data))
    print(solve_2(data))
