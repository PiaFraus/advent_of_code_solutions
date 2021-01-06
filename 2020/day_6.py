def solve(data, *args, **kwargs):
    a, result = 0, 0
    group = None
    for line in data:
        if not line:
            result += len(group) if group else 0
            group = None
            continue
        if group is None:
            group = set(line)
        else:
            group = group.intersection(set(line))

    return result

test_data = '''
abc

a
b
c

ab
ac

a
a
a
a

b

'''

with open('input/day_6.txt') as f:
    data = [line.rstrip() for line in f]
results = solve(data)
print(results)
