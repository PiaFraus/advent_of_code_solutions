from math import sqrt
from functools import partial
from timeit import timeit


def solve(data):
    tiles = parse_input(data)
    side_to_tile_state, tile_state_to_sides = create_lookups(tiles)
    map_state, size = find_map(tiles, side_to_tile_state, tile_state_to_sides)
    corners = map_state[0], map_state[size - 1], map_state[size ** 2 - 1], map_state[size ** 2 - size]
    results = 1
    for c in corners:
        results *= c[0]
    return results


def solve_2(data):
    tiles = parse_input(data)
    side_to_tile_state, tile_state_to_sides = create_lookups(tiles)
    map_state, size = find_map(tiles, side_to_tile_state, tile_state_to_sides)
    sea_monster = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #
'''
    sea_monster = sea_monster[1:].splitlines()
    sm_coordinates = sea_monster_to_coordinates(sea_monster)
    sm_dimensions = len(sea_monster), len(sea_monster[0])
    cleaned_tiles = []
    for tile_number, flip, rotation in map_state:
        tile = tiles[tile_number]
        if flip:
            tile = [list(row)[-2:0:-1] for row in tile[1:-1]]
        else:
            tile = [list(row)[1:-1:1] for row in tile[1:-1]]
        for _ in range(rotation):
            tile = rotate_square_matrix(tile)
        cleaned_tiles.append(tile)
    tile_size = len(cleaned_tiles[0])
    full_map = [[None for _ in range(tile_size * size)] for _ in range(tile_size * size)]
    for i in range(tile_size * size):
        for j in range(tile_size * size):
            tile_row, within_tile_row = i // tile_size, i % tile_size
            tile_column, within_tile_column = j // tile_size, j % tile_size
            full_map[i][j] = cleaned_tiles[tile_row * size + tile_column][within_tile_row][within_tile_column]

    for flip in range(2):
        for _ in range(4):
            results = 0
            for i, line in enumerate(full_map[:-sm_dimensions[0]]):
                for j, char in enumerate(line[:-sm_dimensions[1]]):
                    if all(full_map[i + x][j + y] == '#' for x, y in sm_coordinates):
                        for x, y in sm_coordinates:
                            full_map[i + x][j + y] = 'O'
                        results += 1
            if results:
                print_tile(full_map)
                return sum(line.count('#') for line in full_map)
            full_map = rotate_square_matrix(full_map)
        full_map = flip_square_matrix(full_map)

def sea_monster_to_coordinates(sea_monster):
    result = []
    for i, line in enumerate(sea_monster):
        for j, char in enumerate(line):
            if char == '#':
                result.append((i, j))
    return result

def print_tile(tile):
    print('\n'.join(''.join(r) for r in tile))

def rotate_square_matrix(m):
    return [list(row[::-1]) for row in zip(*m)]

def flip_square_matrix(m):
    return [list(row[::-1]) for row in m]

def parse_input(data):
    tiles = {}
    current_tile = None
    for line in data:
        if not line:
            continue
        if line.startswith('Tile '):
            current_tile = int(line.removeprefix('Tile ')[:-1])
            continue
        tiles.setdefault(current_tile, []).append(line)
    return tiles

def create_lookups(tiles):
    side_to_tile_state = [{}, {}, {}, {}, ]
    tile_state_to_sides = {}
    for tile_number, tile in tiles.items():
        right_side = ''.join(row[-1] for row in tile)
        left_side = ''.join(row[0] for row in tile)
        top = tile[0]
        down = tile[-1]
        tile_sides = top, right_side, down, left_side
        for flip in (0, 1):
            if flip == 1:
                tile_sides = flip_tile(tile_sides)
            for rotation in range(4):
                tile_state_to_sides[tile_number, flip, rotation] = tile_sides
                for side, lookup in zip(tile_sides, side_to_tile_state):
                    lookup.setdefault(side, set()).add((tile_number, flip, rotation))
                tile_sides = rotate_tile(tile_sides)
    return side_to_tile_state, tile_state_to_sides

def rotate_tile(sides):
    a, b, c, d = sides
    return d[::-1], a, b[::-1], c

def flip_tile(sides):
    a, b, c, d = sides
    return a[::-1], d, c[::-1], b

def find_map(tiles, side_to_tile_state, tile_state_to_sides):
    size = int(sqrt(len(tiles)))
    map_state = None
    for first_tile in tile_state_to_sides:
        map_state = [first_tile]
        if try_next_tile(map_state, size, tile_state_to_sides, side_to_tile_state):
            break
    return map_state, size

def try_next_tile(map_state, size, tile_state_to_sides, side_to_tile_state):
    num_of_tiles = len(map_state)
    if num_of_tiles == size ** 2:
        return True
    used_tiles = {tile_state[0] for tile_state in map_state}
    i, j = num_of_tiles // size, num_of_tiles % size
    options = set()
    if i:
        upper_tile_state = map_state[num_of_tiles - size]
        down = tile_state_to_sides[upper_tile_state][2]
        applicable_ups = side_to_tile_state[0].get(down, set())
        options = applicable_ups if not options else options.intersection(applicable_ups)
    if j:
        left_tile_state = map_state[num_of_tiles - 1]
        right_side = tile_state_to_sides[left_tile_state][1]
        applicable_lefts = side_to_tile_state[3].get(right_side, set())
        options = applicable_lefts if not options else options.intersection(applicable_lefts)
    options = {o for o in options if o[0] not in used_tiles}
    if not options:
        return False
    for o in options:
        map_state.append(o)
        if try_next_tile(map_state, size, tile_state_to_sides, side_to_tile_state):
            return True
        map_state.pop()


test_data = ''''''

with open('input/day_20.txt') as f:
    data = [line.rstrip() for line in f]
  print(timeit(partial(solve_2, data), number=10))
