def day05part1(input: str):
    ranges_section, ids_section = input.strip().split("\n\n")
    ranges = [tuple(map(int, line.split("-"))) for line in ranges_section.splitlines()]
    ranges = normalize_ranges(ranges)
    ids = [*map(int, ids_section.splitlines())]

    fresh = 0
    for id_ in ids:
        for from_, to_ in ranges:
            if from_ <= id_ <= to_:
                fresh += 1
                break
    return fresh


def day05part2(input: str):
    ranges_section, _ids_section = input.strip().split("\n\n")
    ranges = [tuple(map(int, line.split("-"))) for line in ranges_section.splitlines()]

    ranges = normalize_ranges(ranges)
    return sum(end - beg + 1 for (beg, end) in ranges)


def normalize_ranges(ranges):
    accepted = []
    unmerged = sorted(ranges, reverse=True)
    while len(unmerged) >= 2:
        a1, a2 = unmerged.pop()
        b1, b2 = unmerged[-1]
        if b1 <= a2 + 1:
            # overlap or adjacent
            unmerged[-1] = (a1, max(a2, b2))
        else:
            # no overlap (with any)
            accepted.append((a1, a2))
    assert len(unmerged) == 1
    accepted.append(unmerged[0])
    return accepted


TEST_INPUT = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def test_part1():
    assert day05part1(TEST_INPUT) == 3


def test_part2():
    assert day05part2(TEST_INPUT) == 14


if __name__ == "__main__":
    import aoc_harness

    aoc_harness.puzzle_main(day05part1, day05part2)
