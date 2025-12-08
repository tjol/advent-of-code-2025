from functools import reduce
import operator
import numpy as np


def day08part1(input_: str, *, n=1000):
    coords = np.fromstring(
        input_.strip().replace("\n", ","), sep=",", dtype="u8"
    ).reshape((-1, 3))
    ii = np.arange(len(coords), dtype="u8")
    II, JJ = np.meshgrid(ii, ii)
    sq_dists = np.sum((coords[II] - coords[JJ]) ** 2, axis=-1)
    full_sq_dist_list = np.stack([sq_dists, II, JJ], axis=-1).reshape((-1, 3))
    sq_dist_list = full_sq_dist_list[full_sq_dist_list[:, 1] < full_sq_dist_list[:, 2]]

    sq_dist_list = sq_dist_list[np.argsort(sq_dist_list[:, 0])]

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
    coords = np.fromstring(
        input_.strip().replace("\n", ","), sep=",", dtype="u8"
    ).reshape((-1, 3))
    ii = np.arange(len(coords), dtype="u8")
    II, JJ = np.meshgrid(ii, ii)
    sq_dists = np.sum((coords[II] - coords[JJ]) ** 2, axis=-1)
    full_sq_dist_list = np.stack([sq_dists, II, JJ], axis=-1).reshape((-1, 3))
    sq_dist_list = full_sq_dist_list[full_sq_dist_list[:, 1] < full_sq_dist_list[:, 2]]

    sq_dist_list = sq_dist_list[np.argsort(sq_dist_list[:, 0])]

    count = len(coords)
    circuits = [{i} for i in range(len(coords))]

    while len(circuits[0]) != count:
        (_, i, j) = sq_dist_list[0]
        sq_dist_list = sq_dist_list[1:]
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
