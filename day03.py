from functools import partial


def day03part1(in_data: str):
    banks = in_data.strip().split("\n")

    return sum(map(max_joltage, banks))


def day03part2(in_data: str):
    banks = in_data.strip().split("\n")

    return sum(map(partial(max_joltage, digits=12), banks))


def max_joltage(bank, digits=2):
    joltage_str = ""
    for i in range(digits):
        head = bank[: len(bank) - (digits - i - 1)]
        digit, neg_idx = max((d, -j) for (j, d) in enumerate(head))
        joltage_str += digit
        bank = bank[-neg_idx + 1 :]
    return int(joltage_str)


TEST_INPUT_1 = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


def test_part1():
    assert day03part1(TEST_INPUT_1) == 357


def test_part1():
    assert day03part2(TEST_INPUT_1) == 3121910778619


if __name__ == "__main__":
    from aoc_harness import puzzle_main

    puzzle_main(day03part1, day03part2)
