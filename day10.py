import re
import operator
from functools import reduce
import collections
import heapq

PATTERN = re.compile(r"^\[([#.]+)\] ((?:\([0-9,]+\) )+)\{([0-9,]+)\}$")


def day10part1(input_: str):
    result = 0
    for line in input_.strip().splitlines():
        lights, buttons, _ = parse_machine_desc(line.strip())
        steps = find_least_presses(lights, buttons)
        result += len(steps)

    return result


def parse_machine_desc(line):
    m = PATTERN.match(line.strip())
    light_diagram = m.group(1)
    lights = reduce(
        operator.or_, ((c == "#") << i for (i, c) in enumerate(light_diagram))
    )
    button_list = m.group(2)
    buttons = []
    for button_desc in button_list.split():
        bit_indices = map(int, button_desc[1:-1].split(","))
        buttons.append(reduce(operator.or_, (1 << i for i in bit_indices)))
    joltage_info = m.group(3)
    joltages = list(map(int, joltage_info.split(",")))
    return lights, buttons, joltages


def find_least_presses(light_pattern, buttons):
    operations = {button: [button] for button in buttons}
    while light_pattern not in operations:
        old_ops = list(operations.items())
        for pattern1, sequence1 in old_ops:
            for pattern2, sequence2 in old_ops:
                new_pattern = pattern1 ^ pattern2
                if new_pattern != 0 and (
                    new_pattern not in operations
                    or len(operations[new_pattern]) > len(sequence1) + len(sequence2)
                ):
                    operations[new_pattern] = [*sequence1, *sequence2]
    return operations[light_pattern]

TEST_INPUT = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""


def test_part1():
    assert day10part1(TEST_INPUT) == 7


def test_parse_line():
    assert parse_machine_desc(
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}"
    ) == (0b01000, [0b11101, 0b1100, 0b10001, 0b111, 0b11110], [7, 5, 12, 7, 2])


def test_example_1():
    lights, buttons, _ = parse_machine_desc(
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
    )
    steps = find_least_presses(lights, buttons)
    assert len(steps) == 2


if __name__ == "__main__":
    from aoc_harness import puzzle_main

    puzzle_main(day10part1)
