import itertools


def simulate_sand(blocked, floor):
    depth = max(key[1] for key in blocked)
    if floor:
        depth += 2
    droplet_x = 500
    for droplet_y in range(1, depth):
        for path in (0, -1, 1):
            if (droplet_x + path, droplet_y) not in blocked:
                droplet_x += path
                break
        else:
            return droplet_x, droplet_y - 1
    if floor:
        return droplet_x, depth - 1
    return None


def solve(data, floor=False):
    rocks = set()
    for line in data:
        points = line.split(' -> ')
        walls = [tuple(map(int, p.split(','))) for p in points]
        for (a, b), (c, d) in itertools.pairwise(walls):
            dx = 0 if a == c else abs(c - a) // (c - a)
            dy = 0 if b == d else abs(d - b) // (d - b)
            for i in range(max(abs(c - a), abs(d - b)) + 1):
                rocks.add((a + i * dx, b + i * dy))
    sand = set()
    draw_area(rocks, sand)
    for i in itertools.count():
        new_piece = simulate_sand(rocks | sand, floor=floor)
        if new_piece is None:
            return i
        sand.add(new_piece)
    draw_area(rocks, sand)
    return 0


def draw_area(rocks, sand):
    print('-' * 30)
    edges = min(x for x, y in rocks), max(x for x, y in rocks), min(y for x, y in rocks), max(y for x, y in rocks),
    for i in range(edges[2], edges[3] + 1):
        for j in range(edges[0], edges[1] + 1):
            print('#' if (j, i) in rocks else 'O' if (j, i) in sand else '.', end = '')
        print()


def solve_2(data):
    return solve(data, True)


test_data = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''

# Not 346
if __name__ == '__main__':
    with open('input/day_14.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    # print(solve(data))
    print(solve_2(data))
