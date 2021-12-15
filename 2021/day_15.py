import heapq
from collections import Counter


def neighbours(x, y, limit_x, limit_y):
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        if 0 <= dx + x <= limit_x and 0 <= dy + y <= limit_y:
            yield x + dx, y + dy


def solve(data):
    data = [list(map(int, line)) for line in data]
    dimensions = len(data)-1, len(data[0])-1
    edge = [(0, 0, 0)]
    passed = set()
    while True:
        d, x, y = heapq.heappop(edge)
        if (x, y) == dimensions:
            return d
        for ni, nj in neighbours(x, y, *dimensions):
            if (ni, nj) not in passed:
                passed.add((ni, nj))
                heapq.heappush(edge, (d + data[ni][nj], ni, nj))

def solve_2(data):
    data = [list(map(int, line)) for line in data]
    mi, mj = len(data), len(data[0])
    data = [[(data[i % mi][j % mj] + i // mi + j //mj - 1) % 9 + 1 for j in range(5*mj)] for i in range(5*mi)]
    return solve(data)


test_data = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''

if __name__ == '__main__':
    with open('input/day_15.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line) for line in data]

    print(solve(data))
    print(solve_2(data))
