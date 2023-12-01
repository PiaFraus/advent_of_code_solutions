import re


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve(data, control_y=10):
    sensors = {}
    for line in data:
        groups = re.match('Sensor at x=(.?\d+), y=(.?\d+): closest beacon is at x=(.?\d+), y=(.?\d+)', line).groups()
        x, y, bx, by, = map(int, groups)
        sensors[x, y] = bx, by
    ranges = []
    for s, b in sensors.items():
        md = distance(s, b)
        if (dy := abs(control_y - s[1])) <= md:
            ranges.append((s[0] - md + dy, s[0] + md - dy))
    beacons_on_control = {x for x, y in sensors.values() if y == control_y}
    result = 0
    last_end = float("-inf")
    for r in sorted(ranges):
        if r[1] > last_end:
            result += r[1] + 1 - max(last_end, r[0])
            for bx in beacons_on_control:
                if last_end <= bx <= r[1]:
                    result -= 1
            last_end = r[1] + 1
    return result


def solve_2(data, max_x):
    max_x = max_x * 2
    sensors = {}
    for line in data:
        groups = re.match('Sensor at x=(.?\d+), y=(.?\d+): closest beacon is at x=(.?\d+), y=(.?\d+)', line).groups()
        x, y, bx, by, = map(int, groups)
        sensors[x, y] = distance((x, y), (bx, by))
    sorded_sensor_md = sorted(sensors.items())
    for control_y in range(0, max_x + 1):
        ranges = []
        for s, md in sorded_sensor_md:
            if (dy := abs(control_y - s[1])) <= md:
                ranges.append((s[0] - md + dy, s[0] + md - dy))
        last_end = 0
        ranges.sort()
        for r in ranges:
            if r[0] > last_end + 1:
                return last_end + 1, control_y, ((last_end + 1) * 4000000 + control_y)
            last_end = max(last_end, r[1])
        if control_y % 10000 == 0:
            print(f"{control_y=}")


test_data = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''

# Not 2557297 * 3267339 = 8355556222683
if __name__ == '__main__':
    with open('input/day_15.txt') as f:
        data = [line.rstrip() for line in f], 2000000
        # data = [line.rstrip() for line in test_data.splitlines()], 10
    # data = [int(line, 2) for line in data]

    print(solve(*data))
    print(solve_2(*data))
