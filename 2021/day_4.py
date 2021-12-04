def solve(data):
    numbers = map(int, data[0].split(','))
    boards = []
    boards_mask = set()
    for line in data[1:]:
        if not line:
            boards.append([])
            continue
        boards[-1].append(list(map(int, line.split())))
    for n in numbers:
        for board_index, board in enumerate(boards):
            for i, row in enumerate(board):
                for j, value in enumerate(row):
                    if value == n:
                        boards_mask.add((board_index, i, j))
                        if sum((board_index, x, j) in boards_mask for x in range(5)) == 5 or sum((board_index, i, x) in boards_mask for x in range(5))==5:
                            score = sum(boards[board_index][a][b] for a in range(5) for b in range(5) if (board_index, a, b) not in boards_mask)
                            return score * value
    return 0




def solve_2(data):
    numbers = map(int, data[0].split(','))
    boards = []
    boards_mask = set()
    winner_boards = set()
    for line in data[1:]:
        if not line:
            boards.append([])
            continue
        boards[-1].append(list(map(int, line.split())))
    for n in numbers:
        for board_index, board in enumerate(boards):
            if board_index in winner_boards:
                continue
            for i, row in enumerate(board):
                for j, value in enumerate(row):
                    if value == n:
                        boards_mask.add((board_index, i, j))
                        if sum((board_index, x, j) in boards_mask for x in range(5)) == 5 or sum(
                                (board_index, i, x) in boards_mask for x in range(5)) == 5:
                            winner_boards.add(board_index)
                            if len(boards) == len(winner_boards):
                                score = sum(boards[board_index][a][b] for a in range(5) for b in range(5) if
                                            (board_index, a, b) not in boards_mask)
                                return score * value
    return 0

test_data = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

if __name__ == '__main__':
    with open('input/day_4.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
