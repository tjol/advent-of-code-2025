from functools import reduce
import operator


def day08part1(input_: str, *, n=1000):
    coords = [tuple(map(int, l.split(","))) for l in input_.strip().splitlines()]

    sq_dist_list = []
    for i, a in enumerate(coords):
        for j, b in enumerate(coords[i + 1 :], start=i + 1):
            sq_dist = sum((a_ - b_) ** 2 for a_, b_ in zip(a, b))
            sq_dist_list.append((sq_dist, i, j))

    sq_dist_list.sort()
    circuits = [{i} for i in range(len(coords))]

    for _, i, j in sq_dist_list[:n]:
        c1 = circuits[i]
        c2 = circuits[j]
        c1.update(c2)
        for k in c1:
            circuits[k] = c1

    uniq_circuits = set(map(frozenset, circuits))
    by_size = sorted(uniq_circuits, key=len)
    return reduce(operator.mul, (len(c) for c in by_size[-3:]))


def day08part2(input_: str):
    coords = [tuple(map(int, l.split(","))) for l in input_.strip().splitlines()]

    sq_dist_list = []
    for i, a in enumerate(coords):
        for j, b in enumerate(coords[i + 1 :], start=i + 1):
            sq_dist = sum((a_ - b_) ** 2 for a_, b_ in zip(a, b))
            sq_dist_list.append((sq_dist, i, j))

    sq_dist_list.sort(reverse=True)
    count = len(coords)
    circuits = [{i} for i in range(len(coords))]

    while len(circuits[0]) != count:
        (_, i, j) = sq_dist_list.pop()
        c1 = circuits[i]
        c2 = circuits[j]
        c1.update(c2)
        for k in c1:
            circuits[k] = c1

    return coords[i][0] * coords[j][0]


TEST_INPUT = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""


def test_part1():
    assert day08part1(TEST_INPUT, n=10) == 40


def test_part2():
    assert day08part2(TEST_INPUT) == 25272


if __name__ == "__main__":
    from aoc_harness import puzzle_main

    puzzle_main(day08part1, day08part2)
