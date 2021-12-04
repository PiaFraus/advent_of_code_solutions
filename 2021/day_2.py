from collections import defaultdict


def solve(data):
    result = defaultdict(int)
    for line in data:
        command, value = line.split()
        result[command] += int(value)
    return result['forward'] * (result['down'] - result['up'])


def solve_2(data):
    aim, x, y = 0, 0, 0
    for line in data:
        command, value = line.split()
        value = int(value)
        match command:
            case 'up':
                aim -= value
            case 'down':
                aim += value
            case 'forward':
                x += value
                y += value * aim
    return x * y


test_data = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''

if __name__ == '__main__':
    with open('input/day_2.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line) for line in data]

    # print(solve(data))
    print(solve_2(data))
