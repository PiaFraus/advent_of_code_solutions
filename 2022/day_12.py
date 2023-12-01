import itertools
import string

height_lookup = {c: i for i, c in enumerate(string.ascii_lowercase)}
height_lookup['E'] = height_lookup['z']
height_lookup['S'] = height_lookup['a']


def valid_neighbours(data, x, y):
    current_height = height_lookup[data[x][y]]
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(data) and 0 <= ny < len(data[0]) and height_lookup[data[nx][ny]] <= current_height + 1:
            yield nx, ny


def solve(data, starting_chars='S'):
    next_to_check = set()
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c in starting_chars:
                next_to_check.add((i, j))
    visited = {}
    for step in itertools.count():
        for to_check in next_to_check.copy():
            visited[to_check] = step
            if data[to_check[0]][to_check[1]] == 'E':
                return step
            for neighbour in valid_neighbours(data, *to_check):
                if neighbour in visited:
                    continue
                next_to_check.add(neighbour)
    return None


def solve_2(data):
    return solve(data, starting_chars='Sa')


test_data = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

# 423 doesn't work!
# Neither is 369
if __name__ == '__main__':
    with open('input/day_12.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
