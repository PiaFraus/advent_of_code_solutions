import functools
import itertools
from ast import literal_eval


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return None if a == b else a < b
    if isinstance(a, list) and isinstance(b, list):
        for sub_a, sub_b in zip(a, b):
            if (cmp := compare(sub_a, sub_b)) is not None:
                return cmp
        return None if len(a) == len(b) else len(a) < len(b)
    return compare([a], b) if isinstance(a, int) else compare(a, [b])

def solve(data):
    result = 0
    data = iter(data)
    for i in itertools.count(1):
        first = next(data)
        second = next(data)
        if next(data, None) is None:
            break
        cmp = compare(literal_eval(first), literal_eval(second))
        print(f"{i=} {first=}, {second=}, {cmp=}, {result=}")
        if cmp:
            result += i
    return result


def solve_2(data):
    all_packets = [[[2]], [[6]]]
    for line in data:
        if line:
            all_packets.append(literal_eval(line))
    all_packets.sort(key=functools.cmp_to_key(lambda a, b: 1 if compare(a, b) else -1), reverse=True)
    return (all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)


test_data = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''

if __name__ == '__main__':
    with open('input/day_13.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
