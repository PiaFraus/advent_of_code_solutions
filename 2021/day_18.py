import json
import math


def add_to_left(x, value):
    if isinstance(x, int):
        return x + value
    return [add_to_left(x[0], value), x[1]]


def add_to_right(x, value):
    if isinstance(x, int):
        return x + value
    return [x[0], add_to_right(x[1], value)]


def explode(x, level=0):
    if isinstance(x, int):
        return x, None
    left, right = x
    if level == 4:
        return 0, (left, right)
    new_left, explosion = explode(left, level + 1)
    if explosion:
        return [new_left, add_to_left(right, explosion[1])], (explosion[0], 0)
    new_right, explosion = explode(right, level + 1)
    if explosion:
        return [add_to_right(left, explosion[0]), new_right], (0, explosion[1])
    return [new_left, new_right], None


def split(x):
    if isinstance(x, int):
        if x >= 10:
            return [x // 2, math.ceil(x / 2)]
        return x
    left, right = x
    new_left = split(left)
    if left != new_left:
        return [new_left, right]
    return [left, split(right)]


def sn_reduce(x, level=0):
    # [[[[[9,8],1],2],3],4] -> [[[[0,9],2],3],4]
    prev_x, new_x = x, x
    while True:
        prev_x, new_x = new_x, explode(new_x)[0]
        if prev_x != new_x:
            # print(f'after explode: {new_x=}')
            continue
        prev_x, new_x = new_x, split(new_x)
        if prev_x != new_x:
            # print(f'after split: {new_x=}')
            continue
        return new_x


def sn_add(x, y):
    # print(f'after addition: {[x, y]}')
    return sn_reduce([x, y])


def sn_magn(x):
    if isinstance(x, int):
        return x
    return sn_magn(x[0]) * 3 + sn_magn(x[1]) * 2


def solve(data):
    result = None
    for line in data:
        snail_number = json.loads(line)
        if result is None:
            result = snail_number
            continue
        result = sn_add(result, snail_number)
    return sn_magn(result)


def solve_2(data):
    result = float('-inf')
    for line1 in data:
        for line2 in data:
            if line1 != line2:
                snail_number1 = json.loads(line1)
                snail_number2 = json.loads(line2)
                result = max(result, sn_magn(sn_add(snail_number1, snail_number2)))
    return result


test_data = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''

if __name__ == '__main__':
    # test = find_explode_index([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]])
    # test = explode([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]])
    # assert test == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
    with open('input/day_18.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
