import time
from itertools import product, permutations, combinations

def manhatten(p1, p2):
    return sum(abs(x-y) for x,y in zip(p1, p2))

def sub_vec3(a, b):
    return tuple(a - b for a, b in zip(a, b))

def cross_vec3(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

def solve(data):
    scanner_beacons = []
    for line in data:
        if not line:
            continue
        if line.startswith('--- scanner'):
            scanner_beacons.append([])
            continue
        scanner_beacons[-1].append(tuple(map(int, line.split(','))))
    found_beacons = set(scanner_beacons[0])
    found_scanners = {0: None}
    my_solution_order = [27, 19, 21, 13, 5, 10, 11, 15, 12, 9, 14, 17, 20, 28, 30, 6, 7, 16, 26, 29, 4, 31, 22, 1, 3,
                         23, 24, 25, 33, 34, 8, 2, 35, 18, 36, 32, 37, 38, 39]
    shifts = []
    t = time.time()
    while True:
        for scanner_index, sb in enumerate(scanner_beacons):
            if scanner_index in found_scanners:
                continue
            shift, aligned = bruteforce(found_beacons, sb)
            if aligned:
                found_beacons |= aligned
                shifts.append(shift)
                new_t = time.time()
                print(f'Found scanner {scanner_index} shift = {shift}. Took {new_t-t:.3}')
                t = new_t
                found_scanners[scanner_index] = aligned
                break
        else:
            break

    return len(found_beacons), max(manhatten(a, b) for a, b in combinations(shifts, 2))


def bruteforce(found_beacons, sb):
    for axes_order in permutations(range(3), 3):
        for axes_directions in product([-1, 1], [-1, 1], [-1, 1]):
            rotation_aligned = [(b[axes_order[0]] * axes_directions[0],
                                 b[axes_order[1]] * axes_directions[1],
                                 b[axes_order[2]] * axes_directions[2]) for b in sb]
            for p in rotation_aligned:
                for fb in found_beacons:
                    shift = sub_vec3(p, fb)
                    aligned = {sub_vec3(x, shift) for x in rotation_aligned}
                    if len(found_beacons & aligned) >= 12:
                        return shift, aligned
    return None, set()


test_data = '''--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14'''

if __name__ == '__main__':
    with open('input/day_19.txt') as f:
        # data = [line.rstrip() for line in f]
        data = [line.rstrip() for line in test_data.splitlines()]
    # data = [int(line, 2) for line in data]

    print(solve(data))

my_results_from_logs = [(-1382, 30, 20),
                        (-1280, 1226, 40),
                        (-2477, 47, -2),
                        (-2490, 5, 1182),
                        (-2480, 3, 2458),
                        (-2537, -1246, 2376),
                        (-1205, -1142, 1150),
                        (-3624, -61, 1278),
                        (-3752, -1215, 1257),
                        (-2530, -2402, 1217),
                        (-3687, 1240, 1176),
                        (-2565, -1122, 1218),
                        (-2566, 1130, 2367),
                        (-1267, -42, -1112),
                        (-4847, 15, 1282),
                        (-4832, -80, 84),
                        (-3785, -48, -1211),
                        (-6041, -14, 1191),
                        (-6132, 1177, 1173),
                        (-7324, 63, 1168),
                        (-8571, 45, 1296),
                        (-1258, 1243, -1158),
                        (-1254, 1265, -2471),
                        (-1212, 1236, -3556),
                        (-1252, 1184, -4724),
                        (-1276, -54, -3592),
                        (-124, 1141, -2453),
                        (-1280, 2409, -2479),
                        (-2450, -92, -1130),
                        (-1367, 2453, 57),
                        (-2468, 2482, -55),
                        (-3607, 2449, 97),
                        (-1273, -1108, -78),
                        (-1321, -2335, -49),
                        (-172, -2, 1300),
                        (-150, -60, 2414),
                        (-2557, 1262, -2305),
                        (-1370, 2400, 1165),
                        (-1253, -14, -2421)]
