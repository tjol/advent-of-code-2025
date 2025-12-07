def day01part1(input: str):
    zeros = 0
    pos = 50
    for line in input.strip().splitlines():
        sign = (-1) if line[0] == "L" else (+1)
        delta = int(line[1:]) * sign
        pos = (pos + delta) % 100
        if pos == 0:
            zeros += 1

    return zeros


def day01part2(input: str):
    zero_passes = 0
    pos = 50
    for line in input.strip().splitlines():
        sign = (-1) if line[0] == "L" else (+1)
        delta = int(line[1:]) * sign

        dest = pos + delta
        if dest <= 0:
            if pos > 0:
                zero_passes += 1
            zero_passes += (-dest) // 100
            pos = dest % 100
        else:
            zero_passes += dest // 100
            pos = dest % 100

    return zero_passes


TEST_INPUT_1 = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def test_part1():
    assert day01part1(TEST_INPUT_1) == 3


def test_part2():
    assert day01part2(TEST_INPUT_1) == 6


if __name__ == "__main__":
    from aoc_harness import puzzle_main

    puzzle_main(day01part1, day01part2)
