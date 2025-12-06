import operator
from functools import reduce

OPERATORS = {"*": operator.mul, "+": operator.add}


def day06part1(input: str):
    lines = input.strip().splitlines()
    numbers = [*map(lambda line: [*map(int, line.split())], lines[:-1])]

    operators = [OPERATORS[op] for op in lines[-1].split()]

    n = len(numbers)
    m = len(numbers[0])

    return sum(
        reduce(operators[j], [numbers[i][j] for i in range(n)]) for j in range(m)
    )


def day06part2(input: str):
    lines = input.strip("\n").split("\n")
    line_lengths = [*map(len, lines)]
    line_len = line_lengths[0]
    assert all(l == line_len for l in line_lengths)
    problems = []
    # find blank columns
    start_of_problem = 0
    for col in range(line_len + 1):
        if col == line_len or all(line[col] == " " for line in lines):
            this_problem = [line[start_of_problem:col] for line in lines]
            problems.append(this_problem)
            start_of_problem = col + 1

    transposed_problems = map(parse_col_problem, problems)
    return sum(reduce(op, vals) for (op, vals) in transposed_problems)


def parse_col_problem(problem):
    w = len(problem[0])
    h = len(problem) - 1
    op = OPERATORS[problem[-1].strip()]

    vals = [
        int("".join(problem[row][col] for row in range(h)))
        for col in range(w - 1, -1, -1)
    ]
    return op, vals


# fmt: off
TEST_INPUT = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""
# fmt: on


def test_part1():
    assert day06part1(TEST_INPUT) == 4277556


def test_part2():
    assert day06part2(TEST_INPUT) == 3263827


if __name__ == "__main__":
    import aoc_harness

    aoc_harness.puzzle_main(day06part1, day06part2)
