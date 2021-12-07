def solve(data):
    numbers = list(map(int, data[0].split(',')))
    target = 1e10
    for n in range(max(numbers)):
        target = min(target, sum(abs(x-n) for x in numbers))
    return target

def solve_2(data):
    numbers = list(map(int, data[0].split(',')))
    target = 1e10
    for n in range(max(numbers)):
        target = min(target, sum(abs(x-n)*(abs(x-n)+1)/2for x in numbers))
    return target

test_data = '''16,1,2,0,4,2,7,1,2,14'''

if __name__ == '__main__':
    with open('input/day_7.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
