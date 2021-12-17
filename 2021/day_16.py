from functools import reduce
from itertools import count


def parse_packet(data):
    version = int(data[0:3], 2)
    type_id = int(data[3:6], 2)
    if type_id == 4:
        value = ''
        for i in count():
            value += data[7 + i * 5:7 + i * 5 + 4]
            if data[6 + i * 5] == '0':
                return version, int(value, 2), 7 + i * 5 + 4
    length_type = data[6]
    consumed = 0
    values = []
    if length_type == '0':
        subpackets_len = int(data[7:7 + 15], 2)
        while consumed < subpackets_len:
            sp_version, value, consumed_bits = parse_packet(data[7 + 15 + consumed:])
            version += sp_version
            consumed += consumed_bits
            values.append(value)
        consumed += 7 + 15
    else:
        subpackets_number = int(data[7:7 + 11], 2)
        consumed = 0
        for i in range(subpackets_number):
            sp_version, value, consumed_bits = parse_packet(data[7 + 11 + consumed:])
            version += sp_version
            consumed += consumed_bits
            values.append(value)
        consumed += 7 + 11
    if type_id == 0:
        value = sum(values)
    elif type_id == 1:
        value = reduce(lambda a, b: a*b, values, 1)
    elif type_id == 2:
        value = min(values)
    elif type_id == 3:
        value = max(values)
    elif type_id == 5:
        assert len(values) == 2
        value = int(values[0] > values[1])
    elif type_id == 6:
        assert len(values) == 2
        value = int(values[0] < values[1])
    elif type_id == 7:
        assert len(values) == 2
        value = int(values[0] == values[1])
    else:
        assert False
    return version, value, consumed


def solve(data):
    bindata = bin(int(data[0], 16)).removeprefix('0b')
    bindata = bindata.zfill(len(bindata) + (4 - len(bindata) % 4) % 4 + 4 * data[0].startswith('0'))
    return parse_packet(bindata)[0]


def solve_2(data):
    bindata = bin(int(data[0], 16)).removeprefix('0b')
    bindata = bindata.zfill(len(bindata) + (4 - len(bindata) % 4) % 4 + 4 * data[0].startswith('0'))
    return parse_packet(bindata)[1]


test_data = '''9C0141080250320F1802104A08'''

if __name__ == '__main__':
    with open('input/day_16.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
