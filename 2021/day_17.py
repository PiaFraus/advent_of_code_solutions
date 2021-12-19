from itertools import count

# It goes up by A it goes down by A
from math import sqrt


def solve(data):
    x, y = data[0].removeprefix('target area: x=').split(', ')
    x0, x1 = map(int, x.removeprefix('x=').split('..'))
    y0, y1 = map(int, y.removeprefix('y=').split('..'))
    global_max_y = 0
    for dx0 in range(int(sqrt(2 * x0)), x1 + 1):
        for dy0 in range(-abs(y0), abs(y0)):
            dx, dy = dx0, dy0
            pos = 0, 0
            max_y = 0
            for t in count():
                pos_x = dx0 * (t + 1) - t * (t + 1) // 2
                pos_y = dy0 * (t + 1) - t * (t + 1) // 2
                pos = pos[0] + dx, pos[1] + dy
                dx -= 1 if dx > 0 else 0
                dy -= 1
                max_y = max(max_y, pos[1])
                if x0 <= pos[0] <= x1 and y0 <= pos[1] <= y1:
                    global_max_y = max(max_y, global_max_y)
                    break
                if pos_y < y0 or pos_x > x1:
                    break
    return global_max_y


def solve_2(data):
    x, y = data[0].removeprefix('target area: x=').split(', ')
    x0, x1 = map(int, x.removeprefix('x=').split('..'))
    y0, y1 = map(int, y.removeprefix('y=').split('..'))
    c = 0
    results = []
    for dx0 in range(int(sqrt(2 * x0)), x1 + 1):
        for dy0 in range(-abs(y0), abs(y0)):
            dx, dy = dx0, dy0
            pos = 0, 0
            for t in count():
                pos_x = dx0 * (t + 1) - t * (t + 1) // 2
                pos_y = dy0 * (t + 1) - t * (t + 1) // 2
                pos = pos[0] + dx, pos[1] + dy
                dx -= 1 if dx > 0 else 0
                dy -= 1
                if x0 <= pos[0] <= x1 and y0 <= pos[1] <= y1:
                    print(f'{dx0=}, {dy0=}')
                    c += 1
                    results.append((dx0, dy0))
                    break
                if pos_y < y0 or pos_x > x1:
                    break
    return c

test_data = '''target area: x=20..30, y=-10..-5'''

if __name__ == '__main__':
    with open('input/day_17.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
