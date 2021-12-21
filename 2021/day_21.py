import itertools
from collections import Counter
from itertools import cycle


def roll_die():
    for i in cycle(range(100)):
        yield i + 1

def solve(sp1, sp2):
    position = [sp1, sp2]
    score = [0, 0]
    die = roll_die()
    n = 0
    for i in cycle((0, 1)):
        roll = sum(next(die) for _ in range(3))
        n += 3
        position[i] = (position[i] + roll - 1) % 10 + 1
        score[i] += position[i]
        if score[i] >= 1000:
            break
    return min(score) * n


SUMS_DISTRIBUTION = Counter(map(sum, itertools.product(*itertools.tee((1,2,3), 3))))
def solve_4(previous_sums, positions, scores):
    winners = [0, 0]
    turn_order = len(previous_sums) % 2
    for dice_sum, number in SUMS_DISTRIBUTION.items():
        new_position = (positions[turn_order] + dice_sum - 1) % 10 + 1
        new_score = scores[turn_order] + new_position
        if new_score >= 21:
            winners[turn_order] += number
            continue
        new_positions = (new_position, positions[1]) if turn_order == 0 else (positions[0], new_position)
        new_scores = (new_score, scores[1]) if turn_order == 0 else (scores[0], new_score)
        nw1, nw2 = solve_4(previous_sums + (dice_sum,), new_positions, new_scores)
        winners[0] += nw1 * number
        winners[1] += nw2 * number
    return winners


if __name__ == '__main__':
    print(solve(4, 8))
    print(solve(3, 10))
    print(solve_4((), (4,8), (0,0)))
    print(solve_4((), (3,10), (0,0)))
