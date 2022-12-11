import heapq
from collections import Counter
from copy import deepcopy

AMPHIPODS = 'ABCD'
AMPHIPODS_TO_COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
AMPHIPODS_ROOM_POSITIONS = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
AMPHIPODS_ROOM_POSITIONS_LOOKUP = {v: k for k, v in AMPHIPODS_ROOM_POSITIONS.items()}


class Game:
    ROOM_START = 2
    CORRIDOR = 1

    def __init__(self, data, cost=0):
        self.data = data
        # self.corridor = self.data[1]
        self.room_depth = len(self.data) - 3
        self.cost = cost
        self.ready_rooms = Counter()
        self.refresh_rooms()

    @property
    def completed(self):
        return sum(self.ready_rooms.values()) == 4 * self.room_depth

    def refresh_room(self, a_type):
        self.ready_rooms[a_type] = 0
        pos = AMPHIPODS_ROOM_POSITIONS[a_type]
        for depth in range(self.ROOM_START, self.ROOM_START + self.room_depth):
            if self.data[depth][pos] not in ('.', a_type):
                if a_type in self.ready_rooms:
                    self.ready_rooms.pop(a_type)
                break
            elif self.data[depth][pos] == a_type:
                self.ready_rooms[a_type] += 1

    def refresh_rooms(self):
        self.ready_rooms.clear()
        for a_type in AMPHIPODS:
            self.refresh_room(a_type)

    @staticmethod
    def distance_to_move(from_x, from_y, to_x, to_y):
        if from_x == to_x:
            return abs(from_y - to_y)
        return from_y - Game.CORRIDOR + to_y - Game.CORRIDOR + abs(from_x - to_x)

    def cost_to_move(self, from_x, from_y, to_x, to_y, amphipod=None):
        if not amphipod:
            amphipod = self.data[from_y][from_x]
        step_cost = AMPHIPODS_TO_COST[amphipod]
        return step_cost * self.distance_to_move(from_x, from_y, to_x, to_y)

    def move(self, from_x, from_y, to_x, to_y):
        self.cost += self.cost_to_move(from_x, from_y, to_x, to_y)
        self.data[to_y][to_x] = self.data[from_y][from_x]
        self.data[from_y][from_x] = '.'
        if from_y != self.CORRIDOR:
            self.refresh_room(AMPHIPODS_ROOM_POSITIONS_LOOKUP[from_x])

    def move_to_room(self, corridor_pos):
        a = self.data[self.CORRIDOR][corridor_pos]
        assert a in self.ready_rooms
        target_depth = self.ROOM_START + self.room_depth - self.ready_rooms[a] - 1
        self.move(corridor_pos, self.CORRIDOR, AMPHIPODS_ROOM_POSITIONS[a], target_depth)
        self.refresh_room(a)

    def state_estimation_simple(self):
        return sum((self.ready_rooms[a_type])*cost for a_type, cost in AMPHIPODS_TO_COST.items())

    def state_estimation(self):
        return self.state_estimation_simple()
        filled = Counter()
        total_cost = 0
        for pos, a in enumerate(self.data[self.CORRIDOR]):  # corridor first
            if a in '#.':
                continue
            total_cost += self.cost_to_move(pos, 1, AMPHIPODS_ROOM_POSITIONS[a],
                                            self.ROOM_START + self.room_depth - filled[a])
            filled[a] += 1
        for a_type, pos in AMPHIPODS_ROOM_POSITIONS.items():
            for depth in range(self.ROOM_START, self.ROOM_START + self.room_depth):
                a = self.data[depth][pos]
                if a not in AMPHIPODS:
                    continue
                target_position = self.ROOM_START + self.room_depth - filled[a] - 1
                if a in self.ready_rooms:
                    if a == a_type:  # cost can be negative here as we technically needed to move other amphipod here,
                        # which we didn't have to do, so refund
                        total_cost += (target_position - depth) * AMPHIPODS_TO_COST[a]
                        filled[a] += 1
                    else:
                        total_cost += self.cost_to_move(pos, depth, AMPHIPODS_ROOM_POSITIONS[a], target_position)
                        filled[a] += 1
                else:
                    total_cost += self.cost_to_move(pos, depth, AMPHIPODS_ROOM_POSITIONS[a], self.CORRIDOR)
                    total_cost += self.cost_to_move(AMPHIPODS_ROOM_POSITIONS[a], self.CORRIDOR, AMPHIPODS_ROOM_POSITIONS[a], target_position, amphipod=a)
                    filled[a] += 1

        return total_cost

    def options_to_move(self):
        options = []
        for a_type, pos in AMPHIPODS_ROOM_POSITIONS.items():
            if a_type in self.ready_rooms:
                continue
            for depth in range(self.ROOM_START, self.ROOM_START + self.room_depth):
                a = self.data[depth][pos]
                if a == '.':
                    continue
                for left_pos in range(pos - 1, 0, -1):
                    if self.data[self.CORRIDOR][left_pos] != '.':
                        break
                    elif left_pos not in AMPHIPODS_ROOM_POSITIONS.values():
                        options.append((pos, depth, left_pos, self.CORRIDOR))
                for right_pos in range(pos + 1, len(self.data[self.CORRIDOR])):
                    if self.data[self.CORRIDOR][right_pos] != '.':
                        break
                    elif right_pos not in AMPHIPODS_ROOM_POSITIONS.values():
                        options.append((pos, depth, right_pos, self.CORRIDOR))
                break
        return options

    def solve(self):
        # 1. if there is a ready room and a way to move bots there - do that
        # 2. Move a piece from room SOMEWHERE and do a recursion
        self.move_to_rooms()

    def move_to_rooms(self):
        while True:
            state_changed = False
            for a_type, filled in self.ready_rooms.items():
                if filled == self.room_depth:
                    continue
                pos = AMPHIPODS_ROOM_POSITIONS[a_type]
                for left_pos in range(pos - 1, 1, -1):
                    if self.data[self.CORRIDOR][left_pos] == a_type:
                        self.move_to_room(left_pos)
                        state_changed = True
                    elif self.data[self.CORRIDOR][left_pos] != '.':
                        break
                for right_pos in range(pos + 1, len(self.data[self.CORRIDOR])):
                    if self.data[self.CORRIDOR][right_pos] == a_type:
                        self.move_to_room(right_pos)
                        state_changed = True
                    elif self.data[self.CORRIDOR][right_pos] != '.':
                        break
            for a_type, pos in AMPHIPODS_ROOM_POSITIONS.items():  # A shortcut
                if a_type in self.ready_rooms:
                    continue
                for depth in range(self.ROOM_START, self.ROOM_START + self.room_depth):
                    a = self.data[depth][pos]
                    if a == '.':
                        continue
                    if a in self.ready_rooms:
                        destination = AMPHIPODS_ROOM_POSITIONS[a]
                        from_, to_ = min(pos, destination), max(pos, destination)
                        if self.data[self.CORRIDOR][from_: to_+1] == ['.']*(to_ - from_):
                            self.move(pos, depth, pos, self.CORRIDOR)
                            self.move_to_room(pos)
                            state_changed = True
                    break
            if not state_changed:
                break

    def __str__(self):
        return '\n'.join(''.join(line) for line in self.data)

    def __lt__(self, other):
        return self.cost < other.cost


def solve(data):
    # columns = list(zip(*(for line in data[2:-1])))
    states = [(0, Game(list(map(list, data))))]
    observed = set()
    while True:
        _, game = heapq.heappop(states)
        # print(f'Next game to look with cost {game.cost} and score {_} is \n{game}')
        if game.completed:
            return game.cost
        options = game.options_to_move()
        for o in options:
            new_game = deepcopy(game)
            # new_game.previous_game = game
            new_game.move(*o)
            new_game.move_to_rooms()
            state = str(new_game)
            if state in observed:
                continue
            heapq.heappush(states, (new_game.cost, new_game))
            observed.add(state)
            # print(f'{o}, {new_game.cost}, {new_game.cost - new_game.state_estimation_simple()}, {"".join(new_game.data[1])}')


part_2_insert = '''#D#C#B#A#
#D#B#A#C#'''


def solve_2(data, insert=part_2_insert):
    counter = Counter()
    result, a, b = 0, 0, 0
    for line in data:
        pass
    return result


test_data = '''#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########'''

test_data_2 = '''#############
#...........#
###A#B#D#C###
  #A#B#C#D#
  #########'''

if __name__ == '__main__':
    with open('input/day_23.txt') as f:
        # data = [line.rstrip() for line in f]
        data = [line.rstrip() for line in test_data.splitlines()]
        # data = [line.rstrip() for line in test_data_2.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
# # ############
# # #...........#
# # ###C#B#D#D###
# #   #B#C#A#A#
# #   #########
#
# # ############
# # #.........D.#
# # ###C#B#D#.###
# #   #B#C#A#A#
# #   #########
# 2000
# # ############
# # #.....A...D.#
# # ###C#B#D#.###
# #   #B#C#A#.#
# #   #########
# 2000 + 5
# # ############
# # #.....A.....#
# # ###C#B#.#D###
# #   #B#C#A#D#
# #   #########
# 9000 + 5
#
# # ############
# # #.A.........#
# # ###C#B#.#D###
# #   #B#C#A#D#
# #   #########
# 9000 + 9
# # ############
# # #.A.B.......#
# # ###C#.#.#D###
# #   #B#C#A#D#
# #   #########
# 9000 + 9 + 20
# # ############
# # #.A.B...A...#
# # ###C#.#.#D###
# #   #B#C#.#D#
# #   #########
# 9000 + 12 + 20
# # ############
# # #.A.B...A...#
# # ###C#.#.#D###
# #   #B#.#C#D#
# #   #########
# 9000 + 12 + 20 + 600
# # ############
# # #.A.....A...#
# # ###C#.#.#D###
# #   #B#B#C#D#
# #   #########
# 9000 + 12 + 50 + 600
# # ############
# # #.A.....A...#
# # ###.#.#C#D###
# #   #B#B#C#D#
# #   #########
# 9000 + 12 + 50 + 1200
# # ############
# # #.A.....A...#
# # ###.#B#C#D###
# #   #.#B#C#D#
# #   #########
# 9000 + 21 + 100 + 1200
# # ############
# # #...........#
# # ###A#B#C#D###
# #   #A#B#C#D#
# #   #########

# #############
# #...........#
# ###C#B#D#D###
#   #D#C#B#A#
#   #D#B#A#C#
#   #B#C#A#A#
#   #########

# #############
# #.........D.#
# ###C#B#D#.###
#   #D#C#B#A#
#   #D#B#A#C#
#   #B#C#A#A#
#   #########
