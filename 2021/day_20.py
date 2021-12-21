from copy import copy


def neighbours(x, y):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            yield x + dx, y + dy

def enhance(image_enhancement_alg, lighted, bound_x, bound_y, outside_bound=0):
    new_lighted = copy(lighted)
    a = [x for x,y in lighted]
    b = [y for x,y in lighted]
    new_bound_x = min(a)-1, max(a)+2
    new_bound_y = min(b)-1, max(b)+2
    for i in range(*new_bound_x):
        for j in range(*new_bound_y):
            ix = int(''.join(('1' if (x, y) in lighted or (outside_bound and (x not in range(*bound_x) or y not in range(*bound_y)))
                              else '0' for x, y in neighbours(i, j))), 2)
            if image_enhancement_alg[ix] == '#':
                new_lighted.add((i, j))
            else:
                new_lighted.discard((i, j))
    return new_lighted, new_bound_x, new_bound_y

def print_image(lighted, bound_x, bound_y):
    output = []
    for i in range(*bound_x):
        output.append(''.join('#' if (i,j) in lighted else '.' for j in range(*bound_y)))
    return '\n'.join(output)

def solve(data, enhancements=2):
    image_enhancement_alg = data[0]
    lighted = set()
    for i, line in enumerate(data[2:]):
        for j, value in enumerate(line):
            if value == '#':
                lighted.add((i, j))
    bound_x = 0, len(data)-2
    bound_y = 0, len(data[2])
    outside_bound_value = 0
    for i in range(enhancements):
        lighted, bound_x, bound_y = enhance(image_enhancement_alg, lighted, bound_x, bound_y, outside_bound=outside_bound_value)
        outside_bound_value = (i+1) % 2 if image_enhancement_alg[0] == '#' else 0
    print(print_image(lighted, bound_x, bound_y))
    return len(lighted)


def solve_2(data):
    return solve(data, enhancements=50)


test_data = '''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###'''

if __name__ == '__main__':
    with open('input/day_20.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))

# 47886 is wrong