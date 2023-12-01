import re
from collections import Counter
from collections import defaultdict


def walk(current_path, turned_valves, current_cost, current_value, valve_paths, valve_rates):
    if current_cost >= 30:
        return current_value, current_path, turned_valves,
    results = []
    for option in valve_paths[current_path[-1]]:
        new_path = current_path + (option,)
        if (value := valve_rates[option] and not option in turned_valves):  # Additional choice to move and turn on
            results.append(
                walk(new_path, turned_valves + (option,), current_cost + 2, current_value + value, valve_paths,
                     valve_rates))
        results.append(walk(new_path, turned_valves, current_cost + 1, current_value, valve_paths, valve_rates))
    return max(results)


def prune_zero_value_paths(valve_paths, valve_rates):
    move_costs = {}
    extended_paths = valve_paths.copy()
    for node, options in extended_paths.items():
        for option in options:
            move_costs[sorted((node, option))] = 1
    touched = set(move_costs.keys())
    while touched:
        a, b = touched.pop()
        mc = move_costs[sorted((a,b))]
        for option in extended_paths[a]:
            known_cost = move_costs[sorted((option, b))]
            new_cost = mc + move_costs[sorted((option, b))]
            if move_costs.get(path, float('inf')) <


def solve(data):
    counter = Counter()
    valve_rates = {}
    valve_paths = defaultdict(set)
    result, a, b = 0, 0, 0
    for line in data:
        match_result = re.match('Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)
        if not match_result:
            pass
        valve, rate, valves = match_result.groups()
        for v in valves.split(', '):
            valve_paths[valve].add(v)
        if rate := int(rate):
            valve_rates[valve] = rate

    result = walk(('AA',), (), 0, 0, valve_paths, valve_rates)
    return result


def solve_2(data):
    counter = Counter()
    result, a, b = 0, 0, 0
    for line in data:
        pass
    return result


test_data = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''

if __name__ == '__main__':
    with open('input/day_16.txt') as f:
        # data = [line.rstrip() for line in f]
        data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
