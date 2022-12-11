import math
import operator
from collections import Counter
from collections import deque
from functools import partial


class Monkey:
    def __init__(self, index) -> None:
        self.index = index
        self.items = deque()
        self.divisor = None
        self.throw_if_true = None
        self.throw_if_false = None
        self.op = None
        self.value = None


OPS = {
    '+': operator.add,
    '*': operator.mul,
}


def solve(data):
    counter = Counter()
    result, a, b = 0, 0, 0
    data = iter(data)
    monkeys = []
    while True:
        new_monkey = Monkey(int(next(data).strip().removeprefix('Monkey ').removesuffix(':')))
        new_monkey.items = deque(map(int, next(data).strip().removeprefix('Starting items: ').split(', ')))
        operation = next(data).strip().removeprefix('Operation: new = old ')
        new_monkey.op, new_monkey.value = operation.split()
        new_monkey.value = 'old' if new_monkey.value == 'old' else int(new_monkey.value)
        new_monkey.operation = lambda old: partial(OPS[new_monkey.op], old,
                                                   old if new_monkey.value == 'old' else int(new_monkey.value))
        new_monkey.divisor = int(next(data).strip().removeprefix('Test: divisible by '))
        new_monkey.throw_if_true = int(next(data).strip().removeprefix('If true: throw to monkey '))
        new_monkey.throw_if_false = int(next(data).strip().removeprefix('If false: throw to monkey '))
        monkeys.append(new_monkey)
        if next(data, None) is None:
            break
    for round in range(20):
        print(f"{round=}")
        for m in monkeys:
            print(f"Monkey {m.index}")
            for item in m.items:
                value = item if m.value == 'old' else m.value
                new_worry = OPS[m.op](item, value) // 3
                print(f"Worry level is now = {new_worry}")
                throw_to = monkeys[m.throw_if_true] if new_worry % m.divisor == 0 else monkeys[m.throw_if_false]
                print(f"Item with worry level {new_worry} is thrown to monkey {throw_to.index}")
                throw_to.items.append(new_worry)
            counter[m.index] += len(m.items)
            m.items.clear()

    return operator.mul(*(mc[1] for mc in counter.most_common(2)))


def solve_2(data):
    counter = Counter()
    result, a, b = 0, 0, 0
    data = iter(data)
    monkeys = []
    while True:
        new_monkey = Monkey(int(next(data).strip().removeprefix('Monkey ').removesuffix(':')))
        new_monkey.items = deque(map(int, next(data).strip().removeprefix('Starting items: ').split(', ')))
        operation = next(data).strip().removeprefix('Operation: new = old ')
        new_monkey.op, new_monkey.value = operation.split()
        new_monkey.value = 'old' if new_monkey.value == 'old' else int(new_monkey.value)
        new_monkey.operation = lambda old: partial(OPS[new_monkey.op], old,
                                                   old if new_monkey.value == 'old' else int(new_monkey.value))
        new_monkey.divisor = int(next(data).strip().removeprefix('Test: divisible by '))
        new_monkey.throw_if_true = int(next(data).strip().removeprefix('If true: throw to monkey '))
        new_monkey.throw_if_false = int(next(data).strip().removeprefix('If false: throw to monkey '))
        monkeys.append(new_monkey)
        if next(data, None) is None:
            break
    # for m in monkeys:
    #     m.items.clear()
    # monkeys[0].items.append(79)
    cycle = math.prod(m.divisor for m in monkeys)
    for round in range(10000):
        if round % 1000 == 0:
            print(f"{round=}")
            print(f"{counter=}")
        for m in monkeys:
            # print(f"Monkey {m.index}")
            for item in m.items:
                value = item if m.value == 'old' else m.value
                new_worry = OPS[m.op](item, value) % cycle
                # print(f"Worry level is now = {new_worry}")
                throw_to = monkeys[m.throw_if_true] if new_worry % m.divisor == 0 else monkeys[m.throw_if_false]
                # print(f"Item with worry level {new_worry} is thrown to monkey {throw_to.index}")
                throw_to.items.append(new_worry)
            counter[m.index] += len(m.items)
            m.items.clear()

    return operator.mul(*(mc[1] for mc in counter.most_common(2)))


test_data = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''

if __name__ == '__main__':
    with open('input/day_11.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
