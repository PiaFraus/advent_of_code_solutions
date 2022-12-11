from collections import Counter


def solve(data):
    result, a, b = 0, 0, 0
    x = 1
    cycle = 0
    for line in data:
        if line == 'noop':
            cycle += 1
            if (cycle - 20) % 40 == 0:
                result += cycle * x
                print(f'1 {cycle=}, {x=}, {result=}, added={cycle * x}')
            continue
        dx = int(line.removeprefix('addx '))
        cycle += 2
        if (cycle - 20) % 40 == 0:
            result += cycle * x
            print(f'2 {cycle=}, {x=}, {result=}, added={cycle * x}')
        if (cycle - 20) % 40 == 1:
            result += (cycle - 1) * x
            print(f'3 {cycle=}, {x=}, {result=}, added={(cycle - 1) * x}')
        x += dx

    return result


def solve_2(data):
    x = 1
    cycle = 0
    result = []
    for line in data:
        result += '#' if abs((cycle % 40) - x) < 2 else '.'
        cycle += 1
        if line == 'noop':
            continue
        result += '#' if abs((cycle % 40) - x) < 2 else '.'
        cycle += 1
        x += int(line.removeprefix('addx '))

    for i in range(len(result) // 40):
        print(''.join(result[i*40:i*40 + 40]))
    return result



test_data = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''

if __name__ == '__main__':
    with open('input/day_10.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
