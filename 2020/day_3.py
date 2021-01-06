def solve(data, right, down):
    pos, result = right, 0
    for line in data[down::down]:
        result += line[pos] == '#'
        pos = (pos + right) % len(line)
    return result


with open('input/day_3.txt') as f:
    data = [line.rstrip() for line in f]
results = [solve(data, right, down) for (right, down) in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))]
r = 1
for x in results:
    r *= x
print(r)
