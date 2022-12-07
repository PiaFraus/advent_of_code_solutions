from collections import Counter


def solve(data):
    total_sizes = Counter()
    current_dir = ['', ]
    for line in data:
        if line.startswith('$ cd '):
            next_dir = line.removeprefix('$ cd ')
            if next_dir == '/':
                current_dir = ['/', ]
            elif next_dir == '..':
                current_dir.pop()
            else:
                current_dir.append(next_dir)
        elif line == '$ ls':
            pass
        elif line.startswith('dir'):
            pass
        else:
            size, filename = line.split()
            size = int(size)
            for i in range(len(current_dir)):
                total_sizes['/'.join(current_dir[:i+1])] += size
    return sum(v for v in total_sizes.values() if v <= 100000)


def solve_2(data):
    total = 70000000
    need = 30000000
    total_sizes = Counter()
    current_dir = ['', ]
    for line in data:
        if line.startswith('$ cd '):
            next_dir = line.removeprefix('$ cd ')
            if next_dir == '/':
                current_dir = ['/', ]
            elif next_dir == '..':
                current_dir.pop()
            else:
                current_dir.append(next_dir)
        elif line == '$ ls':
            pass
        elif line.startswith('dir'):
            pass
        else:
            size, filename = line.split()
            size = int(size)
            for i in range(len(current_dir)):
                total_sizes['/'.join(current_dir[:i+1])] += size
    need_to_remove = need - (total - total_sizes['/'])
    for v in sorted(total_sizes.values()):
        if v >= need_to_remove:
            return v

test_data = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

if __name__ == '__main__':
    with open('input/day_7.txt') as f:
        data = [line.rstrip() for line in f]
        # data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))
    print(solve_2(data))
