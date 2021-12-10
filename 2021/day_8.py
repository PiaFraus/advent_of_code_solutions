"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""
import itertools
from collections import Counter
from collections import defaultdict

_DIGITS = [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg',
]
_LEN_TO_POSSIBILITIES = defaultdict(set)
for digit, signals in enumerate(_DIGITS):
    _LEN_TO_POSSIBILITIES[len(signals)].add(signals)


def solve(data):
    counter = Counter()
    result, a, b = 0, 0, 0
    for line in data:
        digits, output = line.split('|')
        digits = digits.split(' ')
        output = output.split(' ')
        for d in output:
            if len(d) in (2, 4, 3, 7):
                result += 1
        pass
    return result


S = 'abcdefg'

def test_translation(tr_table, digits):
    for d in digits:
        if not d: continue
        x = ''.join(sorted(d.translate(tr_table)))
        if x not in _DIGITS:
            return False
    return True

def solve_2(data):
    counter = Counter()
    all_translates = set(''.join(x) for x in itertools.permutations('abcdefg'))
    result, a, b = 0, 0, 0
    for line in data:
        if not line: continue
        translations = all_translates.copy()
        digits, output = line.split('|')
        digits = digits.split(' ')
        output = output.split(' ')
        signal_possibilities = {c: set(S) for c in S}
        for d in digits:
            digit_possibilities = _LEN_TO_POSSIBILITIES[len(d)]
            if len(digit_possibilities) == 1:
                impossible = set(S) - set(d)
                if not impossible:
                    continue
                for c in list(digit_possibilities)[0]:
                    signal_possibilities[c] -= impossible
        new_translations = [t for t in translations if all(x in signal_possibilities[y] for x, y in zip(t, S))]
        for translation in new_translations:
            tr_table = str.maketrans(translation, S)
            if test_translation(tr_table, digits):
                value = 0
                for d in output:
                    if not d:
                        continue
                    value *= 10
                    value += _DIGITS.index(''.join(sorted(d.translate(tr_table))))
                result+=value
        pass
    return result


test_data = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |fgae cfgab fg bagce'''

if __name__ == '__main__':
    with open('input/day_8.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
