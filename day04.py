import numpy as np
from scipy import ndimage


def day04part1(in_data: str):
    lines = in_data.strip().split("\n")
    rolls = np.array([[c == "@" for c in line] for line in lines], dtype="u1")
    kernel = np.ones([3, 3], dtype="u1")
    neighbourhood = ndimage.convolve(rolls, kernel, mode="constant", cval=0)
    accessible = (rolls == 1) & (neighbourhood < 5)
    return np.count_nonzero(accessible)


def day04part2(in_data: str):
    lines = in_data.strip().split("\n")
    rolls = np.array([[c == "@" for c in line] for line in lines], dtype="u1")
    kernel = np.ones([3, 3], dtype="u1")
    removed = 0
    while True:
        neighbourhood = ndimage.convolve(rolls, kernel, mode="constant", cval=0)
        accessible = (rolls == 1) & (neighbourhood < 5)
        n_accessible = np.count_nonzero(accessible)
        if n_accessible == 0:
            break
        else:
            removed += n_accessible
            rolls -= accessible

    return removed


TEST_INPUT_1 = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def test_part1():
    assert day04part1(TEST_INPUT_1) == 13


def test_part2():
    assert day04part2(TEST_INPUT_1) == 43


if __name__ == "__main__":
    from aoc_harness import puzzle_main

    puzzle_main(day04part1, day04part2)
