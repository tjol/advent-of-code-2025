def day07part1(input_: str):
    world = [*map(list, input_.strip().splitlines())]

    splits = 0

    for y in range(1, len(world)):
        for x in range(len(world[y])):
            above = world[y - 1][x]
            here = world[y][x]
            if above in ("S", "|"):
                if here == "^":
                    splits += 1
                    world[y][x - 1] = "|"
                    world[y][x + 1] = "|"
                elif here == ".":
                    world[y][x] = "|"

    return splits


def day07part2(input_: str):
    world = [*map(list, input_.strip().splitlines())]
    timeline_map = [[1 if c == "S" else 0 for c in row] for row in world]

    splits = 0

    for y in range(1, len(world)):
        for x in range(len(world[y])):
            above = timeline_map[y - 1][x]
            obstacle = world[y][x]
            if above == 0:
                continue
            if obstacle == "^":
                timeline_map[y][x - 1] += above
                timeline_map[y][x + 1] += above
            else:
                timeline_map[y][x] += above

    return sum(timeline_map[-1])


TEST_INPUT = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""


def test_part1():
    assert day07part1(TEST_INPUT) == 21


def test_part2():
    assert day07part2(TEST_INPUT) == 40


if __name__ == "__main__":
    from aoc_harness import puzzle_main

    puzzle_main(day07part1, day07part2)
