import re

def solve(data, dimensions):
    result = 0
    for line in data:
        tokens = tokenize(line)
        
        result += calculate(tokens)[0]
    return result


def tokenize(line):
    line = line.replace(' ', '')
    return re.findall('(\d+|[\+\*\(\)])', line)


def calculate(tokens, start=0):
    result = 0
    op = None
    i = start
    while True:
        if i >= len(tokens):
            return result, i
        t = tokens[i]
        if t in '+*':
            op = t
            i += 1
            continue
        if t == ')':
            return result, i
        if t == '(':
            value, end_pos = calculate(tokens, i + 1)
            i = end_pos
        else:
            value = int(t)
        if op is None:
            result = value
        elif op == '+':
            result += value
        elif op == '*':
            result *= value
        else:
            raise Exception
        i += 1


test_data = '''5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
'''

with open('input/day_18.txt') as f:
    data = [line.rstrip() for line in f]
    # data = [line.rstrip() for line in test_data.splitlines()]
print(solve(data, 100))


class FakeNumber(int):
    def __mul__(self, x: int) -> int:
        return FakeNumber(super().__add__(x))

    def __sub__(self, x: int) -> int:
        return FakeNumber(super().__mul__(x))


def solve_2(line):
    fake_line = re.sub(r'(\d+)', r'FakeNumber(\1)', line, )
    fake_line = fake_line.replace('*', '-').replace('+', '*')
    return eval(fake_line)


result = 0
for line in data:
    result += solve_2(line)

print(result)
