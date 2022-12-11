from collections import defaultdict

sample = '''inp w
mul x 0
add x z
mod x 26
div z
add x
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y
mul y x
add z y'''


def preprocess_code(data):
    values = defaultdict(list)
    template = sample.splitlines()
    line: str
    for i, line in enumerate(data):
        expected = template[i % len(template)]
        if not line.startswith(expected):
            raise 'A'
        leftover = line.removeprefix(expected)
        if leftover:
            values[i // len(template)].append(leftover)
    return [list(map(int, values[i])) for i in sorted(values)]


#
# my_actual_input = [
#     [1, 12, 15],  # w!=x guaranteed, z must be 0
#     [1, 14, 12],  # w!=x guaranteed z must < 26
#     [1, 11, 15],  # w!=x guaranteed, z must < 26**2
#     [26, -9, 12],  # Z <  26**3
#     [26, -7, 15],  # Z <  26**2
#     [1, 11, 2],  # w!=x guaranteed, z < 26
#     [26, -1, 11],  # MUST have w==x and z < 26**2 OR z = 0
#     [26, -16, 15],  # MUST have w==x and z<26
#     [1, 11, 10],  # w!=x guaranteed, z MUST be 0
#     [26, -15, 2],  # MUST have w==x and z<26
#     [1, 10, 0],  # w!=x guaranteed, z MUST be 0
#     [1, 12, 0],  # w!=x guaranteed, z MUST be 0
#     [26, -4, 15]  # MUST have w==x and z<26
# ]
#
# z_cap = list(reversed([26, 1, 1, 26, 1, 26, 26 ** 2, 26, 26 ** 2, 26 ** 3, 26 ** 2, 26, 1]))


# the_actual_code
def f(w, z, a, b, c):
    x = (z % 26) + b
    z = z // a
    if w != x:
        z = z * 26 + w + c
    return z


# z > o ALWAYS
# z increases when w != x or shrinks by //
# So for z to be 0
# we MUST have z < 26 on last 3 steps and either it to be 0 or w!=x
# if b > 10, then w!=x guaranteed
#
def solve(my_actual_input, z_cap, z=0, step=0, previous=()):
    print(previous, step, z)
    if step == len(my_actual_input):
        return previous
    a, b, c = my_actual_input[step]
    x = (z % 26) + b
    for w in range(9, 0, -1):
        z_w = z // a
        if w != x:
            z_w = z_w * 26 + w + c
        if z_w > z_cap[step + 1]:
            continue
        if (result := solve(my_actual_input, z_cap, z_w, step + 1, previous + (w,))) is not None:
            return result

def solve_2(my_actual_input, z_cap, z=0, step=0, previous=()):
    print(previous, step, z)
    if step == len(my_actual_input):
        return previous
    a, b, c = my_actual_input[step]
    x = (z % 26) + b
    for w in range(1, 10):
        z_w = z // a
        if w != x:
            z_w = z_w * 26 + w + c
        if z_w > z_cap[step + 1]:
            continue
        if (result := solve_2(my_actual_input, z_cap, z_w, step + 1, previous + (w,))) is not None:
            return result


if __name__ == '__main__':
    with open('input/day_24.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    my_actual_input = preprocess_code(data)
    z_cap = [0]
    allowance_counter = 0
    for a, b, c in reversed(my_actual_input):
        allowance_counter += 1 if a == 26 else -1
        z_cap.append(26 ** allowance_counter)
    # data = [int(line, 2) for line in data]
    z_cap = tuple(reversed(z_cap))
    print(solve(my_actual_input, z_cap))
    print(solve_2(my_actual_input, z_cap))

# 94399898949959 21176121611511