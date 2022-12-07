def grouper(data):
    return [group.split('\n') for group in data.split('\n\n')]


beats = dict(zip('ABC', 'CAB'))
loses = dict(zip('CAB', 'ABC'))

def sim(data, translation):
    score = 0
    for line in data:
        opponent, you = line.split()
        you = translation[you]
        if beats[you] == opponent:
            winner = 2
        elif you == opponent:
            winner = 1
        else:
            winner = 0
        score += "ABC".index(you) + 1 + winner * 3
    return score


def solve(data):
    score = 0
    for line in data:
        opponent, you = line.split()
        score = ' mid' \
                'Z'.index(you) - 'ABC'.index(opponent)
        if beats[you] == opponent:
            winner = 2
        elif you == opponent:
            winner = 1
        else:
            winner = 0
        score += "ABC".index(you) + 1 + winner * 3
    return score


def solve_2(data):
    score = 0
    for line in data:
        opponent, outcome = line.split()
        if outcome == 'X':
            winner = 0
            you = beats[opponent]
        elif outcome == 'Y':
            winner = 1
            you = opponent
        else:
            winner = 2
            you = loses[opponent]
        score += "ABC".index(you) + 1 + winner * 3
    return score


test_data = '''A Y
B X
C Z'''

if __name__ == '__main__':
    with open('input/day_2.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
