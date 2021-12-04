def solve(data):
    return sum(data[i] < data[i + 1] for i in range(len(data) - 1))


def solve_2(data):
    return sum(sum(data[i:i + 3]) < sum(data[i + 1:i + 4]) for i in range(len(data) - 3))


test_data = '''199
200
208
210
200
207
240
269
260
263'''

with open('input/day_1.txt') as f:
    data = [line.rstrip() for line in f]
    # data = [line.rstrip() for line in test_data.splitlines()]
data = [int(line) for line in data]
# print(solve(data))
print(solve_2(data))
# print(solve_2(test_data.split()))

# NOt 1957
