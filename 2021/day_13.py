def process_and_fold(data):
    points = []
    folding = False
    for line in data:
        if not line:
            folding = True
            continue
        if not folding:
            points.append(tuple(map(int, line.split(','))))
        else:
            axis, value = line.removeprefix('fold along ').split('=')
            value = int(value)
            if axis == 'x':
                points = {((2 * value - x) if x > value else x, y) for x, y in points}
            else:
                points = {(x, (2 * value - y) if y > value else y) for x, y in points}
    return points


def solve(data):
    return len(process_and_fold(data))


def print_points(points):
    max_x, max_y = 0, 0
    for x, y in points:
        max_x, max_y = max(max_x, x), max(max_y, y)
    output = []
    for y in range(max_y + 1):
        output.append(['#' if (x, y) in points else '.' for x in range(max_x + 1)])
    return '\n'.join(''.join(row) for row in output)


def solve_2(data):
    return print_points(process_and_fold(data))


test_data = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''

if __name__ == '__main__':
    with open('input/day_13.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
