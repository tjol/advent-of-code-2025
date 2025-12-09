import numpy as np


def day09part1(input_: str):
    coords = np.fromstring(
        input_.strip().replace("\n", ","), sep=",", dtype="i8"
    ).reshape((-1, 2))
    ii = np.arange(len(coords), dtype="i8")
    II, JJ = np.meshgrid(ii, ii)
    areas = np.prod(np.abs(coords[II] - coords[JJ]) + 1, axis=-1)
    full_area_list = np.stack([areas, II, JJ], axis=-1).reshape((-1, 3))
    area_list = full_area_list[full_area_list[:, 1] < full_area_list[:, 2]]

    sorted_areas = np.sort(area_list[:, 0])
    return sorted_areas[-1]


def day09part2(input_: str):
    pass


TEST_INPUT = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


def test_part1():
    assert day09part1(TEST_INPUT) == 50


# def test_part2():
#     assert day09part2(TEST_INPUT) == 0


if __name__ == "__main__":
    from aoc_harness import puzzle_main

    puzzle_main(day09part1, day09part2)
