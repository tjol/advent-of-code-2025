import itertools


def day02part1(input: str):
    ranges = [
        tuple(map(int, range_str.split("-"))) for range_str in input.strip().split(",")
    ]
    max_val = max(r[1] for r in ranges)

    invalid_sum = 0
    for i in itertools.count(1):
        invalid_num = int(2 * str(i))
        if invalid_num > max_val:
            break
        for n, m in ranges:
            if n <= invalid_num <= m:
                invalid_sum += invalid_num
                break

    return invalid_sum


def day02part2(input: str):
    ranges = [
        tuple(map(int, range_str.split("-"))) for range_str in input.strip().split(",")
    ]
    max_val = max(r[1] for r in ranges)

    invalid_nums = set()
    for i in itertools.count(1):
        any_tested = False
        for k in itertools.count(2):
            invalid_num = int(k * str(i))
            if invalid_num > max_val:
                break

            any_tested = True

            for n, m in ranges:
                if n <= invalid_num <= m:
                    invalid_nums.add(invalid_num)
                    break
        if not any_tested:
            break

    return sum(invalid_nums)


TEST_INPUT_1 = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def test_part1():
    assert day02part1(TEST_INPUT_1) == 1227775554


def test_part2():
    assert day02part2(TEST_INPUT_1) == 4174379265


if __name__ == "__main__":
    from aoc_harness import puzzle_main

    puzzle_main(day02part1, day02part2)
