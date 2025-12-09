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
    coords = np.fromstring(
        input_.strip().replace("\n", ","), sep=",", dtype="i8"
    ).reshape((-1, 2))
    line_segments = np.stack([coords, np.roll(coords, -1, axis=0)], axis=1)
    vert_segments = line_segments[line_segments[:, 0, 0] == line_segments[:, 1, 0]]
    vert_seg_x = vert_segments[:, 0, 0]
    vert_seg_min_y = np.min(vert_segments[:, :, 1], axis=1)
    vert_seg_max_y = np.max(vert_segments[:, :, 1], axis=1)
    horz_segments = line_segments[line_segments[:, 0, 1] == line_segments[:, 1, 1]]
    horz_seg_y = horz_segments[:, 0, 1]
    horz_seg_min_x = np.min(horz_segments[:, :, 0], axis=1)
    horz_seg_max_x = np.max(horz_segments[:, :, 0], axis=1)

    ii = np.arange(len(coords), dtype="i8")
    II, JJ = np.meshgrid(ii, ii)

    zipped = np.stack([coords[II], coords[JJ]], axis=2)
    xy1 = np.min(zipped, axis=2)
    x1 = xy1[:, :, 0]
    y1 = xy1[:, :, 1]
    xy2 = np.max(zipped, axis=2)
    x2 = xy2[:, :, 0]
    y2 = xy2[:, :, 1]

    areas = np.prod(np.abs(coords[II] - coords[JJ]) + 1, axis=-1)
    invalid = np.zeros_like(II, dtype=bool)

    for x, min_y, max_y in zip(vert_seg_x, vert_seg_min_y, vert_seg_max_y):
        invalid[(x1 < x) & (x < x2) & (min_y < y2) & (max_y > y1)] = True

    for y, min_x, max_x in zip(horz_seg_y, horz_seg_min_x, horz_seg_max_x):
        invalid[(y1 < y) & (y < y2) & (min_x < x2) & (max_x > x1)] = True

    return np.max(areas[~invalid])


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


def test_part2():
    assert day09part2(TEST_INPUT) == 24


if __name__ == "__main__":
    from aoc_harness import puzzle_main

    puzzle_main(day09part1, day09part2)
