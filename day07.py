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


if __name__ == "__main__":
    from aoc_harness import puzzle_main

    puzzle_main(day07part1)
